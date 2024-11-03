from gc import collect

import pymongo

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

# songID, name, artist/s, frequency
songsCol = myDatabase["songs"]

cascade = ["user", "info", "settings", "spotify", "friends", "radio", "requests"]

def doesUserExist(userID, table):
    userExist = False
    if table == "users":
        userExist = (usersCol.find_one({"userID": userID})) is not None
    elif table == "information":
        userExist = (infoCol.find_one({"userID": userID})) is not None
    elif table == "settings":
        userExist = (settingsCol.find_one({"userID": userID})) is not None
    elif table == "spotify":
        userExist = (spotifyCol.find_one({"userID": userID})) is not None
    elif table == "friends":
        userExist = (friendsCol.find_one({"userID": userID})) is not None
    elif table == "request":
        userExist = (requestCol.find_one({"userID": userID})) is not None

    return userExist

def doesSongExist(songID):
    return (songsCol.find_one({"songID": songID})) is not None

def addSong(songID, name, artists):
    if (doesSongExist(songID)):
        songsCol.update_one({"songID" : songID }, {"$inc" : {"frequency" : 1}})
    else:
        song = {"songID": songID, "name": name, "artists": artists, "frequency": 1}
        songsCol.insert_one(song)

def addRadio():
    # TODO : Not sure what is being added to radio just yet
    pass

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

# spotify code, latitude and longitude
def addRequests(userID):
    # TODO : decide what and how this works
    if doesUserExist(userID, "request"):
        return
    else:
        user = {"userID" : userID}
        requestCol.insert_one(user)

# Cascade delete
def removeUser(userID):
    query = {"userID": userID}
    if (doesUserExist(userID, "users")):
        usersCol.delete_one(query)

    if (doesUserExist(userID, "information")):
        infoCol.delete_one(query)

    if (doesUserExist(userID, "settings")):
        settingsCol.delete_one(query)

    if (doesUserExist(userID, "spotify")):
        spotifyCol.delete_one(query)

    if (doesUserExist(userID, "friends")):
        friendsCol.delete_one(query)

def removeSong(songID):
    if (doesSongExist(songID)):
        songsCol.delete_one({"songID" : songID})
    else:
        print("Song does not exist")

def updateField(userID, table, field, value):
    if table == "users":
        usersCol.update_one({"userID" : userID}, {"$set": {field: value}})
    if table == "information":
        infoCol.update_one({"userID" : userID}, {"$set": {field: value}})
    if table == "settings":
        settingsCol.update_one({"userID" : userID}, {"$set": {field: value}})
    if table == "spotify":
        spotifyCol.update_one({"userID" : userID}, {"$set": {field: value}})
    if table == "friends":
        friendsCol.update_one({"userID" : userID}, {"$set": {field: value}})

# prints all each record of each table
def debug():
    cursor = usersCol.find()
    print("userCol:")
    for user in cursor:
        print(user)

    print("informationCol:")
    cursor = infoCol.find()
    for user in cursor:
        print(user)

    print("spotifyCol:")
    cursor = settingsCol.find()
    for user in cursor:
        print(user)

    print("friendsCol:")
    cursor = friendsCol.find()
    for user in cursor:
        print(user)

    print("radioCol:")
    cursor = radioCol.find()
    for user in cursor:
        print(user)

    print("requestCol:")
    cursor = requestCol.find()
    for user in cursor:
        print(user)

    print("songsCol:")
    cursor = songsCol.find()
    for user in cursor:
        print(user)

debug()