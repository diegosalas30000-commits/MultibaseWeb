import sqlite3
import os

print("Buscando la base de datos en:", os.getcwd())
conn = sqlite3.connect('sistema.db')
cursor = conn.cursor()

print("\n--- TABLAS EN ESTA BASE DE DATOS ---")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
for tabla in cursor.fetchall():
    print("-", tabla[0])

print("\n--- DATOS EN db_asignacion_equipos ---")
try:
    cursor.execute("SELECT * FROM db_asignacion_equipos")
    filas = cursor.fetchall()
    if len(filas) == 0:
        print("¡ALERTA! La tabla está vacía (0 filas).")
    else:
        for fila in filas:
            print(fila)
except Exception as e:
    print("Error:", e)

conn.close()