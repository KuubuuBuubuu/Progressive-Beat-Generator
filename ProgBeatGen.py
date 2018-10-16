# -----Functionaliteiten----- #
# hij moet drie samples inladen, uit een lijst. deze zijn genaamd low mid en high;
# het moet via de console interactief zijn: de sample, maatsoort, en randomheid moet per object gekozen worden;
# De bpm moet ook random gekozen kunnen worden
# Voor regelmaat, moeten de eerste drie samples bestaan uit low high mid, elk een kwartnoot na elkaar;
# het console moet vragen of je wilt dat hij random een nieuw maatsoort elk maat kiest, of dat het een vaste waarde is;
# De random samplelengtes hebben een waarde van 0.125, 0.2, 0.25, 0.333, 0.5, of 0.75 kwartnoten;

# user input (bpm, samplekeuze, maatsoort, vraag voor vast of random maatsoort)
# bpm
# ritme genereren
# stop mogelijkheid
#
# beat afspelen
# midi exporteren
# locatie voor opslaan bepalen
# sample koppelen aan noot
#
# ritme omzetten naar midi
#
# -----stappenplan----- #
# 1. Defineer een class, met alle opties in __init__ die je wilt aanroepen (bpm, random/vast ritme [y/n], gegeven ritme, ritme>midi [y/n], lijst met samples, play, pause)
# 2. defineer zowel een functie die elke maat van maatsoort kan veranderen, evenals een functie met een aan te geven vaste maatsoort
#    definieer ook debug functies die print of je de juiste variabelen hebt.
# 3. vraag de gebruiker om alle variabelen.
# 4. Roep de juiste functie aan om de samples af te spelen met de juiste variabelen.
# 5. Debugging
# 5. Zorg voor een stop functie:
# ---------- Imports ----------#
import simpleaudio as sa
import time, os, fnmatch, sys, random
# ---------- Classes ---------- #
class userInput:
    def __init__(self, bpm, low, mid, high, choice, sig, exp):
        self.bpm = bpm
        self.low = low
        self.mid = mid
        self.high = high
        self.choice = choice
        self.sig = sig
        self.exp = exp

    def randomSeq(self):
        print() #placeholder
        # TODO: Make an array with notes


    def staticSeq(self):
        print() #placeholder

    def debug(self):
        print("The BPM is: %d" % (self.bpm))
        print("The low sample is: %s" % (self.low))
        print("The mid sample is: %s" % (self.mid))
        print("The high sample is: %s" % (self.high))
        if self.choice == True:
            print ("You've chosen to have a changing signature.")
        elif self.choice == False:
            print ("You've chosen to have a static signature.")
        print("The signature you've chosen is: %s/16" % (self.sig))
        print("the file will be exported as: %s" % (self.exp))

# ---------- Initialization ----------#
audioFiles = []
listOfFiles = os.listdir('./Samples')
pattern = "*.wav"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        audioFiles.append(entry)


# ---------- Variables ----------#
# set the bpm of the beat generator:
bpm = 120
while True:
    try:
        ask = input("The current BPM is %s beats per minute. would you like to change it? [Y/N] " %(bpm)).lower()
        if ask == "y":
            bpm = int(input("Please fill in what BPM you would like. "))
            break
        elif ask == "n":
            break
        else:
            print("That's not a yes or a no. Please use Y or N as your answer.")
            print()
    except:
        print() #safecheck

# list all files, choose which samples go to the 'low', 'mid', and 'high' sampleslots:
for file in audioFiles:
    print(file)
while True:
    try:
        low = input("What sample should the low slot be? ")
        if not low.endswith('.wav'):
            low+=".wav"
        lowPlay = sa.WaveObject.from_wave_file("Samples/"+low)
        break
    except FileNotFoundError:
        print("ERROR: There's no such file in the directory. please use one of the filenames from the list above.")
        print()
while True:
    try:
        mid = input("What sample should the mid slot be? ")
        if not mid.endswith('.wav'):
            mid+=".wav"
        midPlay = sa.WaveObject.from_wave_file("Samples/"+mid)
        break
    except FileNotFoundError:
        print("ERROR: There's no such file in the directory. please use one of the filenames from the list above.")
        print()
while True:
    try:
        high = input("What sample should the high slot be? ")
        if not high.endswith('.wav'):
            high+=".wav"
        highPlay = sa.WaveObject.from_wave_file("Samples/"+high)
        break
    except FileNotFoundError:
        print("ERROR: There's no such file in the directory. please use one of the filenames from the list above.")
        print()

while True:
    choice = input("do you want a static or a random signature? ").lower()
    if choice == "static":
        sig = input("Please fill in how many 16th notes you want as your signature.")
        break
    elif choice == "random":
        sig = random.randint(11, 32)
        break
    else:
        print("That's not a yes or a no. Please use Y or N as your answer.")
        print()

exp = "poep.midi"
p1 = userInput(bpm, low, mid, high, choice, sig, exp)



p1.debug()
