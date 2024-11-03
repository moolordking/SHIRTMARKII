
from spotifyManager import get_artist_image

def getSongs(location):
	f = open("random_song_ids.txt", "r")
	data = f.read()
	f.close()
	songs = []
	for line in data.split("\n"):
		if line.split(", ")[0] == location:
			songs.append(line.split(", ")[1]+"@"+get_artist_image(line.split(", ")[1]))
	print(songs)
	return ":::".join(songs)
