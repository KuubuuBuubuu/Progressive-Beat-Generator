# ---------- Imports ---------- #
import simpleaudio as sa
import time, os, fnmatch, sys, random
from midiutil import MIDIFile
from pynput import keyboard
import threading


# ---------- Classes ---------- #
class userInput:
    def __init__(self, bpm, low, mid, high, choice, sig, exp, keepPlaying):
        self.bpm = bpm
        self.low = low
        self.mid = mid
        self.high = high
        self.choice = choice
        self.sig = sig
        self.exp = exp
        self.keepPlaying = keepPlaying

    def randomSeq(self):                                                                                                # Sequencer with a changing signature every measure.
        # local variables
        global timestampsBuffer
        sig = random.randint(9,19)                                                                                      # Changes signature to something between 9/16 en 19/16.
        timestamps = []                                                                                                 # Creates a list with for notes in actual time.
        timestamps16th = []                                                                                             # Create a list for 16th notes with a starting position.
        sigSum = 0
        sigSum = sigSum + sig                                                                                           # Adds variable that checks how many 16ths have been played in total.
        samNum = 0                                                                                                      # Adds variable that lets you choose what sample should be used for whatever sample (currently used for 1st, 2nd, and 3rd sample in sequence).

        # Create arrays with all notes for that measure.
        notes16th = [2, 2, 2]                                                                                           # Starting values that stay the same every measure, for consistency.
        while True:                                                                                                     # While loop to keep adding notes until your note array fills the whole signature.
            if sum(notes16th) > sig:
                notes16th.pop()
                break
            else:
                notes16th.append(random.randint(1, 2))
        for value in notes16th:                                                                                         # Fills timestamps array [in 16th notes]
            if timestamps16th==[]:
                timestamps16th.append(0)
            else:
                timestamps16th.append(max(timestamps16th) + value)
        timestampsBuffer = timestamps16th                                                                               # Adds buffer so current timestamps are ready to be added together before getting popped.
        for timestamp in timestamps16th:
            timestamps.append(timestamp * ((60 / bpm) / 4.0))                                                           # Fills timestamps array [in actual time]

        # Start sequence
        timestamp = timestamps.pop(0)                                                                                   # Gets rid of 1st timestamp
        startTime = time.time()                                                                                         # Start time counting.
        while keepPlaying==True:                                                                                        # Whileloop to keep checking every ms if a note should be playing.
            currentTime = time.time()
            if(currentTime - startTime >= timestamp):
                if samNum == 0:                                                                                         # 1st note is 'low'
                    lowPlay.play()
                    samNum=samNum+1
                    noteValues.append(32)
                    timestamp = timestamps.pop(0)
                elif samNum ==1:                                                                                        # 2nd note is 'high'
                    highPlay.play()
                    samNum=samNum+1
                    noteValues.append(35)
                    timestamp = timestamps.pop(0)
                elif samNum == 2:                                                                                       # 3rd note is 'mid'
                    midPlay.play()
                    samNum=samNum+1
                    noteValues.append(34)
                    timestamp = timestamps.pop(0)
                else:
                    SamplePlay()                                                                                        # Other notes are random.
                    if timestamps:                                                                                      # Keeps removing timestamps until all timestamps are gone.
                        timestamp = timestamps.pop(0)
                    else:                                                                                               # When there are no more timestamps, keeps filling the same variables via the same algorithm.
                        time.sleep(((60 / bpm) / 4.0))                                                                  # NOTE: Adds 1/16th note of waiting.
                        sig = random.randint(9,19)
                        notes16th = [2, 2, 2]
                        timestamps16th=[]                                                                               # empties the timestamps, ready to be filled again
                        timestamps=[]
                        while True:
                            if sum(notes16th) > sig:
                                notes16th.pop()
                                break
                            else:
                                notes16th.append(random.randint(1, 2))
                            if sum(notes16th) == sig:
                                notes16th.pop()
                                break
                        for value in notes16th:
                            if timestamps16th==[]:
                                timestamps16th.append(0)
                            else:
                                timestamps16th.append(max(timestamps16th) + value)
                        for x in timestamps16th:
                            timestampsBuffer.append(x + sigSum)
                        for timestamp in timestamps16th:
                            timestamps.append(timestamp * ((60 / bpm) / 4.0))
                        timestamp = timestamps.pop(0)
                        startTime = time.time()
                        samNum = 0
                        sigSum = sigSum + sig
            else:
                time.sleep(0.001)                                                                                       # wait for a very short moment

    def staticSeq(self):                                                                                                # Sequencer with a changing signature every measure.
                # local variables
                global timestampsBuffer
                timestamps = []                                                                                                 # Creates a list with for notes in actual time.
                timestamps16th = []                                                                                             # Create a list for 16th notes with a starting position.
                sigSum = 0
                sigSum = sigSum + sig                                                                                           # Adds variable that checks how many 16ths have been played in total.
                samNum = 0                                                                                                      # Adds variable that lets you choose what sample should be used for whatever sample (currently used for 1st, 2nd, and 3rd sample in sequence).

                # Create arrays with all notes for that measure.
                notes16th = [2, 2, 2]                                                                                           # Starting values that stay the same every measure, for consistency.
                while True:                                                                                                     # While loop to keep adding notes until your note array fills the whole signature.
                    if sum(notes16th) > sig:
                        notes16th.pop()
                        break
                    else:
                        notes16th.append(random.randint(1, 2))
                for value in notes16th:                                                                                         # Fills timestamps array [in 16th notes]
                    if timestamps16th==[]:
                        timestamps16th.append(0)
                    else:
                        timestamps16th.append(max(timestamps16th) + value)
                timestampsBuffer = timestamps16th                                                                               # Adds buffer so current timestamps are ready to be added together before getting popped.
                for timestamp in timestamps16th:
                    timestamps.append(timestamp * ((60 / bpm) / 4.0))                                                           # Fills timestamps array [in actual time]

                # Start sequence
                timestamp = timestamps.pop(0)                                                                                   # Gets rid of 1st timestamp
                startTime = time.time()                                                                                         # Start time counting.
                while keepPlaying==True:                                                                                        # Whileloop to keep checking every ms if a note should be playing.
                    currentTime = time.time()
                    if(currentTime - startTime >= timestamp):
                        if samNum == 0:                                                                                         # 1st note is 'low'
                            lowPlay.play()
                            samNum=samNum+1
                            noteValues.append(32)
                            timestamp = timestamps.pop(0)
                        elif samNum ==1:                                                                                        # 2nd note is 'high'
                            highPlay.play()
                            samNum=samNum+1
                            noteValues.append(35)
                            timestamp = timestamps.pop(0)
                        elif samNum == 2:                                                                                       # 3rd note is 'mid'
                            midPlay.play()
                            samNum=samNum+1
                            noteValues.append(34)
                            timestamp = timestamps.pop(0)
                        else:
                            SamplePlay()                                                                                        # Other notes are random.
                            if timestamps:                                                                                      # Keeps removing timestamps until all timestamps are gone.
                                timestamp = timestamps.pop(0)
                            else:                                                                                               # When there are no more timestamps, keeps filling the same variables via the same algorithm.
                                time.sleep(((60 / bpm) / 4.0))                                                                  # NOTE: Adds 1/16th note of waiting.
                                notes16th = [2, 2, 2]
                                timestamps16th=[]                                                                               # empties the timestamps, ready to be filled again
                                timestamps=[]
                                while True:
                                    if sum(notes16th) > sig:
                                        notes16th.pop()
                                        break
                                    else:
                                        notes16th.append(random.randint(1, 2))
                                    if sum(notes16th) == sig:
                                        notes16th.pop()
                                        break
                                for value in notes16th:
                                    if timestamps16th==[]:
                                        timestamps16th.append(0)
                                    else:
                                        timestamps16th.append(max(timestamps16th) + value)
                                for x in timestamps16th:
                                    timestampsBuffer.append(x + sigSum)
                                for timestamp in timestamps16th:
                                    timestamps.append(timestamp * ((60 / bpm) / 4.0))
                                timestamp = timestamps.pop(0)
                                startTime = time.time()
                                samNum = 0
                                sigSum = sigSum + sig
                    else:
                        time.sleep(0.001)                                                                                       # wait for a very short moment


