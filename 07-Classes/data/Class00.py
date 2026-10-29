# with open("lorem_ipsum.txt", "r") as file: 
#     content = file.read()
#     print(content)

setlist = ['Voodoo', 'Stairway to Heaven', 'Nublu', 'message in a bottle', 'love is everywhere','As']

with open("setlist.txt", "w") as file: 
    for ntrack,track in enumerate(setlist):
        file.write(f"{ntrack+1} {track}\n")
        #print(f"{ntrack + 1} {track}\n", end="")
