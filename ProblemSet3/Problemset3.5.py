bpm = int(input(" Enter the BPM: "))
duration = int(input(" Enter the song duration in seconds: "))

beats_per_minute = bpm / 60

second = 1

while second <= duration:
    total_beats = beats_per_minute * second
    print(f"At second {second}, total beats: {total_beats}:")
    second += 1

    