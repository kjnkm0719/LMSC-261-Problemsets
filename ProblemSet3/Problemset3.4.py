song_duration = float(input(" Enter the song duration "))

if song_duration < 2:
    print("Short song")

elif song_duration <= 4:
    print("Medium song")

else:
    print("Long song")
