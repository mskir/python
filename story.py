# Author: Tim Statler
# Copyright: Comp Sci Central @ compscicentral.com
#https://github.com/timstats91/time-unraveled/blob/master/TimeUnraveled.py

import sys
import time

a = 2
b = 0.2
c = 0.08


def intro():
    print()
    print("(ANDILIM NG PALIGID)")
    time.sleep(a)
    print("mej nakikita mo na paligid")
    time.sleep(b)
    print()
    question = "I'm in a cave...?"
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(0.5)
    print()
    print()
    print("cave entrance.")
    time.sleep(a)
    print("Three paths are revealed:")
    time.sleep(b)
    print()
    print("Path #1: Exit.")
    time.sleep(b)
    print("Path #2: Explore.")
    time.sleep(b)
    print("Path #3: Climb down.")
    time.sleep(b)
    print()
    firstPath = input("Which path will you choose? (1/2/3): ")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()
    elif firstPath == '3':
        print()
        path3()


def path1():
    print("You exit forward through the cave's entrance, into the light.")
    time.sleep(a)
    print("It's incredibly bright but your vision adjusts as you continue.")
    time.sleep(a)
    print()
    s1 = '"Hello there!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s2 = "...My name is APOLLO. I thought you were my sister, ARTEMIS..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Ah, now I remember you! Yes, you're looking for CHRONOS..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()

    time.sleep(0.5)
    print()
    print()
    print("There are two paths to take to the bottom of the mountain:")
    time.sleep(a)
    print("Path #1: Take the set path down the mountain.")
    time.sleep(a)
    print("Path #2: Scale down the side of the mountain.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2): ")
    if secondPath == '1':
        path1_1()
    elif secondPath == '2':
        path1_2()


def path1_1():
    print()
    print("The sky is bright and blue and a warm breeze hits your face.")
    time.sleep(a)
    s8 = '  "I could get used to this..."'
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(.25)
    print('  --You think to yourself.')
    time.sleep(a)
    print("A boy calls out to you.")
    time.sleep(a)
    print()
    s1 = '"Hey! Wait up!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...My name is ARES..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    intro()


def path1_2():
    print()
    print("clouds surround you and the world seems small.")
    time.sleep(a)
    s1 = '  "I don\'t believe my eyes..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print()
    print("You continue down the mountain for days until you reach the bottom.")
    time.sleep(a)
    s2 = '  "Finally! I can face you, CHRONOS!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('--You yell, entering the base of Mount OLYMPUS through the largest red and black doors you\'ve ever seen')
    time.sleep(a)
    print("The darkness consumes you as you enter, unable to see a thing.")
    time.sleep(a)
    print("A thunderous voice calls out to you...")
    time.sleep(a)
    print()
    s3 = "Ah... I've been expecting you. But you're far too early..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...It appears you've taken a fairly easy route..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...You can see through the light, but not the DARKNESS..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...You've developed some STRENGTH, but not enough..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...There is more you need to grow..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...More you need to LEARN"
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...And learn you will"
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...In time..."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    intro()


def path2():
    print("You explore the depths of the rear of the cave, into the darkness.")
    time.sleep(a)
    print("It's incredibly dark but your vision adjusts as you continue forward.")
    time.sleep(a)
    print("A huge boulder slides into place behind you, blocking your path back.")
    time.sleep(a)
    print("You notice that the cave floor is declining to the left, like a spiral.")
    time.sleep(a)
    print("A woman calls out to you.")
    time.sleep(a)
    print()
    s1 = '"Hello there!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...My name is ARTEMIS... I thought you were my brother, APOLLO..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Ah, now I remember you! Yes, you're looking for CHRONOS..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...He's the one who trapped you in this time loop..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...However, I cannot bring you to him..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...Only HERMES can do that..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...However, I have heard that CHRONOS dwells at the base of this cave..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()
    print()
    print("There are two paths to continue through the cave:")
    time.sleep(a)
    print("Path #1: Go to the left.")
    time.sleep(a)
    print("Path #2: Go to the right.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2): ")
    if secondPath == '1':
        path2_1()
    elif secondPath == '2':
        path2_2()


def path2_1():
    print()
    print("You take the fork in the cave to the left and continue walking.")
    time.sleep(a)
    print("The cave floor is still declining but is becoming much steeper than before.")
    time.sleep(a)
    print("It's so dark and the winding cave seems to go on forever.")
    time.sleep(a)
    s1 = "I have no choice, I must keep going..."
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print("Still going, fortifying your will, until finally, you reach the largest red and black door in existence.")
    time.sleep(a)
    print()
    s2 = '  "Finally! I can face you, CHRONOS!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You erupt as you enter the doors at the base of the cave inside Mount OLYMPUS')
    time.sleep(a)
    print()
    print("Standing now in the largest room, in front of the largest man you've ever seen.")
    time.sleep(a)
    print("The room is dark, but you can see the source of the thunderous voice which calls out to you...")
    time.sleep(a)
    print()
    s3 = "Ah... I've been expecting you. But you're still too early..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...It appears you've taken a fairly easy route..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Your vision is keen. You see through the darkness and the light..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...However, you haven’t developed quite enough strength..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...There is more you need to grow..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...More you need to learn..."
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...And learn you will..."
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...In time."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    intro()

