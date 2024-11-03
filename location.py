from geopy.geocoders import Nominatim

def get_city(location):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.reverse((location[0], location[1]), exactly_one=True, language="en")
    if location:
        address = location.raw.get("address", {})
        city = address.get("city") or address.get("town") or address.get("village")
        return city if city else "City/town/village not found"
    return "Location not found"
