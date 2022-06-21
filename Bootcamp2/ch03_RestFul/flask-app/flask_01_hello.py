from flask import Flask


# Se crea una instancia de la aplicacion
# El objeto que se utiliza para interactuar con el servidor web
app = Flask(__name__)


# Se utiliza el decorador app.route, que son los URLs de la aplicacion.
@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


# Se pueden pasar parametros en la URL.
@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello, {name}!</h1>"


# To use when run the module as a script
if __name__ == "__main__":
    app.run(debug=True)
