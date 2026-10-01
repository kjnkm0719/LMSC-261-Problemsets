song_duration_in_seconds = int(input("Enter the song duration in seconds: "))

minutes = song_duration_in_seconds // 60
seconds = song_duration_in_seconds % 60

print(f"The song duration is {minutes} minutes and {seconds} seconds.")