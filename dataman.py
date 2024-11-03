# lat, long, trackid, artistimg
# store in csv 
# query for lat long, -> translate to location, search for corresponding in csv
import csv
import location

def add_entry(lat, long, track_id):
    with open('random_song_ids.txt', 'a') as f:
        f.write(f"{location.get_city([lat, long])}, {track_id}\n")

def get_local_songs(lat, long):
    songs = []
    target_city = location.get_city([lat, long])
    print(f"Target City: {target_city}")

    with open("data.csv", mode='r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            found_city = location.get_city([row[0], row[1]])
            print(f"Found City: {found_city}")
            if found_city == target_city:
                print("match")
                songs.append(row)

    return songs