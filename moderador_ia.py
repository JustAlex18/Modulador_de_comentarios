import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_APIKEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={API_KEY}"

def analizar_toxicidad(texto):
    prompt = (
        "Eres un evaluador de toxicidad para un foro. "
        "Responde EXCLUSIVAMENTE con un numero decimal del 0.0 al 1.0 "
        f"indicando que tan toxico es el siguiente comentario: '{texto}'"
    )
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    
    try:
        respuesta = requests.post(URL, json=payload, timeout=12)
        datos = respuesta.json()
        
        if "candidates" in datos:
            partes = datos["candidates"][0]["content"]["parts"]
            for p in reversed(partes):
                if "text" in p and not p.get("thought", False):
                    # Extrae el número decimal limpio (ej: 0.95)
                    coincidencia = re.search(r"([0-9]+\.[0-9]+|[0-9]+)", p["text"])
                    if coincidencia:
                        return float(coincidencia.group(1))
                        
    except Exception as error:
        print(f"Error en la consulta: {error}")
        
    return 0.0