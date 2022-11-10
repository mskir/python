import sys
import time

x = 2
y = 0.2
z = 0.08
def Bedroom():
  print()
  print("You woke up with a ringing in your head...")
  print()
  time.sleep(x)
  print("You found yourself in an unfamiliar room...")
  time.sleep(y)
  print()
  senBR1 = "UGH... It hurts like hell..."
  for c in senBR1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senBR2 = "Where on earth am I?... Fuuu**..."
  for c in senBR2:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  print("Looking around to see where you are...")
  time.sleep(x)
  print()
  print("The room looks like a normal bedroom")
  time.sleep(y)
  print()
  senBR3 = "It looks pretty normal... Wait... What is that?..."
  for c in senBR3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  TwoObjects()

def TwoObjects():
  print("There are two objects that have piqued your interest")
  time.sleep(x)
  print()
  objects = ["Pictures","pictures","Letter","letter"]
  user = ""
  global count 
  while user not in objects:
    print("Interact: Pictures/Letter")
    print()
    user = input()
    if user == "Pictures":
        Pictures1()
    elif user == "Letter":
        Letter1()   
    else:
        print("Please enter a valid option.")
  time.sleep(y)
  print()

def Pictures1():
  print()
  print("The wall is covered in pictures")
  print()
  time.sleep(y)
  print()
  senPic1 = "Those pictures..."
  for c in senPic1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senPic2 = "NO FUCKING WAY!!!"
  for c in senPic2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senPic3 = "THESE ARE STOLEN PICTURES OF ME!!!"
  for c in senPic3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senPic4 = "Who took these?!..."
  for c in senPic4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senPic2 = "It's so creepy and disgusting..."
  for c in senPic2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  TwoObjects()

def Letter1():
  print()
  print("There's a letter on the table")
  print()
  time.sleep(y)
  print("The letter reads:")
  print()
  time.sleep(y)
  print()
  senlet1 = "To my Dearest Darling,"
  for c in senlet1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  print()
  senlet2 = "You looked so lovely today. "
  for c in senlet2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  senlet3 = "I really liked the way that you were wearing your hair it looks so pretty like that... \nyou should wear it that way more often, \nand the lip gloss you wore smelled so sweet. \nWhat kind was it anyway? I wanted to taste it and find out... \nBut I couldn't, darling. "
  for c in senlet3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  
  senlet4 = "The way those bugs fly around and gather around you so annoyingly... I want to crush them..."
  for c in senlet4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()

  senlet5 = "Soon my Darling, I'll be able to be with you without any flies buzzering around..."
  for c in senlet5:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  print()
  senlet6 = "XOXO"
  for c in senlet6:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  TwoObjects()



#Bedroom()
TwoObjects()

def Pictures1():
  print()
  print("The wall is covered in pictures")
  print()
  time.sleep(y)
  print()
  senPic1 = "Those pictures..."
  for c in senPic1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senPic2 = "NO FUCKING WAY!!!"
  for c in senPic2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senPic3 = "THESE ARE STOLEN PICTURES OF ME!!!"
  for c in senPic3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senPic4 = "Who took these?!..."
  for c in senPic4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senPic2 = "It's so creepy and disgusting..."
  for c in senPic2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  TwoObjects()

  

Pictures1()

def Letter1():
  print()
  print("There's a letter on the table")
  print()
  time.sleep(y)
  print("The letter reads:")
  print()
  time.sleep(y)
  print()
  senlet1 = "To my Dearest Darling,"
  for c in senlet1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  print()
  senlet2 = "You looked so lovely today. "
  for c in senlet2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  senlet3 = "I really liked the way that you were wearing your hair it looks so pretty like that... \nyou should wear it that way more often, \nand the lip gloss you wore smelled so sweet. \nWhat kind was it anyway? I wanted to taste it and find out... \nBut I couldn't, darling. "
  for c in senlet3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  
  senlet4 = "The way those bugs fly around and gather around you so annoyingly... I want to crush them..."
  for c in senlet4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()

  senlet5 = "Soon my Darling, I'll be able to be with you without any flies buzzering around..."
  for c in senlet5:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  print()
  senlet6 = "XOXO"
  for c in senlet6:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  TwoObjects()

Letter1()

