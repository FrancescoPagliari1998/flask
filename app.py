from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    bottoni = {
        'b1': 'movies',
        'b2': 'music',
        'b3': 'book',
        'b4': 'Videogiochi'
    }
    return render_template('home_bs.html', titolo='Benvenuti nel nostro sito'.upper(), bottoni=bottoni)

@app.route('/data')
def data():
    
    return 'Ciao, data!'

@app.route('/movies')
def movies():
    with open('film.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return render_template('movies.html', data=data)

@app.route('/book')
def book():
    return render_template('book.html')


@app.route('/music')
def music():
    return render_template('music.html')


if __name__ == '__main__':
    app.run(debug=True)