# ---------- Initialization ---------- #
# list of audiofiles
audioFiles = []
listOfFiles = os.listdir('./Samples')
pattern = "*.wav"
pause = False
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        audioFiles.append(entry)

# General
bpm = 120
keepPlaying = True                                                                                                      # check if sequencer should loop

# MIDI Information
mf = MIDIFile(1)
track = 0
channel = 0
pitch = 0
PitchOut = 32 + pitch
volume = 127
noteValues = []                                                                                                         # Array of all note MIDI Values in the complete sequence.


# ---------- Definitions ---------- #
def thread1 ():                                                                                                         # data for thread 1
  if p1.choice == 'random':
      p1.randomSeq()
  elif p1.choice == 'static':
      p1.staticSeq()

def thread2 ():                                                                                                         # data for thread 2
    with keyboard.Listener(
          on_press=on_press,
          on_release=on_release) as listener:
      listener.join()

def on_press(key):                                                                                                      # function that when a key is pressed, stops sequencer, makes midi, and exits.
    try:
        global keepPlaying
        keepPlaying = False
        for pos, val in zip(timestampsBuffer, noteValues):
            mf.addNote(track, channel, val, pos/4.0, 0.125, volume)
        with open(exp, 'wb') as outf:
            mf.writeFile(outf)
        print("The sequencer has been stopped. Your midi file has been created. Have a nice day! :)")
        time.sleep(2)
        return False
    except AttributeError:
        print()

