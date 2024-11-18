from flask import Flask, render_template

app = Flask(__name__)

posts = [{'author': 'Jason Jang',
          'title': 'Aafari',
          'content': 'The Enfant Terrible',
          'date_posted': '22nd Nov, 2024'
          }
    ,
         {'author': 'Z',
          'title': 'Draw, Damn it',
          'content': 'An artistic monologue',
          'date_posted': '13th Nov, 2024'
          }]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', ti)


if __name__ == '__main__':
    app.run(debug=True)
