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
            notes16th = [2, 2, 2]
            while True:
                if sum(notes16th) > sig:
                    notes16th.pop()
                    if sum(notes16th) < sig -5:
                        notes16th.append(random.randint(1, 4))
                    break
                else:
                    notes16th.append(random.randint(1, 4))
            print(notes16th, "is the note durations")
            durationsToTimestamps16th(notes16th)
            realTimeStamps(timestamps16th, bpm)
            # retrieve first timestamp
            # NOTE: pop(0) returns and removes the element at index 0
            timestamp = timestamps.pop(0)
            # retrieve the startime: current time
            startTime = time.time()
            keepPlaying = True
            samNum = 0
            # play the sequence
            while keepPlaying:
                # retrieve current time
                currentTime = time.time()
                # check if the timestamp's time is passed
                if(currentTime - startTime >= timestamp):
                    # play sample
                    if samNum == 0:
                        lowPlay.play()
                        samNum=samNum+1
                        timestamp = timestamps.pop(0)
                    elif samNum ==1:
                        highPlay.play()
                        samNum=samNum+1
                        timestamp = timestamps.pop(0)
                    elif samNum == 2:
                        midPlay.play()
                        samNum=samNum+1
                        timestamp = timestamps.pop(0)
                    else:
                        samples[random.randint(0,1)].play()
                        print("playing sample at %s seconds." %(currentTime-startTime))

                    # if there are timestamps left in the timestamps list
                        if timestamps:
                        # retrieve the next timestamp
                            timestamp = timestamps.pop(0)
                        else:

                            # list is empty, stop loop
                            keepPlaying = False
                else:
                    # wait for a very short moment
                        time.sleep(0.001)


    def staticSeq(self):
        notes16th = [2, 2, 2]

        samNum = 0
        while True:
            if sum(notes16th) > sig:
                notes16th.pop()
                if sum(notes16th) < sig -5:
                    notes16th.append(random.randint(1, 4))
                break
            else:
                notes16th.append(random.randint(2, 4))
        print(notes16th, "is the note durations")
        durationsToTimestamps16th(notes16th)
        realTimeStamps(timestamps16th, bpm)
        # retrieve first timestamp
        # NOTE: pop(0) returns and removes the element at index 0
        timestamp = timestamps.pop(0)
        # retrieve the startime: current time
        startTime = time.time()
        keepPlaying = True
        # play the sequence
        while keepPlaying:
            # retrieve current time
            currentTime = time.time()
            # check if the timestamp's time is passed
            if(currentTime - startTime >= timestamp):
                # play sample
                if samNum == 0:
                    lowPlay.play()
                    print("playing sample at %s seconds." %(round((currentTime-startTime), 2)))
                    samNum=samNum+1
                    timestamp = timestamps.pop(0)
                elif samNum ==1:
                    highPlay.play()
                    print("playing sample at %s seconds." %(round((currentTime-startTime), 2)))
                    samNum=samNum+1
                    timestamp = timestamps.pop(0)
                elif samNum == 2:
                    midPlay.play()
                    print("playing sample at %s seconds." %(round((currentTime-startTime), 2)))
                    samNum=samNum+1
                    timestamp = timestamps.pop(0)
                else:
                    samples[random.randint(0,1)].play()
                    print("playing sample at %s seconds." %(round((currentTime-startTime), 2)))

                # if there are timestamps left in the timestamps list
                    if timestamps:
                    # retrieve the next timestamp
                        timestamp = timestamps.pop(0)
                    else:

                        # list is empty, stop loop
                        samples[random.randint(0,1)].play()
                        keepPlaying = False
            else:
                # wait for a very short moment
                    time.sleep(0.001)
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

# define durationsToTimestamps16th
def durationsToTimestamps16th(l1):
    for value in l1:
        if timestamps16th==[]:
            timestamps16th.append(0)
        else:
            timestamps16th.append(max(timestamps16th) + value)
    print(timestamps16th, "is the timestamps in 16th.")

# define timestampsin16th to timestampsintime
def realTimeStamps(l1, int):
    for timestamp in l1:
        timestamps.append(timestamp * ((60 / int) / 4.0))
    print(timestamps, "is the timestamps in real time.")

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
        lowPlay.play()
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
        midPlay.play()
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
        highPlay.play()
        break
    except FileNotFoundError:
        print("ERROR: There's no such file in the directory. please use one of the filenames from the list above.")
        print()

while True:
    choice = input("do you want a static or a random signature? ").lower()
    if choice == "static":
        sig = int(input("Please fill in how many 16th notes you want as your signature."))
        break
    elif choice == "random":
        sig = random.randint(18, 32)
        break
    else:
        print("That's not a yes or a no. Please use Y or N as your answer.")
        print()
timestamps = []                                                                                 # create a list to hold the timestamps
timestamps16th = []                                                                             # create a list for 16th notes with a starting position
fullTimeStamps = []
samples = [lowPlay, midPlay, highPlay]
exp = "poep.mid"
rep = input("How many times do you want your sequence to be repeated? ")
p1 = userInput(bpm, low, mid, high, choice, sig, exp)

# ---------- Player starts ----------#
if p1.choice == 'random':
        p1.randomSeq()
else:
    p1.staticSeq()
