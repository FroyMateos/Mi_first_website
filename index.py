from flask import Flask, render_template
#ctrl+shitf+R (refresh)
app = Flask(__name__)

@app.route('/') #localhost:5000
def home():
    return render_template('home.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/web')
def web():
    return render_template('web.html')

@app.route('/post')
def post():
    return render_template('post.html')

if __name__=='__main__':
    app.run(debug=True) #Para modo prueba (no sera necesario cerrar el programa)

    #pip freze para los requirements
    #runtime es tipo de python
