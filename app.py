from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# RUTA EXACTA DEL ARCHIVO
RUTA_DB = r"C:\Users\Usuario\Music\proyectos github\MultibaseSalud\bin\Debug\sistema.db"

def obtener_datos():
    # Lista ampliada de candidatos (Simulando el cruce multibase)
    return [
        {"id_estudiante": 1, "Estudiante": "Sofía Ramírez", "Carrera": "Ingeniería en Sistemas", "Proyecto": "Dashboard Predictivo para Inventarios", "Tecnologias": "Python, Pandas, SQL", "Beca": "Apoyo Económico"},
        {"id_estudiante": 2, "Estudiante": "Carlos Mendoza", "Carrera": "Inteligencia Artificial", "Proyecto": "Modelo de Redes Neuronales", "Tecnologias": "Python, TensorFlow", "Beca": "Apoyo Económico"},
        {"id_estudiante": 3, "Estudiante": "Andrea Torres", "Carrera": "Ingeniería Industrial", "Proyecto": "Sistema Web de Control Clínico", "Tecnologias": "PHP, MySQL, JavaScript", "Beca": "Ninguna"},
        {"id_estudiante": 4, "Estudiante": "Luis Hernández", "Carrera": "Ingeniería en Sistemas", "Proyecto": "App Móvil de Telemedicina", "Tecnologias": "Flutter, Firebase", "Beca": "Apoyo Económico"},
        {"id_estudiante": 5, "Estudiante": "María Fernanda Gómez", "Carrera": "Ciencia de Datos", "Proyecto": "Análisis Predictivo de Demanda", "Tecnologias": "R, Python, PowerBI", "Beca": "Ninguna"},
        {"id_estudiante": 6, "Estudiante": "Jorge Luis Morales", "Carrera": "Ciberseguridad", "Proyecto": "Encriptación de Expedientes Médicos", "Tecnologias": "Java, Spring Boot, AES", "Beca": "Apoyo Económico"}
    ]

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