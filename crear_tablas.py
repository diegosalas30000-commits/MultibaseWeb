import sqlite3

# Conectamos a la base de datos
conn = sqlite3.connect('sistema.db')
cursor = conn.cursor()

# Creamos las tablas que faltan
cursor.executescript("""
CREATE TABLE IF NOT EXISTS db_control_escolar (
    id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_alumno TEXT NOT NULL,
    carrera TEXT NOT NULL,
    materias_cursadas TEXT NOT NULL,
    disponible TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS db_portafolio (
    id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
    id_estudiante INTEGER,
    titulo_proyecto TEXT NOT NULL,
    dominio TEXT NOT NULL,
    tecnologias TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS db_dependencias (
    id_reto INTEGER PRIMARY KEY AUTOINCREMENT,
    entidad_salud TEXT NOT NULL,
    descripcion_problema TEXT NOT NULL,
    estado_reto TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS db_becas (
    id_beca INTEGER PRIMARY KEY AUTOINCREMENT,
    id_estudiante INTEGER,
    tipo_beca TEXT NOT NULL,
    estatus_beca TEXT NOT NULL
);
""")

# Insertamos los datos
cursor.executescript("""
INSERT INTO db_control_escolar (nombre_alumno, carrera, materias_cursadas, disponible) VALUES
('Sofía Ramírez', 'Ingeniería en Sistemas', 'Bases de Datos, Programación, Ciencia de Datos', 'Sí'),
('Carlos Mendoza', 'Inteligencia Artificial', 'Bases de Datos, Machine Learning, Minería de Datos', 'Sí'),
('Luis Hernández', 'Ingeniería en Sistemas', 'Bases de Datos, Programación Web', 'Sí');

INSERT INTO db_portafolio (id_estudiante, titulo_proyecto, dominio, tecnologias) VALUES
(1, 'Dashboard Predictivo para Inventarios Hospitalarios', 'Salud', 'Python, Pandas, SQL'),
(2, 'Modelo de Redes Neuronales para Alertas de Stock', 'Salud', 'Python, TensorFlow'),
(3, 'Sistema Web de Control Clínico', 'Salud', 'PHP, MySQL, JavaScript');

INSERT INTO db_dependencias (entidad_salud, descripcion_problema, estado_reto) VALUES
('Secretaría de Salud / Hospital Central', 'Sistema inteligente para predecir el desabastecimiento de medicamentos', 'abierto');

INSERT INTO db_becas (id_estudiante, tipo_beca, estatus_beca) VALUES
(1, 'Apoyo Económico de Investigación', 'Activa'),
(2, 'Apoyo Económico de Investigación', 'Activa'),
(3, 'Ninguna', 'Pendiente');
""")

conn.commit()
conn.close()
print("¡Tablas y datos creados con exito!")
