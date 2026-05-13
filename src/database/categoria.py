import sqlite3
from src.models.categoria import Categoria

def insertar_categoria(conexion: sqlite3.Connection, cursor: sqlite3.Cursor, categoria):
    sql = 'INSERT INTO Categoria (id, nombre) VALUES (?)', (Categoria.nombre)