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

# Data for category items
item_data = {
    'landwirtschaft': [
        {'name': 'Bauernhof Müller', 'image': 'pictures/oesterreich-kuehe-touristen-kuhunfaelle.jpg'},
        {'name': 'Bio-Gemüse Hof', 'image': 'pictures/aschau-ichiemgau.jpeg'},
        {'name': 'Milchviehbetrieb', 'image': 'pictures/nature.jpg'},
        {'name': 'Obstplantage', 'image': 'pictures/tour.jpeg'},
        {'name': 'Käserei Regional', 'image': 'pictures/keramik.jpeg'},
        {'name': 'Weinbau Aschau', 'image': 'pictures/1046-Schloss_HohenaschauTourist_Info_Aschau_i_Chiemgau_small_mSOQhmX.png'},
        {'name': 'Imkerei Chiemgau', 'image': 'pictures/bergsteigerdorf-sachrang.jpeg'},
        {'name': 'Fischzucht', 'image': 'pictures/bergsteigerdorf-sachrang.jpeg'},
        {'name': 'Landwirtschaftsverband', 'image': 'pictures/aschau-ichiemgau.jpeg'}
    ],
    'keramik': [
        {'name': 'Töpferei Schmidt', 'image': 'pictures/keramik.jpeg'},
        {'name': 'Keramik Atelier', 'image': 'pictures/aschau-ichiemgau.jpeg'},
        {'name': 'Porzellan Manufaktur', 'image': 'pictures/nature.jpg'},
        {'name': 'Steinzeug Werkstatt', 'image': 'pictures/tour.jpeg'},
        {'name': 'Kunstkeramik Galerie', 'image': 'pictures/oesterreich-kuehe-touristen-kuhunfaelle.jpg'},
        {'name': 'Tonarbeiten Chiemgau', 'image': 'pictures/1046-Schloss_HohenaschauTourist_Info_Aschau_i_Chiemgau_small_mSOQhmX.png'},
        {'name': 'Irdenware Produktion', 'image': 'pictures/bergsteigerdorf-sachrang.jpeg'},
        {'name': 'Majolika Atelier', 'image': 'pictures/bergsteigerdorf-sachrang.jpeg'},
        {'name': 'Keramik Schule', 'image': 'pictures/aschau-ichiemgau.jpeg'}
    ],
    'tourismus': [
        {'name': 'Chiemsee Bootsfahrt', 'image': 'pictures/tour.jpeg'},
        {'name': 'Wanderwege Alpen', 'image': 'pictures/aschau-ichiemgau.jpeg'},
        {'name': 'Schloss Hohenaschau', 'image': 'pictures/nature.jpg'},
        {'name': 'Kulturelle Festivals', 'image': 'pictures/keramik.jpeg'},
        {'name': 'Wintersport Aschau', 'image': 'pictures/oesterreich-kuehe-touristen-kuhunfaelle.jpg'},
        {'name': 'Radwege Region', 'image': 'pictures/1046-Schloss_HohenaschauTourist_Info_Aschau_i_Chiemgau_small_mSOQhmX.png'},
        {'name': 'Historische Stätten', 'image': 'pictures/bergsteigerdorf-sachrang.jpeg'},
        {'name': 'Naturpark Chiemgau', 'image': 'pictures/bergsteigerdorf-sachrang.jpeg'},
        {'name': 'Tourismus Info', 'image': 'pictures/aschau-ichiemgau.jpeg'}
    ],
    'natur': [
        {'name': 'Chiemsee Ufer', 'image': 'pictures/nature.jpg'},
        {'name': 'Alpenwanderwege', 'image': 'pictures/aschau-ichiemgau.jpeg'},
        {'name': 'Waldgebiete', 'image': 'pictures/tour.jpeg'},
        {'name': 'Vogelbeobachtung', 'image': 'pictures/keramik.jpeg'},
        {'name': 'Mountainbiking', 'image': 'pictures/oesterreich-kuehe-touristen-kuhunfaelle.jpg'},
        {'name': 'Angeln Spots', 'image': 'pictures/1046-Schloss_HohenaschauTourist_Info_Aschau_i_Chiemgau_small_mSOQhmX.png'},
        {'name': 'Naturpark Trails', 'image': 'pictures/bergsteigerdorf-sachrang.jpeg'},
        {'name': 'Seen und Teiche', 'image': 'pictures/bergsteigerdorf-sachrang.jpeg'},
        {'name': 'Umweltbildung', 'image': 'pictures/aschau-ichiemgau.jpeg'}
    ],
    'vereine': [
        {'name': 'Sportverein Aschau', 'image': 'pictures/aschau-ichiemgau.jpeg'},
        {'name': 'Kulturverein Chiemgau', 'image': 'pictures/nature.jpg'},
        {'name': 'Anglerverein', 'image': 'pictures/tour.jpeg'},
        {'name': 'Schützenverein', 'image': 'pictures/keramik.jpeg'},
        {'name': 'Feuerwehrverein', 'image': 'pictures/oesterreich-kuehe-touristen-kuhunfaelle.jpg'},
        {'name': 'Musikverein', 'image': 'pictures/1046-Schloss_HohenaschauTourist_Info_Aschau_i_Chiemgau_small_mSOQhmX.png'},
        {'name': 'Wanderclub', 'image': 'pictures/bergsteigerdorf-sachrang.jpeg'},
        {'name': 'Jugendgruppe', 'image': 'pictures/bergsteigerdorf-sachrang.jpeg'},
        {'name': 'Gemeinschaftsverein', 'image': 'pictures/aschau-ichiemgau.jpeg'}
    ],
    'news': [
        {'name': 'Festival Ankündigung', 'image': 'pictures/aschau-ichiemgau.jpeg'},
        {'name': 'Wirtschaftsupdate', 'image': 'pictures/nature.jpg'},
        {'name': 'Kulturelle Events', 'image': 'pictures/tour.jpeg'},
        {'name': 'Gemeinde Nachrichten', 'image': 'pictures/keramik.jpeg'},
        {'name': 'Sport Highlights', 'image': 'pictures/oesterreich-kuehe-touristen-kuhunfaelle.jpg'},
        {'name': 'Veranstaltungskalender', 'image': 'pictures/1046-Schloss_HohenaschauTourist_Info_Aschau_i_Chiemgau_small_mSOQhmX.png'},
        {'name': 'Lokale Entwicklungen', 'image': 'pictures/bergsteigerdorf-sachrang.jpeg'},
        {'name': 'Umwelt News', 'image': 'pictures/bergsteigerdorf-sachrang.jpeg'},
        {'name': 'Community Updates', 'image': 'pictures/aschau-ichiemgau.jpeg'}
    ]
}

@app.route('/<category>/info/<int:id>')
def info_page(category, id):
    if category not in item_data or id < 1 or id > len(item_data[category]):
        return 'Not Found', 404
    item = item_data[category][id - 1]
    lorem_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    return render_template('info.html', category=category, item=item, lorem_text=lorem_text)

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)