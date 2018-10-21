# ---------- Imports ----------#
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

    def randomSeq(self):
        global timestampsBuffer
        sig = random.randint(9,19)
        timestamps = []                                                                                 # create a list to hold the timestamps
        timestamps16th = []                                                                             # create a list for 16th notes with a starting position
        sigSum = 0
        sigSum = sigSum + sig
        notes16th = [2, 2, 2]
        while True:
            if sum(notes16th) > sig:
                notes16th.pop()
                if sum(notes16th) < sig -5:
                    notes16th.append(random.randint(1, 2))
                break
            else:
                notes16th.append(random.randint(1, 2))
        for value in notes16th:
            if timestamps16th==[]:
                timestamps16th.append(0)
            else:
                timestamps16th.append(max(timestamps16th) + value)
        timestampsBuffer = timestamps16th
        for timestamp in timestamps16th:
            timestamps.append(timestamp * ((60 / bpm) / 4.0))
        # retrieve first timestamp
        # NOTE: pop(0) returns and removes the element at index 0
        timestamp = timestamps.pop(0)
        # retrieve the startime: current time
        startTime = time.time()
        samNum = 0
        # play the sequence
        while keepPlaying==True:
            # retrieve current time
            currentTime = time.time()
            # check if the timestamp's time is passed
            if(currentTime - startTime >= timestamp):
                # play sample
                if samNum == 0:
                    lowPlay.play()
                    samNum=samNum+1
                    noteValues.append(32)
                    timestamp = timestamps.pop(0)
                elif samNum ==1:
                    highPlay.play()
                    samNum=samNum+1
                    noteValues.append(35)
                    timestamp = timestamps.pop(0)
                elif samNum == 2:
                    midPlay.play()
                    samNum=samNum+1
                    noteValues.append(34)
                    timestamp = timestamps.pop(0)
                else:
                    SamplePlay()
                # if there are timestamps left in the timestamps list
                    if timestamps:
                    # retrieve the next timestamp
                        timestamp = timestamps.pop(0)
                    else:
                        time.sleep(((60 / bpm) / 4.0))
                        print(timestampsBuffer)
                        sig = random.randint(9,19)
                        notes16th = [2, 2, 2]
                        timestamps16th=[]
                        timestamps=[]
                        while True:
                            if sum(notes16th) > sig:
                                notes16th.pop()
                                if sum(notes16th) < sig -5:
                                    notes16th.append(random.randint(1, 2))
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
                # wait for a very short moment
                time.sleep(0.001)

    def staticSeq(self):
        global timestampsBuffer
        timestamps = []                                                                                 # create a list to hold the timestamps
        timestamps16th = []                                                                             # create a list for 16th notes with a starting position
        sigSum = 0
        sigSum = sigSum + sig
        notes16th = [2, 2, 2]
        while True:
            if sum(notes16th) > sig:
                notes16th.pop()
                if sum(notes16th) < sig -5:
                    notes16th.append(random.randint(1, 2))
                break
            else:
                notes16th.append(random.randint(1, 2))
        for value in notes16th:
            if timestamps16th==[]:
                timestamps16th.append(0)
            else:
                timestamps16th.append(max(timestamps16th) + value)
        timestampsBuffer = timestamps16th
        for timestamp in timestamps16th:
            timestamps.append(timestamp * ((60 / bpm) / 4.0))
        # retrieve first timestamp
        # NOTE: pop(0) returns and removes the element at index 0
        timestamp = timestamps.pop(0)
        # retrieve the startime: current time
        startTime = time.time()
        samNum = 0
        # play the sequence
        while keepPlaying==True:
            # retrieve current time
            currentTime = time.time()
            # check if the timestamp's time is passed
            if(currentTime - startTime >= timestamp):
                # play sample
                if samNum == 0:
                    lowPlay.play()
                    samNum=samNum+1
                    noteValues.append(32)
                    timestamp = timestamps.pop(0)
                elif samNum ==1:
                    highPlay.play()
                    samNum=samNum+1
                    noteValues.append(35)
                    timestamp = timestamps.pop(0)
                elif samNum == 2:
                    midPlay.play()
                    samNum=samNum+1
                    noteValues.append(34)
                    timestamp = timestamps.pop(0)
                else:
                    SamplePlay()
                # if there are timestamps left in the timestamps list
                    if timestamps:
                    # retrieve the next timestamp
                        timestamp = timestamps.pop(0)
                    else:
                        time.sleep(((60 / bpm) / 4.0))
                        print(timestampsBuffer)
                        notes16th = [2, 2, 2]
                        timestamps16th=[]
                        timestamps=[]
                        while True:
                            if sum(notes16th) > sig:
                                notes16th.pop()
                                if sum(notes16th) < sig -5:
                                    notes16th.append(random.randint(1, 2))
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
                # wait for a very short moment
                time.sleep(0.001)

# ---------- Initialization ----------#
audioFiles = []
listOfFiles = os.listdir('./Samples')
pattern = "*.wav"
pause = False
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        audioFiles.append(entry)
bpm = 120
channel = 0
pitch = 0
PitchOut = 32 + pitch
volume = 127
keepPlaying = True
noteValues = []
mf = MIDIFile(1)                       #Name library
track = 0                               #Create track

def thread1 ():
  if p1.choice == 'random':
      p1.randomSeq()
  elif p1.choice == 'static':
      p1.staticSeq()

def thread2 ():
    with keyboard.Listener(
          on_press=on_press,
          on_release=on_release) as listener:
      listener.join()

def on_press(key):
    try:
        global keepPlaying
        keepPlaying = False
        print(timestampsBuffer)
        for pos, val in zip(timestampsBuffer, noteValues):
            mf.addNote(track, channel, val, pos/4.0, 0.125, volume)
        with open("output.mid", 'wb') as outf:
            mf.writeFile(outf)
        print("The sequencer has been stopped. Your midi file has been created. Have a nice day! :)")
        time.sleep(2)
        return False
    except AttributeError:
        print()

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def SamplePlay():
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
while True:
    ask = input("The current BPM is %s beats per minute. would you like to change it? [Y/N] " %(bpm)).lower()
    if ask == "y":
        while True:
            try:
                bpm = int(input("Please fill in what BPM you would like. "))
                break
            except ValueError:
                print("That's no value, silly goose.")
    elif ask == "n":
        break
    else:
        print("That's not a yes or a no. Please use Y or N as your answer.")
        print()
    break

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
        sig = random.randint(9,19)
        break
    else:
        print("That's not a yes or a no. Please use Y or N as your answer.")
        print()

samples = [lowPlay, midPlay, highPlay]
exp = "poep.mid"
p1 = userInput(bpm, low, mid, high, choice, sig, exp, keepPlaying)

# ---------- Thread1 starts ----------#

t1 = threading.Thread(target=thread1, args=[])
t2 = threading.Thread(target=thread2, args=[])
t1.start()
t2.start()
