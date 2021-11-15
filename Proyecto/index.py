from flask import Flask, render_template

app = Flask(__name__)

"""""
@app.route('/')
def principal():
    return "Bienvenid@ a mi sitio con python!"

@app.route('/contacto')
def contacto():
    return "Esta es la pagina de contacto"
"""

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/lenguajes')
def mostrarLenguajes():
    mislenguajes=("PHP","Python","Java","C#",
                "JavaScript","Perl","Ruby","Rust")
    return render_template('lenguajes.html', Lenguajes=mislenguajes)

@app.route('/contactos')
def contacto():
    return render_template('contactos.html')



if __name__ == '__main__':
    app.run(debug=True, port=5017)

