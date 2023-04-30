# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "Aiko" # escribe tu nombre
    age = "16" # escribe tu edad
    img = "me"

    return render_template('index.html' , name = name , age = age, img = img)

# define la ruta a la página web de tu padre.
@app.route("/father")
def padre():
    name = "Celestino"
    age = "35"
    
    return render_template('father.html', name=name, age=age)

# define la ruta a la página web de tu madre.
@app.route("/mother")
def mother():
    name = "Diana"
    age = "43"
    
    return render_template('mother.html', name=name, age=age)

# define la ruta a la página web de tus amigos.
@app.route("/friend")
def friend():
    name = "Gabriela"
    age = "17"
    
    return render_template('friend.html', name=name, age=age)


# agrega otras rutas, si tú quieres.
@app.route("/pet")
def pet():
    name = "Nina"
    age = "1"
    
    return render_template('pet.html', name=name, age=age)




# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)
