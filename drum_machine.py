from midiutil import MIDIFile
import random

midiFile = MIDIFile (1)
midiFile.addTempo(0, 0, 120)

def randomNote():
    random.seed()
    #It will write midi notes starting on C3 to C4 
    drums = [60, 62, 64, 65, 67, 69, 71, 72]
    drums = int(random.choice(drums))
    return drums

def randomStart():
    random.seed()
    ## It will give you 2 bars 
    min = 0
    max = 7
    random_value = random.random()
    tiempo = int (min + random_value * (max - min))
    return tiempo

def randomVelocity():
    random.seed()
    min = 1
    max = 127
    random_value = random.random()
    valor = int (min + random_value * (max - min))
    return valor

triggers = [int(x) for x in input("Enter as many 1s as you want to create midi notes separate them with spaces:\n").split()]

for x in triggers:
    if x == 1:
        note = randomNote()
        start = randomStart()
        vel = randomVelocity()
        print (x, note, start, vel)
        midiFile.addNote(0, 0, note, start, 16/16.0, vel)
    elif x == 0:
        note = 0
        vel = 0
        print (x, note, vel)
    else: 
        print (x, "This wasn't a 1 or 0")

with open ("drums.mid", "wb") as myOutputMIDIClip: 
     midiFile.writeFile(myOutputMIDIClip)
print("sheeeeesh")
