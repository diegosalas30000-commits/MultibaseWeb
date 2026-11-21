from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# RUTA EXACTA DEL ARCHIVO QUE ABRISTE EN DBEAVER
RUTA_DB = r"C:\Users\Usuario\Music\proyectos github\MultibaseSalud\bin\Debug\sistema.db"

def obtener_datos():
    conn = sqlite3.connect(RUTA_DB)
    cursor = conn.cursor()
    
    # 1. Verificamos si hay alumnos, si no, los insertamos
    cursor.execute("SELECT COUNT(*) FROM db_control_escolar")
    if cursor.fetchone()[0] == 0:
        print("La base de datos está vacía. Insertando datos de prueba...")
        cursor.executescript("""
            INSERT INTO db_control_escolar (id_estudiante, nombre_alumno, carrera, materias_cursadas, disponible) VALUES
            (1, 'Sofía Ramírez', 'Ingeniería en Sistemas', 'Bases de Datos, Programación, Ciencia de Datos', 'Sí'),
            (2, 'Carlos Mendoza', 'Inteligencia Artificial', 'Bases de Datos, Machine Learning, Minería de Datos', 'Sí'),
            (3, 'Andrea Torres', 'Ingeniería Industrial', 'Gestión de Procesos, Logística', 'Sí');

            INSERT INTO db_portafolio (id_estudiante, titulo_proyecto, dominio, tecnologias) VALUES
            (1, 'Dashboard Predictivo para Inventarios', 'Salud', 'Python, Pandas, SQL'),
            (2, 'Modelo de Redes Neuronales', 'Salud', 'Python, TensorFlow'),
            (3, 'Sistema Web de Control Clínico', 'Salud', 'PHP, MySQL, JavaScript');

            INSERT INTO db_becas (id_estudiante, tipo_beca, estatus_beca) VALUES
            (1, 'Apoyo Económico', 'Activa'),
            (2, 'Apoyo Económico', 'Activa'),
            (3, 'Ninguna', 'Pendiente');
        """)
        conn.commit()

    # 2. Hacemos la consulta
    conn.row_factory = sqlite3.Row
    query = """
        SELECT 
            e.id_estudiante,
            e.nombre_alumno AS Estudiante,
            e.carrera AS Carrera,
            p.titulo_proyecto AS Proyecto,
            p.tecnologias AS Tecnologias,
            b.tipo_beca AS Beca
        FROM db_control_escolar e
        LEFT JOIN db_portafolio p ON e.id_estudiante = p.id_estudiante
        LEFT JOIN db_becas b ON e.id_estudiante = b.id_estudiante
        WHERE e.disponible = 'Sí' AND p.dominio = 'Salud'
    """
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.close()
    return datos

@app.route('/')
def index():
    alumnos = obtener_datos()
    return render_template('index.html', alumnos=alumnos)

@app.route('/asignar', methods=['POST'])
def asignar():
    ids_seleccionados = request.form.getlist('estudiantes')
    
    if ids_seleccionados:
        conn = sqlite3.connect(RUTA_DB)
        cursor = conn.cursor()
        
        for id_est in ids_seleccionados:
            cursor.execute("""
                INSERT INTO db_asignacion_equipos (id_estudiante, id_reto, nombre_equipo, rol_asignado, estatus_aceptacion) 
                VALUES (?, 1, 'Equipo MedPredict-ITSLP', 'Candidato Aceptado', 'Aceptado')
            """, (id_est,))
        
        cursor.execute("UPDATE db_dependencias SET estado_reto = 'asignado' WHERE id_reto = 1")
        
        conn.commit()
        conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)