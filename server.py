from flask import Flask, render_template, request

import location as locator

import spotifyManager as sManager

import sampleData as sData

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('spotifyAuth.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('data')
    print(data)
    #spotify_code:::latitude:::longitude:::home_addrs
    data_elements = data.split(":::")
    print(f">>>DATA>>> {data_elements[0]}")
    # the city
    location = locator.get_city([data_elements[1], data_elements[2]])

    # sManager.add_top_songs(data_elements[0], data_elements[1], data_elements[2])

    # 10 songs from database
    
    # sManager.check_auth(sManager.auth(data_elements[0]))
    
    # songs = sManager.get_top_songs(data_elements[0]) 
    songs = sData.getSongs(location);

    return f"{location}:::{songs}"

if __name__ == '__main__':
    app.run(host='localhost',debug=True)
