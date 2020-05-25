from flask import Flask, render_template
import os

PEOPLE_FOLDER = os.path.join('static')

app = Flask(__name__)
x = PEOPLE_FOLDER

@app.route('/')
@app.route('/index')
def show_index():
    full_filename = os.path.join(x, 'nisum.jpg')
    return render_template("index.html", user_image = full_filename)

if __name__ == '__main__':
    	app.run(debug=True, host='0.0.0.0', port=5002)
