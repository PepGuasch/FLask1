from flask import Flask, render_template, request

app = Flask(__name__)

def guardar_datos_en_archivo(datos):
    with open('datos_formulario.txt', 'a') as archivo:
        archivo.write(datos + '\n')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        destino = request.form['destino']
        necesidades = request.form.getlist('necesidades')

        # Formatea los datos para guardarlos en el archivo de texto
        datos = f'Nombre: {nombre}, Dirección: {direccion}, Teléfono: {telefono}, Email: {email}, Destino: {destino}, Necesidades: {", ".join(necesidades)}'

        # Guarda los datos en el archivo de texto
        guardar_datos_en_archivo(datos)

        # Puedes redirigir a una página de confirmación o mostrar un mensaje de confirmación
        return 'Formulario enviado correctamente, Su viaje ha sido reservado con exito!'
    else:
        return render_template('index.html')
        
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)