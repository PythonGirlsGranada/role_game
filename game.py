#!/usr/bin/env python

import random


# PENDIENTE DEL DIA ANTERIOR:

'''
- documento memories, necesario cambiarlo
'''


#dice
min = 0
max = 99

cla = "none"
name_ = "dummy"
answer = "no"
roll_dice = "no"
action = "none"
lo_tengo = False
he_ido = False

#text blocks
intro = open("introduction.txt","r")
dice_rule = open("dice.txt", "r")
primer_escenario = open("dice.txt", "r")

# defining the basic player
class Player:
    def __init__(self, name, s_class):
        self.general_points = 0
        self.name = name
        self.s_class = s_class
        self.abilities = [] #creates a list of empty abilities
        self.backpack = ["calling_device", "notebook", "pencil", "pills_tin"] #default backpack
        self.places = ["starting point, home"]

        self.rude = 0
        self.happy = 0
        self.sad = 0
        self.angry = 0
        self.nice= 0
        self.intelligence = 0
        self.charisma = 0
        self.shy = 0
        self.extrovert = 0
        self.crazy = 0
        self.techie = 0
        self.knowledge = 0
        self.pretty = 0
        self.health = 100
        #for the programmer, so he can see the errors
        self.dummy = 0

    def add_ability(self, ab):
        self.abilities.append(ab)

    def change_class(self, cl):
        self.s_class = cl

    def add_place(self,pl):
        self.places.append(pl)

    def add_personality(self, aspect):

        if aspect == "rude":
            self.rude = self.rude + 1
        elif aspect == "happy":
            self.happy = self.happy + 1
        elif aspect == "sad":
            self.sad = self.sad + 1
        elif aspect == "angry":
            self.angry = self.angry + 1
        elif aspect == "nice":
            self.nice = self.nice + 1
        elif aspect == "intelligence":
            self.intelligence = self.intelligence + 1
        elif aspect == "charisma":
            self.charisma = self.charisma + 1
        elif aspect == "shy":
            self.shy = self.shy + 1
        elif aspect == "extrovert":
            self.extrovert = self.extrovert + 1
        elif aspect == "crazy":
            self.crazy = self.crazy + 1
        elif aspect == "techie":
            self.techie = self.techie + 1
        elif aspect == "knowledge":
            self.knowledge = self.knowledge + 1
        elif aspect == "pretty":
            self.pretty = self.pretty + 1
        elif aspect == "health":
            self.health = self.health + 1
        else:
            self.dummy = self.dummy + 1



class Scene:
    def __init__(self,description):
        self.description = description
        self.objects = [] #empty list of objects availables in this room


    def add_object(self, o):
        self.objects.append(o)

    def change_d(self, d):
        self.description = d

#notebook
class Notebook:
    def __init__(self, owner):
        self.owner = owner
        self.pages = ["We need not to be let alone. We need to be really bothered once in a while. How long is it since you were really bothered? About something important, about something real?","#8956672"]

    def write_page(self, text):
        self.pages.append(text)

    def read_page(self, p):
        print self.pages[int(p)]


#dice from 0 to 99
def dice():

    d = random.randint(min, max)
    print "The dices are rolling..."
    print "They say...."
    print d
    return d

#select the action
def do_(act, pe, di, sc):
    number_a = 0
    aux = "none"
    #COMMANDS LIST
    # SEE
    if act == "see":
        print "See..."
        print "------------------"
        print "1- around"
        print "2- something else"
        op = raw_input("What do you want to see? >> ")

        if op == "1" or op == "around":
            print sc.description
        else:
            #add logic
            print "proximo"
            for i in sc.objects:
                print i

    #CHECK BACKPACK
    elif act == "check backpack":
        for x in pe.backpack:
            print x
    #USE
    elif act == "use":
        #lo_tengo = False
        for i in pe.backpack:
            print i

        obj = raw_input("What are you going to use? >> ")

        for j in pe.backpack:
            if obj == j:
                lo_tengo = True

        if lo_tengo:
            print "You are going to use " + obj
            aux = obj
        else:
            print "You don't have that item yet"

        #return obj
        number_a = 2

    #READ
    elif act == "read":
        nb = raw_input("Want to read the notebook? >> ")
        if nb == "yes":
            pa = raw_input("Which page? >> ")
            print di.pages[int(pa)]
            # use read_page instead
        else:
            #this will change
            #print "You have nothing else to read for now"
            for a in pe.backpack:
                if a.contains("book"):
                    sentence = "Read " + a
                    answer = raw_input( sentence + " ? >> " )
                    if answer == "yes":
                        print "You read " + a
                    else:
                        print "You changed your mind and let the book alone."
                if b.contains("paper"):
                    sentence = "Read " + b
                    answer = raw_input(sentence + "? >> ")
                    if answer == "yes":
                        print "You read " + b
                    else:
                        print "You changed your mind and let the paper alone."
        number_a = 3

    #SLEEP
    elif act == "sleep":
        number_a = 4
        dream(pe)

    #WRITE
    elif act == "write":
        number_a = 5
        te = raw_input("Write >> ")
        di.write_page(te)

    #GO
    elif act == "go":
        for a in pe.places:
            print a
        place = raw_input("where do you want to go? >> ")
        for b in pe.places:
            if b == place:
                he_ido = True

        if he_ido:
            print "You go to " + place
        #number_a = 6
        aux = place

    #TAKE
    elif act == "takes":
        ob = raw_input("What are you going to take?")
    else:
        print "You do nothing"

    return aux

