import sqlite3

# Esta es la ruta exacta que tienes en DBeaver
ruta_db = r"C:\Users\Usuario\Music\proyectos github\MultibaseSalud\bin\Debug\sistema.db"

conn = sqlite3.connect(ruta_db)
cursor = conn.cursor()

# Creamos todas las tablas de un jalón
cursor.executescript("""
CREATE TABLE IF NOT EXISTS db_portafolio (
    id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
    id_estudiante INTEGER,
    titulo_proyecto TEXT NOT NULL,
    dominio TEXT NOT NULL,
    tecnologias TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS db_becas (
    id_beca INTEGER PRIMARY KEY AUTOINCREMENT,
    id_estudiante INTEGER,
    tipo_beca TEXT NOT NULL,
    estatus_beca TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS db_dependencias (
    id_reto INTEGER PRIMARY KEY AUTOINCREMENT,
    entidad_salud TEXT NOT NULL,
    descripcion_problema TEXT NOT NULL,
    estado_reto TEXT NOT NULL
);

INSERT INTO db_portafolio (id_estudiante, titulo_proyecto, dominio, tecnologias) VALUES
(1, 'Dashboard Predictivo', 'Salud', 'Python, Pandas, SQL'),
(2, 'Redes Neuronales', 'Salud', 'Python, TensorFlow'),
(3, 'Sistema Web', 'Salud', 'PHP, MySQL');

INSERT INTO db_becas (id_estudiante, tipo_beca, estatus_beca) VALUES
(1, 'Apoyo Económico', 'Activa'),
(2, 'Apoyo Económico', 'Activa'),
(3, 'Ninguna', 'Pendiente');

INSERT INTO db_dependencias (entidad_salud, descripcion_problema, estado_reto) VALUES
('Secretaría de Salud', 'Desabastecimiento de medicamentos', 'abierto');
""")

conn.commit()
conn.close()
print("¡Las 5 tablas y los datos se crearon correctamente en bin/Debug!")