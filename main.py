import sqlite3
from moderador_ia import analizar_toxicidad

conexion = sqlite3.connect('forotech.db')
cursor = conexion.cursor()

while True:
        comentario = input("\nIntroduce un comentario (o 'salir'): ")

        if comentario.lower() == 'salir':
                print("Cerrando el moderador. ¡Hasta pronto!")
                break

        puntuacion = analizar_toxicidad(comentario)
        print(f"Puntuación de toxicidad: {puntuacion}")

        if puntuacion < 0.40:
                print("hermoso comentario chaval, tenkiu")
                estado = "Bueno"
        elif puntuacion <= 0.70:
                print("comentario dudoso detectado, cuidaito chamo")
                estado = "Dudoso"
        else:
                print("comentario toxico detectado, fuera de aqui mano")
                estado = "Toxico"

        # Guardamos en la base de datos
        cursor.execute("INSERT INTO comentarios (comentario_escrito) VALUES (?)", (comentario,))
        id_comentario = cursor.lastrowid

        cursor.execute("INSERT INTO moderaciones (tipo_comentario, id_comentario, puntuacion) VALUES (?, ?, ?)", 
                        (estado, id_comentario, puntuacion))
        conexion.commit()