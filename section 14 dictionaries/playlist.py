##134 playlist spotify
playlist = {"title":"patagonia bus",
 "author" : "subham deb",
 "songs" : [
     {"title": "song1", "artist": ["blue"],"duration" : 2.5},
     {"title": "song1", "artist": ["djcat","kitty"],"duration" : 3.5},
 ]
}

total_length = 0
for song in playlist["songs"] : 
    print(song["duration"])
    total_length += song["duration"]

print(total_length)
print(playlist["author"])