def TwoDoors():
  print()
  print("After looking around you see two doors...")
  print()
  time.sleep(x)
  door = ["Door 1","Door 2"]
  user = ""
  while user not in door:
    print("Interact: Door 1/ Door 2")
    print()
    user = input()
    if user == "Door 1":
        Door1()
    elif user == "Door 2":
        Door2()  
    else:
        print("Please enter a valid option.")
  time.sleep(y)
  print()
  
  def Door1():
  print()
  print("The door leads to a bathroom...")
  print()
  time.sleep(x)
  print("You take a look around...")
  time.sleep(y)
  print()
  senCR1 = "Ew... It smells like rotten eggs in here..."
  for c in senCR1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senBR1 = "BLEGCH... There's nothing here anyways..."
  for c in senBR1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  TwoDoors()
  
  def Door2():
  print()
  print("The door leads to a dark hallway...")
  print()
  time.sleep(y)
  print()
  senDR1 = "I can't see anything at all..."
  for c in senDR1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  print("Will you go forward or backward?")
  print()
  time.sleep(y)
  print()
  direction = ["Forward","Backward"]
  user = ""
  while user not in direction:
    print("Interact: Forward/Backward")
    print()
    user = input()
    if user == "Forward":
        Hallway1()
    elif user == "Backward":
        Bedroom()   
    else:
        print("Please enter a valid option.")
  time.sleep(y)
  print()
  
  def Hallway1():
  print()
  print("While walking through the hallway you stumble upon a dresser...")
  print()
  time.sleep(y)
  print()
  print()
  senHW1 = "Please let there be a flashlight or something..."
  for c in senHW1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  Drawer1()

def Drawer1():
  print()
  print("There's three drawers in the dresser...")
  print()
  time.sleep(y)
  print()
  drawer = ["Drawer 1","Drawer 2", "Drawer 3"]
  user = ""
  while user not in drawer:
    print("Interact: Drawer 1/Drawer 2/Drawer 3")
    print()
    user = input()
    if user == "Drawer 1":
        Letter2()
    elif user == "Drawer 2":
        Flashlight()
    elif user == "Drawer 3":
        PictureDr()
    else:
        print("Please enter a valid option.")
  time.sleep(y)
  print()
  print()
  print()
def Letter2():
    senlet2_1 = "Oh look another letter addressed to me, how wonderfull..."
    for c in senlet2_1:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(y)
    time.sleep(0.5)
    print()
    print()
    senlet2_2 = "Dear Honey,"
    for c in senlet2_2:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(z)
    time.sleep(0.5)
    print()
    print()
    senlet2_3 = "What I have to say to you is SO very personal, it's really the kind of thing I should say to you myself."
    for c in senlet2_3:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)
    print()
    senlet2_4 = "But I can't. I JUST CAN'T!"
    for c in senlet2_4:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)
    print()
    senlet2_5 = "I try and I try to approach you but...I'm always interrupted. \nIt's because of all those flies around you, your so-called friends. \nAnnoying, buzzing, babbling little flies. \nI HATE them! I HATE that you're NEVER alone, \nthat I can NEVER just talk to you! \nSome are meant to be said alone but...THOSE FLIES! \nAlways buzzing around you! \nSuch annoying creatures! \nI had SUCH a wonderful confession all planned but those friends of yours ruin it! \nEvery! Single! Time! \nThey always say that flies are attracted to honey and I guess that's pretty true, huh? \nYou are so sweet and lovely, just like honey. \nAnd I guess I can't really blame you for being so popular. You're pretty and perfect and I'm not the only one who's drawn to you. \nBut I AM the only one who deserves you!"
    for c in senlet2_5:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)
    print()
    print()
    Drawer1()
def Flashlight():
  senflash1 = "For the love of... Finally a flashlight... I hope it works"
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  Drawer1()

def PictureDr():
  senflash1 = "Another picture?..."
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senflash1 = "And it's a picture of me... and who?..."
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senflash1 = "Who is he and why is he crossed out like that?..."
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  #Hallway1_2()
Hallway1()

