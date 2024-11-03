import requests

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
