from midiutil import MIDIFile
import numpy as np
import random

midiFile = MIDIFile(1)

midinotesmajor = {"C":[0, 2, 4, 5, 7, 9, 11, 12], "G": [7, 9, 11, 12, 14, 16, 18, 19],"D": [2, 4, 6, 7, 9, 11, 13, 14], "A": [9, 11, 13, 14, 16, 18, 20, 21], "E": [4, 6, 8, 9, 11, 13, 15, 16], "B":[11, 13, 15, 16, 18, 20, 22, 23],"Gb": [6, 8, 10, 11, 13, 15, 17, 18],"Db": [1, 3, 5, 6, 8, 10, 11, 12, 13],"Ab":[8, 10, 12, 13, 15, 17, 19, 20], "Eb": [3, 5, 7, 8, 10, 12, 14, 15],"Bb": [10, 12, 14, 15, 17, 19, 21, 22], "F":[5, 7, 9, 10, 12, 14, 16, 17] }

midinotesminor = {"Am":[9, 11, 12, 14, 16, 17, 19, 21,], "Em":[4, 6, 7, 9, 11, 12, 14, 16], "Bm": [11, 13, 14, 16, 18, 19, 21, 23], "F#m": [6, 8, 9, 11, 13, 14, 16, 18], "C#m": [1, 3 ,4, 6, 8, 9, 11, 13], "G#m":[8, 10, 11, 13, 15, 16, 18, 20],"Ebm":[3, 5, 6, 8, 10, 11, 12, 14], "Bbm": [10, 12, 13, 15, 17, 18, 20, 22], "Fm": [5, 7, 8, 10, 12, 13, 15, 17], "Cm": [1, 3, 4, 6, 8, 9, 11, 13], "Gm": [7, 9, 10, 12, 14, 15, 17, 19],"Dm": [2, 4, 5, 7, 9, 10, 12, 14] }

duration = {"1": 64/16.0, "2":48/16.0, "3": 32/16.0, "4": 24/16.0, "5": 16/16.0, "6": 12/16.0, "7": 8/16.0, "8": 6/16.0, "9": 4/16.0 }

midiNotes = {           "C-1": 0,  "C#-1": 1, "D-1": 2, "D#-1": 3, "E-1":4, "F-1": 5, "F#-1": 6,
                        "G-1": 7, "G#-1": 8, "A-1": 9, "A#-1": 10, "B-1": 11,"C0": 12, "C#0": 13,
                        "D0": 14, "D#0": 15, "E0": 16, "F0": 17, "F#0": 18,  "G0": 19,
                        "G#0": 20, "A0": 21, "A#0": 22, "B0": 23, "C1": 24, "C#1": 25 , "D1": 26,
                        "D#1": 27, "E1": 28, "F1": 29,  "F#1": 30, "G1": 31, "G#1": 32, "A1": 33, "A#1": 34,
                        "B1": 35, "C2": 36, "C#2": 37,  "D2": 38,  "D#2": 39, "E2": 40, "F2": 41,
                        "F#2": 42, "G2":43, "G#2": 44,  "A2": 45, "A#2": 46, "B2": 47, "C3": 48,
                        "C#3": 49, "D3":50,  "D#3": 51, "E3": 52 ,"F3": 53, "F#3": 54, "G3": 55,
                        "G#3": 56 ,"A3": 57, "A#3": 58, "B3":59, "C4": 60, "C#4": 61, "D4":62,
                        "D#4": 63, "E4": 64, "F4": 65, "F#4": 66, "G4": 67, "G#4": 68, "A4": 69,
                        "A#4": 70, "B4": 71, "C5": 72, "C#5": 73, "D5": 74, "D#5": 75, "E5": 76,
                        "F5": 77, "F#5": 78, "G5": 79, "G#5": 80, "A5": 81, "A#5": 82, "B5": 83,
                        "C6": 84, "C#6": 85, "D6": 86, "D#6": 87, "E6": 88, "F6": 89, "F#6": 90,
                        "G6":91, "G#6": 92, "A6": 93, "A#6": 94, "B6": 95, "C7": 96, "C#7": 97,
                        "D7": 98, "D#7": 99, "E7": 100, "F7": 101, "F#7": 102, "G7": 103, "G#7": 104,
                        "A7": 105,"A#7": 106, "B7": 107, "C8": 108, "C#8": 109, "D8": 110,
                        "D#8": 111,"E8": 112, "F8": 113, "F#8": 114, "G8": 115, "G#8": 116,
                        "A8": 117, "A#8": 118, "B8": 119, "C9": 120, "C#9": 121, "D9": 122,
                        "D#9": 123, "E9": 124, "F9": 125, "F#9": 126, "G9": 127
                        }

                        
