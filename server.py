from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/landwirtschaft')
def landwirtschaft():
    return render_template('landwirtschaft.html')

@app.route('/keramik')
def keramik():
    return render_template('keramik.html')

@app.route('/tourismus')
def tourismus():
    return render_template('tourismus.html')

@app.route('/natur')
def natur():
    return render_template('natur.html')

@app.route('/vereine')
def vereine():
    return render_template('vereine.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)