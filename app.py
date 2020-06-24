import random
import tkinter as tk



questions = [["What movie came out first in the MCU?","The Incredible Hulk","Thor","Captian America: The Fist Avenger","Iron Man"]]
questions.append(["Who made Captain America’s shield?","Tony Stark","Nick Fury","Peggy Carter","Howard Stark"])
questions.append(["What is Captain America’s shield made out of?","Adamantium","Iron","Tungston","Vibranium"])
questions.append(["What is Black Widow’s real name?","Demi Robinson","Ellie Johnson","Darya Smirnov","Natasha Romanoff"])
questions.append(["On what planet was the Soul Stone hidden in Infinity War?","Krypton","Galifrey","Cybertron","Vormir"])
questions.append(["What is the name of Thor’s hammer?","Stormbreaker","Percy","Ampco","Mjolnir"])
questions.append(["In which film’s post-credit scene did Thanos first appear?","Avengers: Age of Ultron","Iron Man","Thor: The Dark World","Avengers Assemble"])
questions.append(["Director Taika Waititi also played which comedic Thor: Ragnarok character?","Valkyrie","Heimdall","Odin","Korg"])
questions.append(["Who played Bruce Banner in The Incredible Hulk?","Mark Ruffalo","Lou Ferrigno","Eric Bana","Edward Norton"])
questions.append(["What is the name of Black Panther’s home country?","Kenya","Ghana","Ethiopia","Wakanda"])
questions.append(["Which former Batman played Spider-Man villain the Vulture?","Christian Bale","Ben Affleck","Adam West","Michael Keaton"])
questions.append(["Who was Tony Stark’s favourite band, whose songs feature in the Iron Man movies?","The Rolling Stones","Led Zeppelin","Guns N' Roses","AC/DC"])
questions.append(["What species is Loki revealed to be?","Asguardian","Dark Elf","Chitauri","Frost Giant"])
questions.append(["Before becoming Vision, what is the name of Iron Man’s A.I. butler?","Jeeves","Alfred","Benson","Jarvis"])
questions.append(["What is the only Marvel film not to have a post-credit scene?","Iron Man","Guardians of the Galaxy","Avenger:Infinity War","Avengers: Endgame"])

def clear():
    list = window.grid_slaves()
    for n in list:
        n.destroy()

class Quiz:
    def __init__(self,quest):
        clear()
        self.ask = []
        for n in quest:
            self.ask.append(n)
        self.a1=""
        self.a2=""
        self.a3=""
        self.a4=""
        self.Ra=""
        self.RaBtn = tk.Button(window, text="")
        self.b1 = tk.Button(window, text="")
        self.b2 = tk.Button(window, text="")
        self.b3 = tk.Button(window, text="")
        self.b4 = tk.Button(window, text="")
        self.lock=False
        self.right=0
        self.next = tk.Button(window,text="Next",command=self.Question)
        self.number=0
        self.Max=3
        self.Question()
    def Question(self):
        self.next.grid(column=0,row=5,pady=5)
        if len(self.ask) > 0 and self.number < self.Max:
            self.number += 1
            self.lock = False
            randNum = random.randint(0,len(self.ask)-1)
            AskText = self.ask[randNum][0]
            self.Ra = self.ask[randNum][-1]
            answers = []
            for i in range(1,5):
                answers.append(self.ask[randNum][i])
            random.shuffle(answers)

            self.a1 = answers[0]
            self.a2 = answers[1]
            self.a3 = answers[2]
            self.a4 = answers[3]

            Question = tk.Text(window, width=40, height=2)
            Question.insert(tk.END,AskText)
            Question.grid(column=0,row=0,padx=110,pady=(75,0))

            self.b1 = tk.Button(window, text=self.a1, width=39,command = self.control1)
            self.b2 = tk.Button(window, text=self.a2, width=39,command = self.control2)
            self.b3 = tk.Button(window, text=self.a3, width=39,command = self.control3)
            self.b4 = tk.Button(window, text=self.a4, width=39,command = self.control4)

            self.b1.grid(column=0,row=1,pady=(8,5))
            self.b2.grid(column=0,row=2,pady=5)
            self.b3.grid(column=0,row=3,pady=5)
            self.b4.grid(column=0,row=4,pady=5)

            if self.a1 == self.Ra:
                self.RaBtn = self.b1
            elif self.a2 == self.Ra:
                self.RaBtn = self.b2
            elif self.a3 == self.Ra:
                self.RaBtn = self.b3
            elif self.a4 == self.Ra:
                self.RaBtn = self.b4
            self.ask.pop(randNum)
        else:
            clear()
            lb = tk.Label(window, text="You got " + str(self.right) + " out of " + str(self.Max) + " correct!")
            lb.grid(column=0,row=0,padx=205,pady=(170,15))
            zumMenu = tk.Button(window, text="Menu",command=menuCreator)
            zumMenu.grid(column=0,row=1)
            leave = tk.Button(window, text="Quit",command=window.destroy)
            leave.grid(column=0, row=2)
    
    def control1(self):
	    if self.lock == False:
		    if self.Ra != self.a1:
			    self.b1.configure(bg="red")
		    else:
			    self.b1.configure(bg="green")
			    self.right += 1
		    self.RaBtn.configure(bg="green")
		    self.lock = True
            

    def control2(self):
	    if self.lock == False:
		    if self.Ra != self.a2:
			    self.b2.configure(bg="red")
		    else:
			    self.b2.configure(bg="green")
			    self.right += 1
		    self.RaBtn.configure(bg="green")
		    self.lock = True

    def control3(self):
	    if self.lock == False:
		    if self.Ra != self.a3:
			    self.b3.configure(bg="red")
		    else:
			    self.b3.configure(bg="green")
			    self.right += 1
		    self.RaBtn.configure(bg="green")
		    self.lock = True

    def control4(self):
	    if self.lock == False:
		    if self.Ra != self.a4:
			    self.b4.configure(bg="red")
		    else:
			    self.b4.configure(bg="green")
			    self.right += 1
		    self.RaBtn.configure(bg="green")
		    self.lock = True


class Menu:
    def __init__(self):
        clear()
        self.Quiz = tk.Button(window, text="Quiz", command=quizCreator, width=15, height=3)
        self.Quiz.grid(column=0,row=0,padx=218,pady=170)
        self.leave1 = tk.Button(window, text="Quit",command=window.destroy)
        self.leave1.grid(column=0, row=3,padx=218,pady=170)

def menuCreator():
    m = Menu()

def quizCreator():
    q = Quiz(questions)

window = tk.Tk()
window.title("Quiz")
window.geometry("550x400")

menuCreator()

window.mainloop()