#dreaming...
def dream(p):
    dream = random.randint(0,5)
    dreams =  ["You dream of an unicorn... You don't know where it comes from. Always confused about this dream...", "You have an ugly nightmare... maybe you are loosing your mind", "You dream of an ocean. It's scary but at the same time beautiful. You feel... happy", "You dream of a desert. You see a died lion in the sand, everything is quiet. You feel... sad", "You cannot remember your dream.", "You dream of someone, someone important. But you can't remember the face... gah! you feel... angry"]

    print dreams[dream]

    if dream == 1:
        p.add_personality("crazy")
    elif dream == 2:
        p.add_personality("happy")
    elif dream == 3:
        p.add_personality("sad")
    elif dream == 4:
        p.add_personality("angry")


#printing the introduction...
print intro.read()

#getting main player name and class
while answer == "no":
    name_ = raw_input("Assistant - What is your name? >> ")
    sentence = "Assistant - Your name is " + name_
    answer = raw_input( sentence + ", right? >> " )

print "Assistant - Nice to meet you " + name_
print " "
print dice_rule.read()
print " "

while roll_dice == "no":
    roll_dice = raw_input("Assistant - Ready to roll the dices?  >> ")
    print "okay..."

di = dice()

if di > 50:
    print "Assistant - Congratulations lucky kid, you get to choose your class."
    cla = raw_input("Write your class here >> ")
else:
    print "Assistant - Unfortunately you cannot choose your class... The dices weren't on your favour. Your class will be 'dummy kid' until you have the chance to change it again"
    cla = "dummy kid"

#creating main character
p = Player(name_,cla)
for i in p.backpack:
    if i == "notebook":
        diario = Notebook(name_)

# getting a friend
new_cha = "no"
new_cha = raw_input("Assistant - Do you want a friend to join you? >> ")

if new_cha == "yes":
    print "Assistant - Okay. Just tell me a name. For now your friend class will be only 'friend'. Maybe you guys will have the chance to change it later."
    new_cha_name = raw_input("Name >> ")
    p2 = Player(new_cha_name, "friend")
    print "Assistant - Your friend me reminds me of a very close friend I used to have too..."
else:
    print "Assistant - Okay, lone wolf, eh? I was like you when I was young..."

# trying the points system
print "-------------------------------------------------------"
print "1- I'm not interested "
print "2- Really? Why is that? "
print "3- Yes... see you."
print "--------------------------------------------------------"
answer = raw_input(">> ")
print "--------------------------------------------------------"

if answer == "1":
    print "Assistant - Wow, pretty rude. Anyway, I'm not interested in telling you more. Go away already."
    p.add_personality("rude")
    p.add_personality("charisma")
elif answer == "2":
    print "Assistant - Yes... But that's quite a long story. You seems to be a nice person...Good luck out there, kid."
    p.add_personality("nice")
    p.add_personality("extrovert")
else:
    print "Assistant - Quite mysterious. Anyway, be seeing you."
    p.add_personality("shy")
print "--------------------------------------------------------"
print " "

#learning about the backpack
print "You check yourself, and notice you are wearing a backpack..."
answer = raw_input("Want to check the inside? >> ")

if answer == "yes":
    print "You take your backpack and open it. Takes a sight inside..."
    for x in p.backpack:
        print x
    print " "
    #learning about the notebook
    print "There's a notebook there. Want to check the inside? "
    answer = raw_input("Want to check the inside? >> ")
    if answer == "yes":
        print "There's stuff writen in here..."
        page = raw_input("What page do you want to check? >> ")
        print diario.pages[int(page)]
    print "From now on, if you want to check your backpack write 'check backpack' when you are not doing anything else. If you want to write in the notebook type 'write' or 'read' to choose read the notebook."
else:
    #jump the instructions
    print "Okay, smart ass."

print "Now, you are on your own..."

#key is watching, let the player try other things
first_sc = Scene("sitio de inicio")

first_sc.add_object("objeto1")
first_sc.add_object("objeto2")
first_sc.add_object("objeto3")
first_sc.add_object("objeto4")

while(action != "see"):

    action = raw_input("What do you do? >> ")
    do_(action, p, diario, first_sc)
