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

    def staticSeq(self):
        print() #placeholder

    def debug(self):
        print("The BPM is: " + str(self.bpm))
        print("The low sample is: " + self.low)
        print("The mid sample is: " + self.mid)
        print("The high sample is: " + self.high)
        if self.choice == True:
            print ("You've chosen to have a changing signature.")
        elif self.choice == False:
            print ("You've chosen to have a static signature.")
        print("The signature you've chosen is: " + self.sig)
        print("the file will be exported as: " + self.exp)

p1 = userInput(120, "low.wav", "mid.wav", "high.wav", False, "5/8", "Export.midi")

p1.debug()
