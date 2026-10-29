class Track: 
    def __init__(self,name,volume,solo):
        self.name = name
        self.volume = volume
        self.solo = solo

    def runsolo(self): 
        self.solo = not self.solo



track01 = Track('track01', 0.6, False)
#track02 = Track('track02', 0.0, True)
#print(track01.name, track01.volume, track01.solo)
#print(track02.name, track02.volume, track02.solo)

for idx in range(3):
    print(track01.solo)
    track01.runsolo()
