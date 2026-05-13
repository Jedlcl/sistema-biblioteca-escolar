import sqlite3

def crear_bd() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    try:
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        print("Conexion y cursor creados con exito")
        return conexion, cursor
    except sqlite3.Error as e:
        print("Sucedió un error", e)

def crear_tablas(conexion: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    try:
        sql = """CREATE TABLE IF NOT EXISTS Escuela(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            turno TEXT NOT NULL,
            cct TEXT NOT NULL,
            activo INTEGER NOT NULL DEFAULT 1 
        )"""
        cursor.execute(sql)
        sql = """ CREATE TABLE IF NOT EXISTS Salon(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grado INTEGER NOT NULL,
            grupo INTEGER NOT NULL,
            id_escuela INTEGER NOT NULL,
            activo INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (id_escuela) REFERENCES Escuela(id)
        )"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Maestro(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido_paterno TEXT NOT NULL,
            apellido_materno TEXT NOT NULL,
            id_salon INTEGER,
            activo INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (id_salon) REFERENCES Salon(id)
        )"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Alumno(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido_paterno TEXT NOT NULL,
            apellido_materno TEXT NOT NULL,
            notas TEXT,
            id_salon INTEGER NOT NULL ,
            activo INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (id_salon) REFERENCES Salon(id)
        )"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Libro(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT ,
            Nombre TEXT NOT NULL,
            editorial TEXT ,
            autor TEXT ,
            anio_lanzamiento INTEGER,
            activo INTEGER NOT NULL DEFAULT 1
        )"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )"""
        cursor.execute(sql)        
        sql = """CREATE TABLE IF NOT EXISTS Libro_categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_libro INTEGER NOT NULL,
            id_categoria INTEGER NOT NULL,
            FOREIGN KEY (id_libro) REFERENCES Libro(id),
            FOREIGN KEY (id_categoria) REFERENCES Categoria(id)
        )"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Ejemplar(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_libro INTEGER NOT NULL,
            numero_ejemplar INTEGER NOT NULL,
            observaciones TEXT,
            activo INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (id_libro) REFERENCES Libro(id)
        )"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Prestamo(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_ejemplar INTEGER NOT NULL,
            id_alumno INTEGER NOT NULL,
            id_maestro INTEGER NOT NULL,
            fecha_inicio DATE NOT NULL,
            fecha_final DATE NOT NULL,
            nota_devolucion TEXT,
            activo INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (id_ejemplar) REFERENCES Ejemplar(id),
            FOREIGN KEY (id_alumno) REFERENCES Alumno(id),
            FOREIGN KEY (id_maestro) REFERENCES Maestro(id)
        )"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Usuario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_maestro INTEGER NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            rol TEXT NOT NULL,
            activo INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (id_maestro) REFERENCES Maestro(id)
        )"""
        cursor.execute(sql)
        conexion.commit()
        print("Tablas creadas con exito")
    except sqlite3.Error as e:
        print("Ocurrió un error",e)

if __name__ == "__main__":
    conn, cur = crear_bd()
    crear_tablas(conn, cur)