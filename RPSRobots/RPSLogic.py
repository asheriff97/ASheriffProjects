'''
PYTHON LOGIC FOR RPS ROBOTS
This file is not runnable! It needs to be ran in the software supported by NAO Robots (Choregraphe)
When looking at "Brain.png" This code is located as the "Wait for signals" box.
It waits until this and the other robot makes its choice, and then calculates the winner.
'''

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)
        self.mychoice="z"
        self.player2choice="x"
        self.result="y"

    def onLoad(self):
        self.ok = [False]*2

    def onUnload(self):
        #puts code for box cleanup here
        ""

    def onStart(self, nInput):



        self.ok[nInput-1] = True
        bOutput = True
        for bOk in self.ok:
            bOutput = bOutput and bOk
        if( bOutput ):
            self.ok = [False]*2

            me = self.mychoice
            player2 = False

            while player2 == False:
                player2 = self.player2choice
                if player2 == me:
                    self.result = "tie"
                    break
                elif player2 == "rock":
                    if me == "paper":
                        self.result = "I win"
                        break
                    else:
                        self.result = "You win"
                        break
                elif player2 == "paper":
                    if me == "scissors":
                        self.result = "I win"
                        break
                    else:
                        self.result = "You win"
                        break
                elif player2 == "scissors":
                    if me == "rock":
                        self.result = "I win"
                        break
                    else:
                        self.result = "You win"
                        break
                else:
                    self.result = "error"
                    break
                player2 = False

            self.signalsReceived(self.result)



    def onInput_signal2(self, p):
        self.player2choice = str(p)
        self.onStart(2)


    def onInput_signal1(self, p):

        self.mychoice = str(p)
        if self.mychoice == "1":
            self.mychoice = "rock"
        elif self.mychoice == "2":
            self.mychoice = "paper"
        elif self.mychoice == "3":
            self.mychoice = "scissors"
        self.onStart(1)