T = True
while T:
    majororminor = int(input("Select:\n\tMajor: 1\n\tMinor: 2\n"))
    if majororminor not in [1, 2]:
        print("Wrong option, try again.")
    else:
        T = False

if majororminor == 1:
    tonality = input("Select tonality Major:\nC\nG\nD\nA\nE\nB\nGb\nDb\nAb\nEb\nBb\nF\n")
    listran = midinotesmajor[tonality]
else:
    tonality = input("Select tonality Minor:\nAm\nEm\nBm\nF#m\nC#m\nG#m\nEbm\nBbm\nFm\nCm\nGm\nDm\n")
    listran = midinotesminor[tonality]

bpm = int (input("Select bpm in numbers\n"))

midiFile.addTempo (0, 0, bpm)

noc =  int (input ("Select how many cycles:\n"))

start = 0
i = 0 
arrayf=[]

dur = ((input("Select rate:\n Whole note : 1\n dotted white note: 2\n white note: 3\n dotted quarter note: 4\n quarter note: 5\n dotted eight note: 6\n eight note: 7\n dotted sixteenth note: 8\n sixteenth note: 9\n")))

move = int( input("Select arpeggiator movement:\n Up and Down: 1\n Up: 2\n Down: 3\n Random: 4\n"))

for m in range(noc): 
    octave = int(input("Select octave for the fundamental note the arpeggio:\nfrom -1 to 9\n"))
    fundamental = int(input("Select fundamental note:\n First: 1\n Second: 2\n Third: 3\n Fourth: 4\n Fifth: 5\n Sixth 6\n Seventh: 7\n"))
    note = listran [fundamental - 1] + (12 * (octave + 1))
    durate =duration[dur] 
    rate = durate
    i = i
    print("Your note is: {}".format(list(midiNotes.keys())[list(midiNotes.values()).index(note)]))
    def updown(note, c = 0):
        return list(midiNotes.keys())[list(midiNotes.values()).index(note + c)]
    def up(note, c = 0):
        return list(midiNotes.keys())[list(midiNotes.values()).index(note + c)]
    def down (note, c = 0):
        return list(midiNotes.keys())[list(midiNotes.values()).index(note + c)]
    def originalnote (note):
        return list(midiNotes.keys())[list(midiNotes.values()).index(note)]
    def plox (note, pls = 0):
        random.seed()
        pls = [0, 4, 7, 12, 16]
        pls = random.choice(pls)
        return list(midiNotes.keys())[list(midiNotes.values()).index(note + pls)]
    if move == 1:
        updownnotes = ((midiNotes[(updown(note))]),(midiNotes[(updown(note, 4))]), midiNotes[(updown(note, 7))], midiNotes[(updown(note, 12))],midiNotes[(updown(note, 16))], midiNotes[(updown(note, 12))],midiNotes[(updown(note, 7))],midiNotes[ (updown(note, 4))])
        array = np.asarray(updownnotes)
    elif move == 2:
        upnotes = ((midiNotes[(up(note))]),(midiNotes[(up(note, 4))]), midiNotes[(up(note, 7))], midiNotes[(up(note, 12))],midiNotes[(up(note, 16))])
        array = np.asarray(upnotes)
    elif move == 3: 
        downnotes = ((midiNotes[(down (note))]),(midiNotes[(down(note, -5))]), midiNotes[(down(note, -8))], midiNotes[(down(note, -12))],midiNotes[(down(note, -16))])
        array = np.asarray(downnotes)
    elif move == 4:
        randomnotes = ((midiNotes[(originalnote(note))]),(midiNotes[(plox(note))]),(midiNotes[(plox(note))]),(midiNotes[(plox(note))]),(midiNotes[(plox(note))]),(midiNotes[(plox(note))]),(midiNotes[(plox(note))]),(midiNotes[(plox(note))]),(midiNotes[(plox(note))]))
        array = np.asarray(randomnotes)
    arrayf = np.concatenate([arrayf, array])

print (arrayf)
    
for x in arrayf:
    midiFile.addNote(0, 0, int (arrayf[i]), start, rate, 100)
    i = i+1
    start = start+rate

with open ("ARP.mid", "wb") as myOutputMIDIClip: 
     midiFile.writeFile(myOutputMIDIClip)
print("sheeeeesh")