def path2_2():
    print()
    print("You take the fork in the cave to the right and continue walking.")
    time.sleep(a)
    print("The cave floor is now inclining and is becoming quite steep.")
    time.sleep(a)
    print("It's so dark but after what seems like days of walking, you see a glow in the distance.")
    time.sleep(a)
    s1 = '  "What in the world can that be...?"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print("Approaching the brilliant light, you reach the end of this path and see an old book perched atop a pedestal")
    time.sleep(a)
    print()
    s2 = '  "THE SECRETS OF TIME"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You read the large inscription on the cover before opening the book.')
    print()
    time.sleep(a)
    s3 = '"If you stumble upon this tomb...'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...It may save you from your doom..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Your vision is keen, that much is clear..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...But you have yet to face your fear..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = '...The truest path is one of toil..."'
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...Climb down vines beneath the soil..."
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...Speak with MOIRAE, help her first..."
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...Then you will complete your search..."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a)
    intro()


def path3():
    print("You climb down the vines into a bottomless hole in the ground")
    time.sleep(a)
    print("It's dark, damp, and hard to climb down the vines, but your vision and muscles eventually adjust.")
    time.sleep(a)
    print("A huge boulder slides into place above you, blocking your escape.")
    time.sleep(a)
    print("You continue climbing down the vines until you hear something whirring up at you.")
    time.sleep(a)
    print("Someone calls out to you.")
    time.sleep(a)
    print()
    s1 = '"Hey, hey there!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...My name is HERMES... I'll be your guide to freedom..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Yes, I know all about you! You're looking for CHRONOS..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...He's the one who trapped you in this time loop..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...I'm on my way to deliver a message, so I can't escort you personally..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...However, I can transport you there, or anywhere else on Mount OLYMPUS..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...CHRONOS is just below and he'll certainly TEST YOU when you meet him."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1)
    print()
    print()
    print("HERMES will transport you anywhere on Mount OLYMPUS:")
    time.sleep(a)
    print("Path #1: Continue below to face CHRONOS.")
    time.sleep(a)
    print("Path #2: Read: THE SECRETS OF TIME.")
    time.sleep(a)
    print("Path #3: Speak with ARES.")
    time.sleep(a)
    print("Path #4: Speak with ARTEMIS.")
    time.sleep(a)
    print("Path #5: Speak with APOLLO.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2/3/4/5): ")
    if secondPath == '2':
        path2_2()
    elif secondPath == '3':
        path1_1()
    elif secondPath == '4':
        path1()
    elif secondPath == '5':
        path2()
    else:
        print()
    print("You continue down the vines until you reach the bottom.")
    time.sleep(a)
    print("You see a small old woman next to the largest red and black iron-wrought double-doors you've ever seen.")
    time.sleep(a)
    print('The old woman calls out to you')
    time.sleep(a)
    print()
    s8 = '"Hello there, young traveler...'
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = '...My name is MOIRAE, I\'m in great need of help...'
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = '...I know who you seek... CHRONOS is just beyond this door...'
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(a)
    print()
    print()
    print("Path #1: Forget the old woman. Enter the doors and speak with CHRONOS.")
    time.sleep(a)
    print("Path #2: Honor the woman's request. Help MOIRAE return home safely.")
    time.sleep(a)
    thirdPath = input("Which path would you like to take? (1/2) ")
    if thirdPath == '1':
        path3_1()
    elif thirdPath == '2':
        path3_2()


def path3_1():
    print()
    print('You begin walking toward the doors, ignoring MOIRAE\'s request')
    time.sleep(a)
    s1 = '"I would help you but I\'m in a bit of a hurry, you understand"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print("You pull open the massive door")
    print()
    print("Standing now in the largest room, in front of the largest man you've ever seen.")
    time.sleep(a)
    print()
    s3 = "Ah... I've been expecting you. But you're somewhat early..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a)
    intro()


def path3_2():
    print()
    print('You begin walking toward MOIRAE, honoring her request')
    time.sleep(a)
    s1 = '  "I understand. I know what it\'s like to miss home... That\'s why I need to get out of here..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s2 = '  "But before I walk through those doors, I promise that I\'ll get you home safely."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a)
    print("You kneel down in front of MOIRAE, allowing her to climb easily onto your back.")
    time.sleep(a)
    print()
    s3 = "Ah... I've been expecting you. And you're right on time!..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...It appears you've taken a very difficult route..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Your vision is keen. You see through the darkness and the light..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...And your strength has grown from your travels..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(5)


# Main Function ###

print()
print()
print("     ######################")
print("     |                    |")
print("     |   Time Unraveled   |")
print("     |                    |")
print("     ######################")
print()
print()
time.sleep(a)
print("asan aq?")
time.sleep(a)
print("dilim naman...")
time.sleep(a)
print()
startGame = input("usto mue b mag laro? (yes/no): ")
if startGame == "no" or startGame == "No" or startGame == "NO":
    print()
    print("sige bye, pangit mo")
    time.sleep(3)
elif startGame == "yes" or startGame == "Yes" or startGame == "YES":
    intro()