def on_release(key):                                                                                                    # function that shows what happens when a key is released
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def SamplePlay():                                                                                                       # function that randomly chooses what sample to play at that given moment.
    pitch = random.randint(0,2)
    PitchOut = 32 + pitch
    if pitch == 0:
        lowPlay.play()
        noteValues.append(32)
    elif pitch == 1:
        midPlay.play()
        noteValues.append(34)
    elif pitch == 2:
        highPlay.play()
        noteValues.append(35)


# ---------- userInput Variables ----------#
while True:                                                                                                             # Asks the user if they want a different tempo than 120 bpm.
    try:
        ask = input("The current BPM is %s beats per minute. would you like to change it? [Y/N] " %(bpm)).lower()
        if ask == "y":
            while True:
                try:
                    bpm = int(input("Please fill in what BPM you would like. "))
                    break
                except ValueError:
                    print("ERROR: That's no value, silly goose.")
                    print()
            break
        elif ask == "n":
            break
        else:
            print("ERROR: Please answer with Y or N")
            print()
    except:
        print()

print()
print("----- Audio Files -----")
for file in audioFiles:
    print(file)
print("-----------------------")
print()
while True:                                                                                                             # Asks the user what they want for their 'low' sampleslot.
    try:
        low = input("What sample should the low slot be? ")
        if not low.endswith('.wav'):
            low += ".wav"
        lowPlay = sa.WaveObject.from_wave_file("Samples/"+low)
        lowPlay.play()
        break
    except FileNotFoundError:
        print("ERROR: There's no such file in the directory. please use one of the filenames from the list above.")
        print()

while True:                                                                                                             # Asks the user what they want for their 'mid' sampleslot.
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

while True:                                                                                                             # Asks the user what they want for their 'high' sampleslot.
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

while True:                                                                                                             # Asks the user for either a static or a changing signature.
    choice = input("do you want a static or a random signature? ").lower()
    if choice == "static":
        sig = int(input("Please fill in how many 16th notes you want as your signature. "))
        break
    elif choice == "random":
        sig = random.randint(9,19)
        break
    else:
        print("ERROR: Please choose either a static or a random signature.")
        print()

while True:                                                                                                             # Asks the user what to name their exported MIDI-file.
    try:
        exp = input("How would you like to name the sequence export that will be generated?")
        if not exp.endswith('.mid'):
            exp += ".mid"
        break
    except:
        print("That's not a viable name. Please name it something differently.")
        print()

samples = [lowPlay, midPlay, highPlay]                                                                                  # adds an array with playable sample variables.
p1 = userInput(bpm, low, mid, high, choice, sig, exp, keepPlaying)                                                      # Adds all the user input to the userInput class as p1


# ---------- Running Code ----------#
print("The sequencer will now start. Press the any key to stop the sequencer.")
print("Your sequence will be exported as %s when done."%(exp))
print()
t1 = threading.Thread(target=thread1, args=[])                                                                          # makes first thread with the sequencer data.
t2 = threading.Thread(target=thread2, args=[])                                                                          # makes second thread with a keyboard input listener.
t1.start()
t2.start()
