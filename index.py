from flask import Flask, render_template
#ctrl+shitf+R (refresh)
app = Flask(__name__)

@app.route('/') #localhost:5000
def home():
    return render_template('home.html')

@app.route('/proyectos')#localhost:5000/about
def proyectos():
    return render_template('proyectos.html')

if __name__=='__main__':
    app.run(debug=True) #Para modo prueba (no sera necesario cerrar el programa)

    #pip freze para lo requirements
    #runtime es tipo de python
