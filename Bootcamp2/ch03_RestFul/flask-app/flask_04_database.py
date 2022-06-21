from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    new = False
    if request.method == 'POST' and 'name' in request.form:
        name = request.form['name']
        if mongo.db.customers.find_one({'name': name}) is None:
            # this is a new name, add it to the database
            mongo.db.customers.insert_one({'name': name})
            new = True
    return render_template('database.html', name=name, new=new)


if __name__ == '__main__':
    app.run(debug=True)