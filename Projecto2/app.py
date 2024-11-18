from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejer1', methods=['GET', 'POST'])
def ejer1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3) / 3
        estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"
        return render_template('ejer1.html', promedio=promedio, estado=estado)
    return render_template('ejer1.html')


@app.route('/ejer2', methods=['GET', 'POST'])
def ejer2():
    if request.method == 'POST':
        # Obtenemos los nombres desde el formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        max_nombre = max([nombre1, nombre2, nombre3], key=len)

        max_length = len(max_nombre)

        return render_template('ejer2.html', max_nombre=max_nombre, max_length=max_length)

    return render_template('ejer2.html')

if __name__ == '__main__':
    app.run(debug=True)