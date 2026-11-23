import sqlite3
conexion = sqlite3.connect('forotech.db')
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS autores (
        id_autor       INT PRIMARY KEY,
        nombre         VARCHAR(20),
        correo         VARCHAR(20),
        fecha_registro DATE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS comentarios (
        id_comentario      INTEGER PRIMARY KEY AUTOINCREMENT,
        id_autor           INTEGER,
        comentario_escrito TEXT,
        fecha_publicacion  DATE,
        FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
    )
""")

cursor.execute("""
create table if not exists moderaciones(
    id_moderacion INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_comentario text check(tipo_comentario in('Bueno', 'Dudoso', 'Toxico')),  
    id_autor int,
    id_comentario int,
    puntuacion real ,                                                          
    foreign key(id_autor) references autores(id_autor),
    foreign key(id_comentario) references comentarios(id_comentario)
);
""")

conexion.commit()
conexion.close()