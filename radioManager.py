import requests
<<<<<<< HEAD:main.py
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from http.server import HTTPServer
import os

def auth():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read"))
=======
>>>>>>> parent of bf1a4b3 (merged python files):radioManager.py

# ---------------------------------------------------------------------------------
# query radio-browser.info for stations
# response {"name": "", "url": "", "server_type": ""}
# --------------------------------------------------------------------------------

def get_stations_country(country: str):
    response = requests.get(f"https://de1.api.radio-browser.info/json/stations/bycountry/{country}")
    return response.json()

def get_stations_intext(area: str):
    response = requests.get(f"https://de1.api.radio-browser.info/json/stations/byname/{area}", timeout=5)
    return response.json()

# dont use this, doesnt work right, use intext.
def get_stations_region(country: str, state: str):
    response = requests.get(f"https://de1.api.radio-browser.info/json/stations/bycountry/{country}/bystate/{state}")
    return response.json()

# ---------------------------------------------------------------------------------
# find stations for given locations
# ---------------------------------------------------------------------------------

def radio_lookup(country: str, region: str, city: str, relevance: int):
    stations_dict = {}

    if relevance > 0:
        city_stations = get_stations_intext(city)
        if city_stations:
            stations_dict.update({
                station['name']: {
                    "url": station['url_resolved'],
                    "relevance": 1,
                    "server_type": infer_server_type(station)
                }
                for station in city_stations
            })

    if relevance > 1:
        region_stations = get_stations_intext(region)
        if region_stations:
            stations_dict.update({
                station['name']: {
                    "url": station['url_resolved'],
                    "relevance": 2,
                    "server_type": infer_server_type(station)
                }
                for station in region_stations
            })

    if relevance > 1:
        country_stations = get_stations_country(country)
        if country_stations:
            stations_dict.update({
                station['name']: {
                    "url": station['url_resolved'],
                    "relevance": 3,
                    "server_type": infer_server_type(station)
                }
                for station in country_stations
            })

    if not stations_dict:
        print("No stations found.")
    return stations_dict


def infer_server_type(station):
    url = station['url_resolved']
    if 'shoutcast' in url or '/;stream' in url:
        return 'shoutcast'
    elif 'icecast' in url or 'status-json.xsl' in url:
        return 'icecast'
    else:
        return 'unknown'

# ---------------------------------------------------------------------------------
# testing scripts
# ---------------------------------------------------------------------------------

def print_stations(stations):
    for station in stations:
        print(f"Name : {station['name']}")

def test_metadata():
    for station in stations:
        stream_url = station['url']
        now_playing = get_metadata(stream_url)
        print(f"Now playing on {station['name']}: {now_playing}")

def get_regions():
    response = requests.get(f"https://de1.api.radio-browser.info/json/states/")
    regions = response.json()
    for r in regions:
        print(r['name'])
    
    return regions

def main():
    # stations = get_stations_intext("brighton")
    # for s in stations:
    #     print(s)

    stations = radio_lookup("Japan", "Kansai", "Kyoto", 3)
    for name, info in stations.items():
        print(f"Station: {name}, URL: {info['url']}, Relevance: {info['relevance']}, Server Type: {info['server_type']}")


<<<<<<< HEAD:main.py
main()
def get_city(location):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.reverse((location[0], location[1]), exactly_one=True, language="en")
    if location:
        address = location.raw.get("address", {})
        city = address.get("city") or address.get("town") or address.get("village")
        return city if city else "City/town/village not found"
    return "Location not found"

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

myDatabase = myClient["mydatabase"]

# id, access token (text and not null), refresh token (text and not null), token expires at (time stamp and not null), last accessed
usersCol = myDatabase["users"]

# id, city, country, longitude, latitude
infoCol = myDatabase["information"]

# id, ...
settingsCol = myDatabase["settings"]

# id, artists (Set), songs (Set)
spotifyCol = myDatabase["spotify"]

# id, friends (Set)
friendsCol = myDatabase["friends"]

# id, ...
radioCol = myDatabase["radio"]

# id, ...
requestCol = myDatabase["requests"]

def doesUserExist(userID, table):
    userExist = False
    if table == "users":
        userExist = usersCol.find({"userID": userID}) > 0
    elif table == "information":
        userExist = infoCol.find({"userID": userID}) > 0
    elif table == "settings":
        userExist = settingsCol.find({"userID": userID}) > 0
    elif table == "spotify":
        userExist = spotifyCol.find({"userID": userID}) > 0
    elif table == "friends":
        userExist = friendsCol.find({"userID": userID}) > 0
    elif table == "radio":
        userExist = radioCol.find({"userID": userID}) > 0
    elif table == "request":
        userExist = requestCol.find({"userID": userID}) > 0

    return userExist

def addUser(userID, accessToken, refreshToken, tokenExpire):
    if doesUserExist(userID, "users"):
        return
    else:
        user = {"userID" : userID, "accessToken" : accessToken, "refreshToken" : refreshToken, "tokenExpire": tokenExpire }
        usersCol.insert_one(user)

def addInfo(userID, city, country, longitude, latitude ):
    if doesUserExist(userID, "information"):
        return
    else:
        user = {"userID" : userID, "city" : city, "country" : country, "longitude": longitude, "latitude": latitude}
        infoCol.insert_one(user)

def addSettings(userID):
    # TODO : decide what fields the settings need
    pass

def addSpotify(userID, artists, songs):
    if doesUserExist(userID, "spotify"):
        return
    else:
        user = {"userID" : userID, "artists" : artists, "songs" : songs}
        spotifyCol.insert_one(user)

def addFriends(userID, friends):
    if doesUserExist(userID, "friends"):
        return
    else:
        user = {"userID" : userID, "friends" : friends}
        friendsCol.insert_one(user)

def addRadio(userID ):
    # TODO : decide what fields the radio table needs
    if doesUserExist(userID, "radio"):
        return
    else:
        user = {"userID" : userID}
        radioCol.insert_one(user)

def addRequests(userID):
    # TODO : decide what and how this works
    if doesUserExist(userID, "request"):
        return
    else:
        user = {"userID" : userID}
        requestCol.insert_one(user)



port = os.getenv('PORT',3000)
server = HTTP(('0,0,0,0',port),MyServer)
server.serve_forever()
=======
main()
>>>>>>> parent of bf1a4b3 (merged python files):radioManager.py