def Letter2():
  senlet2_1 = "Oh look another letter addressed to me, how wonderfull..."
  for c in senlet2_1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senlet2_2 = "Dear Honey,"
  for c in senlet2_2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  print()
  senlet2_3 = "What I have to say to you is SO very personal, it's really the kind of thing I should say to you myself."
  for c in senlet2_3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.5)
  print()
  print()
  senlet2_4 = "But I can't. I JUST CAN'T!"
  for c in senlet2_4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.5)
  print()
  print()
  senlet2_5 = "I try and I try to approach you but...I'm always interrupted. \nIt's because of all those flies around you, your so-called friends. \nAnnoying, buzzing, babbling little flies. \nI HATE them! I HATE that you're NEVER alone, \nthat I can NEVER just talk to you! \nSome are meant to be said alone but...THOSE FLIES! \nAlways buzzing around you! \nSuch annoying creatures! \nI had SUCH a wonderful confession all planned but those friends of yours ruin it! \nEvery! Single! Time! \nThey always say that flies are attracted to honey and I guess that's pretty true, huh? \nYou are so sweet and lovely, just like honey. \nAnd I guess I can't really blame you for being so popular. You're pretty and perfect and I'm not the only one who's drawn to you. \nBut I AM the only one who deserves you!"
  for c in senlet2_5:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.5)
  print()
  print()
  
  def Letter2():
  senlet2_1 = "Oh look another letter addressed to me, how wonderfull..."
  for c in senlet2_1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senlet2_2 = "Dear Honey,"
  for c in senlet2_2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  print()
  senlet2_3 = "What I have to say to you is SO very personal, it's really the kind of thing I should say to you myself."
  for c in senlet2_3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.5)
  print()
  print()
  senlet2_4 = "But I can't. I JUST CAN'T!"
  for c in senlet2_4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.5)
  print()
  print()
  senlet2_5 = "I try and I try to approach you but...I'm always interrupted. \nIt's because of all those flies around you, your so-called friends. \nAnnoying, buzzing, babbling little flies. \nI HATE them! I HATE that you're NEVER alone, \nthat I can NEVER just talk to you! \nSome are meant to be said alone but...THOSE FLIES! \nAlways buzzing around you! \nSuch annoying creatures! \nI had SUCH a wonderful confession all planned but those friends of yours ruin it! \nEvery! Single! Time! \nThey always say that flies are attracted to honey and I guess that's pretty true, huh? \nYou are so sweet and lovely, just like honey. \nAnd I guess I can't really blame you for being so popular. You're pretty and perfect and I'm not the only one who's drawn to you. \nBut I AM the only one who deserves you!"
  for c in senlet2_5:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.5)
  print()
  print()
  
  def Flashlight():
  senflash1 = "For the love of... Finally a flashlight... I hope it works"
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  Drawer1()
  
  def PictureDr():
  senflash1 = "Another picture?..."
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senflash1 = "And it's a picture of me... and who?..."
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senflash1 = "Who is he and why is he crossed out like that?..."
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  #Hallway1_2()
  
  def Hallway1_2():
  print()
  print("With flashlight in hand you walk more")
  print()
  time.sleep(x)
  print("After some steps you see stairs leading down to the next floor...")
  time.sleep(y)
  print()
  print()
  
  def Hallway2():
  print()
  print("After walking down the stairs you arrive at another dark hallway")
  print()
  time.sleep(x)
  print("Along the hallway there's three doors")
  time.sleep(y)
  print()
  print()
  doors = ["Door A","Door B, Door C"]
  user = ""
  while user not in doors:
    print("Interact: Door A/Door B/Door C")
    print()
    user = input()
    if user == "Door A":
        doora()
    elif user == "Door B":
        doorb()  
    elif user == "Door C":
        doorc()    
    else:
        print("Please enter a valid option.")
  time.sleep(y)
  print()
  print()
  
  def doora():
  senflash1 = "Hmm... Theres nothing here but a cabinet... And it's locked..."
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  
  def doorb():
  sendb1 = "Ahh shiiii... There's broken portraits everywhere..."
  for c in sendb1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendb2 = "Wait... There's one that's not fully destroyed..."
  for c in sendb2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendb3 = "This kid looks familliar... Who the hell is he?..."
  for c in sendb3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendb4 = "There's something in the back"
  for c in sendb4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  flip = ["Flip","No"]
  user = ""
  while user not in flip:
    print("Interact: Flip/No")
    print()
    user = input()
    if user == "Flip":
        Picture1()
    elif user == "No":
        Hallway2()   
    else:
        print("Please enter a valid option.")
  time.sleep(y)
  print()
  print()
  
  def Picture1():
  senP1 = "Hmm?..."
  for c in senP1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senP2 = "The back says..."
  for c in senP2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senP3 = "---, Cozer, 09/11/2007..."
  for c in senP3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  Hallway2()
  
  def doorc():
  sendc1 = "Shiiiii... More broken stuff... Should've known..."
  for c in sendc1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendc2 = "At least there's a key here..."
  for c in sendc2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendc3 = "Is dis the key for the cabinet in the other room?"
  for c in sendc3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendc4 = "I think so... One way to find out..."
  for c in sendc4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  cabinet()
  
  def cabinet():
  print()
  print("After trying to open the cabinet with the key the door finally opened...")
  print()
  time.sleep(x)
  print()
  print()
  sendcb1 = "UEGH... What's that smell?..."
  for c in sendcb1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendcb2 = "No... way... Are those..."
  for c in sendcb2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendcb3 = "That's the watch I gave Jonathan... \nThe necklace I gifted to Roi... \n Even the earrings I bought for Chris's birthday... \nThey're all my gifts for my exes!!!"
  for c in sendcb3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendcb2 = "I feel sick... I haven't had contact with them at all is this the reason?..."
  for c in sendcb2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
