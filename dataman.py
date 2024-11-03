# lat, long, trackid, artistimg
# store in csv 
# query for lat long, -> translate to location, search for corresponding in csv
import csv
import location

def add_entry(lat, long, track_id, artist_img):
    with open("data.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([lat, long, track_id, artist_img])

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

add_entry(54.774700874515986, -1.589109503156958, "123456", "photo_of_me.png")

print(get_local_songs(54.77499791269901, -1.5814705719504962))