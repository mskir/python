import sys
import time

x = 1
y = 0.05
z = 0.05
def Bedroom():
  print()
  print("You woke up with a ringing in your head...")
  print()
  time.sleep(x)
  print("You found yourself in an unfamiliar room...")
  time.sleep(y)
  print()
  senBR1 = "𝐔𝐆𝐇... 𝐈𝐭 𝐡𝐮𝐫𝐭𝐬 𝐥𝐢𝐤𝐞 𝐡𝐞𝐥𝐥..."
  for c in senBR1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senBR2 = "𝐖𝐡𝐞𝐫𝐞 𝐨𝐧 𝐞𝐚𝐫𝐭𝐡 𝐚𝐦 𝐈?... 𝐅𝐮𝐮𝐮**..."
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
  senBR3 = "𝐈𝐭 𝐥𝐨𝐨𝐤𝐬 𝐩𝐫𝐞𝐭𝐭𝐲 𝐧𝐨𝐫𝐦𝐚𝐥... 𝐖𝐚𝐢𝐭... 𝐖𝐡𝐚𝐭 𝐢𝐬 𝐭𝐡𝐚𝐭?..."
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
  user = "" 
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
  time.sleep(y)
  print()


def Pictures1():
  print()
  print("The wall is covered in pictures")
  print()
  time.sleep(y)
  print()
  senPic1 = "𝐓𝐡𝐨𝐬𝐞 𝐩𝐢𝐜𝐭𝐮𝐫𝐞𝐬..."
  for c in senPic1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senPic2 = "𝐍𝐎 𝐅𝐔𝐂𝐊𝐈𝐍𝐆 𝐖𝐀𝐘!!!"
  for c in senPic2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senPic3 = "𝐓𝐇𝐄𝐒𝐄 𝐀𝐑𝐄 𝐒𝐓𝐎𝐋𝐄𝐍 𝐏𝐈𝐂𝐓𝐔𝐑𝐄𝐒 𝐎𝐅 𝐌𝐄!!!"
  for c in senPic3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senPic4 = "𝐖𝐡𝐨 𝐭𝐨𝐨𝐤 𝐭𝐡𝐞𝐬𝐞?!..."
  for c in senPic4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senPic2 = "𝐈𝐭'𝐬 𝐬𝐨 𝐜𝐫𝐞𝐞𝐩𝐲 𝐚𝐧𝐝 𝐝𝐢𝐬𝐠𝐮𝐬𝐭𝐢𝐧𝐠..."
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
  senlet1 = "𝑻𝒐 𝒎𝒚 𝑫𝒆𝒂𝒓𝒆𝒔𝒕 𝑫𝒂𝒓𝒍𝒊𝒏𝒈,"
  for c in senlet1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  print()
  senlet2 = "𝒀𝒐𝒖 𝒍𝒐𝒐𝒌𝒆𝒅 𝒔𝒐 𝒍𝒐𝒗𝒆𝒍𝒚 𝒕𝒐𝒅𝒂𝒚. "
  for c in senlet2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  senlet3 = "𝑰 𝒓𝒆𝒂𝒍𝒍𝒚 𝒍𝒊𝒌𝒆𝒅 𝒕𝒉𝒆 𝒘𝒂𝒚 𝒕𝒉𝒂𝒕 𝒚𝒐𝒖 𝒘𝒆𝒓𝒆 𝒘𝒆𝒂𝒓𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒉𝒂𝒊𝒓 𝒊𝒕 𝒍𝒐𝒐𝒌𝒔 𝒔𝒐 𝒑𝒓𝒆𝒕𝒕𝒚 𝒍𝒊𝒌𝒆 𝒕𝒉𝒂𝒕... \n𝒚𝒐𝒖 𝒔𝒉𝒐𝒖𝒍𝒅 𝒘𝒆𝒂𝒓 𝒊𝒕 𝒕𝒉𝒂𝒕 𝒘𝒂𝒚 𝒎𝒐𝒓𝒆 𝒐𝒇𝒕𝒆𝒏, \n𝒂𝒏𝒅 𝒕𝒉𝒆 𝒍𝒊𝒑 𝒈𝒍𝒐𝒔𝒔 𝒚𝒐𝒖 𝒘𝒐𝒓𝒆 𝒔𝒎𝒆𝒍𝒍𝒆𝒅 𝒔𝒐 𝒔𝒘𝒆𝒆𝒕. \n𝑾𝒉𝒂𝒕 𝒌𝒊𝒏𝒅 𝒘𝒂𝒔 𝒊𝒕 𝒂𝒏𝒚𝒘𝒂𝒚? 𝑰 𝒘𝒂𝒏𝒕𝒆𝒅 𝒕𝒐 𝒕𝒂𝒔𝒕𝒆 𝒊𝒕 𝒂𝒏𝒅 𝒇𝒊𝒏𝒅 𝒐𝒖𝒕... \n𝑩𝒖𝒕 𝑰 𝒄𝒐𝒖𝒍𝒅𝒏'𝒕, 𝒅𝒂𝒓𝒍𝒊𝒏𝒈."
  for c in senlet3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  
  senlet4 = "𝑻𝒉𝒆 𝒘𝒂𝒚 𝒕𝒉𝒐𝒔𝒆 𝒃𝒖𝒈𝒔 𝒇𝒍𝒚 𝒂𝒓𝒐𝒖𝒏𝒅 𝒂𝒏𝒅 𝒈𝒂𝒕𝒉𝒆𝒓 𝒂𝒓𝒐𝒖𝒏𝒅 𝒚𝒐𝒖 𝒔𝒐 𝒂𝒏𝒏𝒐𝒚𝒊𝒏𝒈𝒍𝒚... 𝑰 𝒘𝒂𝒏𝒕 𝒕𝒐 𝒄𝒓𝒖𝒔𝒉 𝒕𝒉𝒆𝒎..."
  for c in senlet4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()

  senlet5 = "𝑺𝒐𝒐𝒏 𝒎𝒚 𝑫𝒂𝒓𝒍𝒊𝒏𝒈, 𝑰'𝒍𝒍 𝒃𝒆 𝒂𝒃𝒍𝒆 𝒕𝒐 𝒃𝒆 𝒘𝒊𝒕𝒉 𝒚𝒐𝒖 𝒘𝒊𝒕𝒉𝒐𝒖𝒕 𝒂𝒏𝒚 𝒇𝒍𝒊𝒆𝒔 𝒃𝒖𝒛𝒛𝒊𝒏𝒈 𝒂𝒓𝒐𝒖𝒏𝒅..."
  for c in senlet5:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  print()
  senlet6 = "𝑿𝑶𝑿𝑶"
  for c in senlet6:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(z)
  time.sleep(0.5)
  print()
  TwoDoors()


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
  senCR1 = "𝐄𝐰... 𝐈𝐭 𝐬𝐦𝐞𝐥𝐥𝐬 𝐥𝐢𝐤𝐞 𝐫𝐨𝐭𝐭𝐞𝐧 𝐞𝐠𝐠𝐬 𝐢𝐧 𝐡𝐞𝐫𝐞..."
  for c in senCR1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senCR2 = "𝐁𝐋𝐄𝐆𝐂𝐇... 𝐓𝐡𝐞𝐫𝐞'𝐬 𝐧𝐨𝐭𝐡𝐢𝐧𝐠 𝐡𝐞𝐫𝐞 𝐚𝐧𝐲𝐰𝐚𝐲𝐬..."
  for c in senCR2:
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
  senDR1 = "𝐈 𝐜𝐚𝐧'𝐭 𝐬𝐞𝐞 𝐚𝐧𝐲𝐭𝐡𝐢𝐧𝐠 𝐚𝐭 𝐚𝐥𝐥..."
  for c in senDR1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  Hallway1()
  
def Hallway1():
  print()
  print("You decided to walk through the dark hallway and you stumble upon a dresser...")
  print()
  time.sleep(y)
  print()
  print()
  senHW1 = "𝐏𝐥𝐞𝐚𝐬𝐞 𝐥𝐞𝐭 𝐭𝐡𝐞𝐫𝐞 𝐛𝐞 𝐚 𝐟𝐥𝐚𝐬𝐡𝐥𝐢𝐠𝐡𝐭 𝐨𝐫 𝐬𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠..."
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
    senlet2_1 = "𝐎𝐡 𝐥𝐨𝐨𝐤 𝐚𝐧𝐨𝐭𝐡𝐞𝐫 𝐥𝐞𝐭𝐭𝐞𝐫 𝐚𝐝𝐝𝐫𝐞𝐬𝐬𝐞𝐝 𝐭𝐨 𝐦𝐞, 𝐡𝐨𝐰 𝐰𝐨𝐧𝐝𝐞𝐫𝐟𝐮𝐥..."
    for c in senlet2_1:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(y)
    time.sleep(0.5)
    print()
    print()
    senlet2_2 = "𝑫𝒆𝒂𝒓 𝑯𝒐𝒏𝒆𝒚,"
    for c in senlet2_2:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(z)
    time.sleep(0.5)
    print()
    print()
    senlet2_3 = "𝑾𝒉𝒂𝒕 𝑰 𝒉𝒂𝒗𝒆 𝒕𝒐 𝒔𝒂𝒚 𝒕𝒐 𝒚𝒐𝒖 𝒊𝒔 𝑺𝑶 𝒗𝒆𝒓𝒚 𝒑𝒆𝒓𝒔𝒐𝒏𝒂𝒍, 𝒊𝒕'𝒔 𝒓𝒆𝒂𝒍𝒍𝒚 𝒕𝒉𝒆 𝒌𝒊𝒏𝒅 𝒐𝒇 𝒕𝒉𝒊𝒏𝒈 𝑰 𝒔𝒉𝒐𝒖𝒍𝒅 𝒔𝒂𝒚 𝒕𝒐 𝒚𝒐𝒖 𝒎𝒚𝒔𝒆𝒍𝒇..."
    for c in senlet2_3:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)
    print()
    print()
    senlet2_4 = "𝑩𝒖𝒕 𝑰 𝒄𝒂𝒏'𝒕... I̵̯̣͕̍̌͠ ̸̟͑̄̉J̵̮̟̮̱̆͌͛̏̒͜U̴̡̗̻̙̖͉̘̓̓̄̽̄̍̕S̵̞̙͍̟̲̪͙̩̱͗̉̊́̏̕ͅŤ̶̗̳̤͙͎̮̘̗͎͋̓̐͝͝ͅ ̷̨̲̞͍̪̐̍͊C̷̝̖̼̫̞̖̖̈́̂̽̎͑́́͛À̵̘̭͈͎͉̮̗̅͝N̴̨̧̨̩̻̺̙̎͐̽̅́͐̐̓ͅ'̵̟͍̤̫͔͆̈́T̷̢̜͖͕͚̙͚̮͖͑̽̿̌̆͆͗̚͘͜͝!̷͖͗̕"
    for c in senlet2_4:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    time.sleep(0.2)
    print()
    print()
    senlet2_5 = "𝑰 𝒕𝒓𝒚 𝒂𝒏𝒅 𝑰 𝒕𝒓𝒚 𝒕𝒐 𝒂𝒑𝒑𝒓𝒐𝒂𝒄𝒉 𝒚𝒐𝒖 𝒃𝒖𝒕...𝑰'𝒎 𝒂𝒍𝒘𝒂𝒚𝒔 𝒊𝒏𝒕𝒆𝒓𝒓𝒖𝒑𝒕𝒆𝒅.  \n𝑰𝒕'𝒔 𝒃𝒆𝒄𝒂𝒖𝒔𝒆 𝒐𝒇 𝒂𝒍𝒍 𝒕𝒉𝒐𝒔𝒆 𝒇𝒍𝒊𝒆𝒔 𝒂𝒓𝒐𝒖𝒏𝒅 𝒚𝒐𝒖, 𝒚𝒐𝒖𝒓 𝒔𝒐-𝒄𝒂𝒍𝒍𝒆𝒅 𝒇𝒓𝒊𝒆𝒏𝒅𝒔. \n𝑨𝒏𝒏𝒐𝒚𝒊𝒏𝒈, 𝒃𝒖𝒛𝒛𝒊𝒏𝒈, 𝒃𝒂𝒃𝒃𝒍𝒊𝒏𝒈 𝒍𝒊𝒕𝒕𝒍𝒆 𝒇𝒍𝒊𝒆𝒔. \n𝑰 𝑯𝑨𝑻𝑬 𝒕𝒉𝒂𝒕 𝒚𝒐𝒖'𝒓𝒆 𝑵𝑬𝑽𝑬𝑹 𝒂𝒍𝒐𝒏𝒆,\n𝒕𝒉𝒂𝒕 𝑰 𝒄𝒂𝒏 𝑵𝑬𝑽𝑬𝑹 𝒋𝒖𝒔𝒕 𝒕𝒂𝒍𝒌 𝒕𝒐 𝒚𝒐𝒖! \n𝑺𝒐𝒎𝒆 𝒂𝒓𝒆 𝒎𝒆𝒂𝒏𝒕 𝒕𝒐 𝒃𝒆 𝒔𝒂𝒊𝒅 𝒂𝒍𝒐𝒏𝒆 𝒃𝒖𝒕...𝑻𝑯𝑶𝑺𝑬 𝑭𝑳𝑰𝑬𝑺! \n𝑨𝒍𝒘𝒂𝒚𝒔 𝒃𝒖𝒛𝒛𝒊𝒏𝒈 𝒂𝒓𝒐𝒖𝒏𝒅 𝒚𝒐𝒖!\n𝑺𝒖𝒄𝒉 𝒂𝒏𝒏𝒐𝒚𝒊𝒏𝒈 𝒄𝒓𝒆𝒂𝒕𝒖𝒓𝒆𝒔! \n𝑰 𝒉𝒂𝒅 𝑺𝑼𝑪𝑯 𝒂 𝒘𝒐𝒏𝒅𝒆𝒓𝒇𝒖𝒍 𝒄𝒐𝒏𝒇𝒆𝒔𝒔𝒊𝒐𝒏 𝒂𝒍𝒍 𝒑𝒍𝒂𝒏𝒏𝒆𝒅 𝒃𝒖𝒕 𝒕𝒉𝒐𝒔𝒆 𝒇𝒓𝒊𝒆𝒏𝒅𝒔 𝒐𝒇 𝒚𝒐𝒖𝒓𝒔 𝒓𝒖𝒊𝒏 𝒊𝒕!\n𝑬𝑽𝑬𝑹𝒀! 𝑺𝑰𝑵𝑮𝑳𝑬! 𝑭𝑼𝑪𝑲𝑰𝑵𝑮! 𝑻𝑰𝑴𝑬! \n𝑻𝒉𝒆𝒚 𝒂𝒍𝒘𝒂𝒚𝒔 𝒔𝒂𝒚 𝒕𝒉𝒂𝒕 𝒇𝒍𝒊𝒆𝒔 𝒂𝒓𝒆 𝒂𝒕𝒕𝒓𝒂𝒄𝒕𝒆𝒅 𝒕𝒐 𝒉𝒐𝒏𝒆𝒚 𝒂𝒏𝒅 𝑰 𝒈𝒖𝒆𝒔𝒔 𝒕𝒉𝒂𝒕'𝒔 𝒑𝒓𝒆𝒕𝒕𝒚 𝒕𝒓𝒖𝒆, 𝒉𝒖𝒉? \n𝒀𝒐𝒖 𝒂𝒓𝒆 𝒔𝒐 𝒔𝒘𝒆𝒆𝒕 𝒂𝒏𝒅 𝒍𝒐𝒗𝒆𝒍𝒚, 𝒋𝒖𝒔𝒕 𝒍𝒊𝒌𝒆 𝒉𝒐𝒏𝒆𝒚. \n𝑨𝒏𝒅 𝑰 𝒈𝒖𝒆𝒔𝒔 𝑰 𝒄𝒂𝒏'𝒕 𝒓𝒆𝒂𝒍𝒍𝒚 𝒃𝒍𝒂𝒎𝒆 𝒚𝒐𝒖 𝒇𝒐𝒓 𝒃𝒆𝒊𝒏𝒈 𝒔𝒐 𝒑𝒐𝒑𝒖𝒍𝒂𝒓. 𝒀𝒐𝒖'𝒓𝒆 𝒑𝒓𝒆𝒕𝒕𝒚 𝒂𝒏𝒅 𝒑𝒆𝒓𝒇𝒆𝒄𝒕 𝒂𝒏𝒅 𝑰'𝒎 𝒏𝒐𝒕 𝒕𝒉𝒆 𝒐𝒏𝒍𝒚 𝒐𝒏𝒆 𝒘𝒉𝒐'𝒔 𝒅𝒓𝒂𝒘𝒏 𝒕𝒐 𝒚𝒐𝒖. \n𝑩𝒖𝒕 𝑰 𝑨𝑴 𝒕𝒉𝒆 𝒐𝒏𝒍𝒚 𝒐𝒏𝒆 𝒘𝒉𝒐 𝒅𝒆𝒔𝒆𝒓𝒗𝒆𝒔 𝒚𝒐𝒖!"
    for c in senlet2_5:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)
    print()
    print()
    senlet2_6 = "𝒀𝒐𝒖𝒓 𝒍𝒐𝒗𝒊𝒏𝒈 𝒅𝒂𝒓𝒍𝒊𝒏𝒈, \n \n Y̶̛̛̮̯̲͈̱͖̼̜̝̱͎̱͓̅̊̏̇̈́̽͊̈̿̚͜͝͝ͅυ̴̢̡̨̡̼̗̦̖͎͔͕̫̟͎͒͊̊̈̓̋̓́̀͋̇͌͌̆̕ɿ̶̡̤͖͎̤̭͈͈̥̹͕̬̼͍̈̿́̍̿̆͆̅͛̾͜͝͠͠͝i̵̢̡͉͕̟̞̖̠̠̜̤̗̣͚̊̇̊̃͛̇̋͑̏͌̈͝͝͠"
    for c in senlet2_6:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    time.sleep(0.2)
    print()
    print()
    Drawer1()


def Flashlight():
  senflash1 = "𝐅𝐨𝐫 𝐭𝐡𝐞 𝐥𝐨𝐯𝐞 𝐨𝐟... 𝐅𝐢𝐧𝐚𝐥𝐥𝐲 𝐚 𝐟𝐥𝐚𝐬𝐡𝐥𝐢𝐠𝐡𝐭... 𝐈 𝐡𝐨𝐩𝐞 𝐢𝐭 𝐰𝐨𝐫𝐤𝐬..."
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  Drawer1()


def PictureDr():
  senflash1 = "𝐀𝐧𝐨𝐭𝐡𝐞𝐫 𝐩𝐢𝐜𝐭𝐮𝐫𝐞?..."
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senflash1 = "𝐀𝐧𝐝 𝐢𝐭'𝐬 𝐚 𝐩𝐢𝐜𝐭𝐮𝐫𝐞 𝐨𝐟 𝐦𝐞... 𝐚𝐧𝐝 𝐰𝐡𝐨?..."
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senflash1 = "𝐖𝐡𝐨 𝐢𝐬 𝐡𝐞 𝐚𝐧𝐝 𝐰𝐡𝐲 𝐢𝐬 𝐡𝐞 𝐜𝐫𝐨𝐬𝐬𝐞𝐝 𝐨𝐮𝐭 𝐥𝐢𝐤𝐞 𝐭𝐡𝐚𝐭?..."
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  Hallway1_2()

def Hallway1_2():
  print()
  print("With flashlight in hand you walk more")
  print()
  time.sleep(x)
  print("After some steps you see stairs leading down to the next floor...")
  time.sleep(y)
  print()
  print()
  Hallway2()


def Hallway2():
  print()
  print("After walking down the stairs you arrive at another dark hallway")
  print()
  time.sleep(x)
  print("Along the hallway there are three doors")
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
  senflash1 = "𝐇𝐦𝐦... 𝐓𝐡𝐞𝐫𝐞'𝐬 𝐧𝐨𝐭𝐡𝐢𝐧𝐠 𝐡𝐞𝐫𝐞 𝐛𝐮𝐭 𝐚 𝐜𝐚𝐛𝐢𝐧𝐞𝐭... 𝐀𝐧𝐝 𝐢𝐭'𝐬 𝐥𝐨𝐜𝐤𝐞𝐝..."
  for c in senflash1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  Hallway2()


def doorb():
  sendb1 = "𝐀𝐡𝐡 𝐬𝐡𝐢𝐢𝐢𝐢... 𝐓𝐡𝐞𝐫𝐞 𝐚𝐫𝐞 𝐛𝐫𝐨𝐤𝐞𝐧 𝐩𝐨𝐫𝐭𝐫𝐚𝐢𝐭𝐬 𝐞𝐯𝐞𝐫𝐲𝐰𝐡𝐞𝐫𝐞..."
  for c in sendb1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendb2 = "𝐖𝐚𝐢𝐭... 𝐓𝐡𝐞𝐫𝐞'𝐬 𝐨𝐧𝐞 𝐭𝐡𝐚𝐭'𝐬 𝐧𝐨𝐭 𝐟𝐮𝐥𝐥𝐲 𝐝𝐞𝐬𝐭𝐫𝐨𝐲𝐞𝐝..."
  for c in sendb2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendb3 = "𝐓𝐡𝐢𝐬 𝐤𝐢𝐝 𝐥𝐨𝐨𝐤𝐬 𝐟𝐚𝐦𝐢𝐥𝐢𝐚𝐫... 𝐖𝐡𝐨 𝐭𝐡𝐞 𝐡𝐞𝐥𝐥 𝐢𝐬 𝐡𝐞?..."
  for c in sendb3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendb4 = "𝐓𝐡𝐞𝐫𝐞'𝐬 𝐬𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐢𝐧 𝐭𝐡𝐞 𝐛𝐚𝐜𝐤..."
  for c in sendb4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senb5 = "𝐓𝐡𝐞 𝐛𝐚𝐜𝐤 𝐬𝐚𝐲𝐬..."
  for c in senb5:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senb6 = " ̷-̷-̷-̷-̷, 𝐂𝐨𝐳𝐞𝐫, 𝟎𝟗/𝟏𝟏/𝟐𝟎𝟎𝟕..."
  for c in senb6:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  Hallway2()

def doorc():
  sendc1 = "𝐒𝐡𝐢𝐢𝐢𝐢𝐢... 𝐌𝐨𝐫𝐞 𝐛𝐫𝐨𝐤𝐞𝐧 𝐬𝐭𝐮𝐟𝐟... 𝐒𝐡𝐨𝐮𝐥𝐝'𝐯𝐞 𝐤𝐧𝐨𝐰𝐧..."
  for c in sendc1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendc2 = "𝐀𝐭 𝐥𝐞𝐚𝐬𝐭 𝐭𝐡𝐞𝐫𝐞'𝐬 𝐚 𝐤𝐞𝐲 𝐡𝐞𝐫𝐞..."
  for c in sendc2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendc3 = "𝐈𝐬 𝐭𝐡𝐢𝐬 𝐭𝐡𝐞 𝐤𝐞𝐲 𝐭𝐨 𝐭𝐡𝐞 𝐜𝐚𝐛𝐢𝐧𝐞𝐭 𝐢𝐧 𝐭𝐡𝐞 𝐨𝐭𝐡𝐞𝐫 𝐫𝐨𝐨𝐦?"
  for c in sendc3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendc4 = "𝐈 𝐭𝐡𝐢𝐧𝐤 𝐬𝐨... 𝐎𝐧𝐞 𝐰𝐚𝐲 𝐭𝐨 𝐟𝐢𝐧𝐝 𝐨𝐮𝐭..."
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
  print("After trying to open the cabinet with the key, it finally opened...")
  print()
  time.sleep(x)
  print()
  print()
  sendcb1 = "𝐔𝐄𝐆𝐇... 𝐖𝐡𝐚𝐭'𝐬 𝐭𝐡𝐚𝐭 𝐬𝐦𝐞𝐥𝐥?..."
  for c in sendcb1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendcb2 = "𝐍𝐨... 𝐰𝐚𝐲... 𝐀𝐫𝐞 𝐭𝐡𝐨𝐬𝐞..."
  for c in sendcb2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendcb3 = "𝐓𝐡𝐚𝐭'𝐬 𝐭𝐡𝐞 𝐰𝐚𝐭𝐜𝐡 𝐈 𝐠𝐚𝐯𝐞 𝐉𝐨𝐧𝐚𝐭𝐡𝐚𝐧... \n𝐓𝐡𝐞 𝐧𝐞𝐜𝐤𝐥𝐚𝐜𝐞 𝐈 𝐠𝐢𝐟𝐭𝐞𝐝 𝐭𝐨 𝐑𝐨𝐢... \n𝐄𝐯𝐞𝐧 𝐭𝐡𝐞 𝐞𝐚𝐫𝐫𝐢𝐧𝐠𝐬 𝐈 𝐛𝐨𝐮𝐠𝐡𝐭 𝐟𝐨𝐫 𝐂𝐡𝐫𝐢𝐬'𝐬 𝐛𝐢𝐫𝐭𝐡𝐝𝐚𝐲... \n𝐓𝐡𝐞𝐲'𝐫𝐞 𝐚𝐥𝐥 𝐦𝐲 𝐠𝐢𝐟𝐭𝐬 𝐟𝐨𝐫 𝐦𝐲 𝐞𝐱𝐞𝐬!!!"
  for c in sendcb3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendcb4 = "𝐈 𝐟𝐞𝐞𝐥 𝐬𝐢𝐜𝐤... 𝐈 𝐡𝐚𝐯𝐞𝐧'𝐭 𝐡𝐚𝐝 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐰𝐢𝐭𝐡 𝐭𝐡𝐞𝐦 𝐚𝐭 𝐚𝐥𝐥... 𝐢𝐬 𝐭𝐡𝐢𝐬 𝐭𝐡𝐞 𝐫𝐞𝐚𝐬𝐨𝐧?..."
  for c in sendcb4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  sendcb5 = "𝐈 𝐫𝐞𝐚𝐥𝐥𝐲 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐫𝐮𝐧 𝐚𝐰𝐚𝐲..."
  for c in sendcb5:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  Hallway2_2()


def Hallway2_2():
  print()
  print("Quickly picking up your pace you reached a door leading to the outside world...")
  print()
  time.sleep(x)
  print()
  print()
  senhw21 = "𝐀 𝐝𝐨𝐨𝐫..."
  for c in senhw21:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senhw22 = "𝐂𝐚𝐧 𝐈 𝐟𝐢𝐧𝐚𝐥𝐥𝐲 𝐠𝐨 𝐨𝐮𝐭?..."
  for c in senhw22:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  print("You run frantically torwards the door until...")
  print()
  time.sleep(y)
  print()
  print()
  senhw23 = "𝐅𝐔**𝐈𝐍𝐆 𝐇𝐄𝐋𝐋!!! 𝐈𝐭'𝐬 𝐥𝐨𝐜𝐤𝐞𝐝 𝐟𝐫𝐨𝐦 𝐭𝐡𝐞 𝐨𝐮𝐭𝐬𝐢𝐝𝐞..."
  for c in senhw23:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  print("Will you stay or go back to the stairs?...")
  print()
  time.sleep(y)
  print()
  print()
  stay = ["Stay","Stairs"]
  user = ""
  while user not in stay:
    print("Interact: Stay/Stairs")
    print()
    user = input()
    if user == "Stay":
        Stay()
    elif user == "Stairs":
        Hallway3()   
    else:
        print("Please enter a valid option.")
  time.sleep(y)
  print()
  print()

def Stay():
  print()
  print()
  print("Footsteps can be heard...")
  print()
  time.sleep(x)
  print("Will you hide, or runaway?")
  time.sleep(y)
  print()
  print()
  hor = ["Hide","Runaway"]
  user = ""
  while user not in hor:
    print("Interact: Hide/Runaway")
    print()
    user = input()
    if user == "Hide":
        Hide()
    elif user == "Runaway":
        Run()   
    else:
        print("Please enter a valid option.")
  time.sleep(y)
  print()
  print()


def Hide():
  senhd1 = "𝑶𝒉 𝒎𝒚 𝑫𝒂𝒓𝒍𝒊𝒏𝒈... 𝑾𝒉𝒂𝒕 𝒂𝒓𝒆 𝒚𝒐𝒖 𝒅𝒐𝒊𝒏𝒈 𝒉𝒆𝒓𝒆?..."
  for c in senhd1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senhd2 = "𝑫𝒊𝒅 𝒚𝒐𝒖 𝒑𝒆𝒓𝒉𝒂𝒑𝒔 𝒏𝒐𝒕 𝒍𝒊𝒌𝒆 𝒐𝒖𝒓 𝒏𝒆𝒘 𝒃𝒆𝒅?"
  for c in senhd2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senhd3 = "𝒀𝒐𝒖 𝒔𝒉𝒐𝒖𝒍𝒅𝒏'𝒕 𝒃𝒆 𝒉𝒆𝒓𝒆 𝒎𝒚 𝒍𝒐𝒗𝒆, 𝒄𝒐𝒎𝒆 𝒂𝒏𝒅 𝒍𝒆𝒕'𝒔 𝒈𝒐 𝒃𝒂𝒄𝒌 𝒕𝒐 𝒐𝒖𝒓 𝒓𝒐𝒐𝒎, 𝒔𝒉𝒂𝒍𝒍 𝒘𝒆?"
  for c in senhd3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senhd3 = "𝐓𝐡𝐚𝐭 𝐯𝐨𝐢𝐜𝐞... 𝐈𝐭 𝐜𝐚𝐧'𝐭 𝐛𝐞?..."
  for c in senhd3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  print("...𝗧𝗵𝗲 𝗽𝘀𝘆𝗰𝗵𝗼 𝗹𝘂𝗻𝗮𝘁𝗶𝗰 𝗵𝗮𝘀 𝗳𝗼𝘂𝗻𝗱 𝘆𝗼𝘂...")
  print()
  print("Play Again?")
  play = ["Yes","No"]
  user = ""
  while user not in play:
    print("Interact: Yes/No")
    print()
    user = input()
    if user == "Yes":
        Bedroom()
    elif user == "No":
        print("Thank you for playing") 
    else:
        print("Please enter a valid option.")


def Run():
  senrw1 = "𝑶𝒉 𝒎𝒚 𝒃𝒆𝒍𝒐𝒗𝒆𝒅 𝒓𝒖𝒏𝒏𝒊𝒏𝒈 𝒂𝒘𝒂𝒚 𝒘𝒐𝒏'𝒕 𝒉𝒆𝒍𝒑 𝒚𝒐𝒖... \n 𝑰𝒕'𝒍𝒍 𝒐𝒏𝒍𝒚 𝒎𝒂𝒌𝒆 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔 𝒉𝒖𝒓𝒕 𝒎𝒐𝒓𝒆... \n 𝑫𝒐𝒏'𝒕 𝒓𝒖𝒏 𝒂𝒘𝒂𝒚... \n𝑰 𝒅𝒐𝒏'𝒕 𝒘𝒂𝒏𝒕 𝒕𝒐 𝒉𝒖𝒓𝒕 𝒚𝒐𝒖..."
  for c in senrw1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senrw2 = "𝐒𝐡𝐮𝐭 𝐮𝐩... 𝐈'𝐦 𝐧𝐨𝐭 𝐲𝐨𝐮𝐫 𝐟𝐮𝐜𝐤𝐢𝐧𝐠 𝐛𝐞𝐥𝐨𝐯𝐞𝐝!!!"
  for c in senrw2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  print("...𝗧𝗵𝗲 𝗽𝘀𝘆𝗰𝗵𝗼 𝗹𝘂𝗻𝗮𝘁𝗶𝗰 𝗵𝗮𝘀 𝗰𝗮𝘂𝗴𝗵𝘁 𝘆𝗼𝘂...")
  print()
  print("Play Again?")
  play = ["Yes","No"]
  user = ""
  while user not in play:
    print("Interact: Yes/No")
    print()
    user = input()
    if user == "Yes":
        Bedroom()
    elif user == "No":
        print("Thank you for playing") 
    else:
        print("Please enter a valid option.")


def Hallway3():
  print()
  print()
  print("You went backed to the stairs and went down to the basement...")
  print()
  time.sleep(x)
  print("You stumbled another two sets of room ")
  print()
  time.sleep(y)
  print()
  senrw1 = "𝐓𝐰𝐨 𝐦𝐨𝐫𝐞 𝐫𝐨𝐨𝐦𝐬..."
  for c in senrw1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  rooms = ["Room 1","Room 2"]
  user = ""
  while user not in rooms:
    print("Interact: Room 1/Room 2")
    print()
    user = input()
    if user == "Room 1":
        BRoom1()
    elif user == "Room 2":
        BRoom2()
    else:
        print("Please enter a valid option.")


def BRoom1():
  print()
  print("You walk into the room...")
  print()
  time.sleep(x)
  print("You take a look around...")
  time.sleep(y)
  print()
  senBRo1 = "𝐁𝐋𝐀𝐑𝐆𝐇𝐇𝐇... 𝐅𝐔*𝐊𝐊..."
  for c in senBRo1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senBRo2 = "𝐅𝐮𝐜𝐤𝐢𝐧𝐠 𝐡𝐞𝐥𝐥... 𝐀𝐫𝐞 𝐭𝐡𝐨𝐬𝐞... 𝐃𝐞𝐚𝐝 𝐛𝐨𝐝𝐢𝐞𝐬..."
  for c in senBRo2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senBRo2 = "𝐓𝐡𝐚𝐭'𝐬... \n𝐉𝐨𝐧𝐚𝐭𝐡𝐚𝐧... \n𝐑𝐨𝐢... \n𝐂𝐡𝐫𝐢𝐬... \n𝐧𝐨... \n𝐓𝐡𝐢𝐬 𝐜𝐚𝐧'𝐭 𝐛𝐞..."
  for c in senBRo2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  senBRo3 = "𝐈'𝐦 𝐬𝐨𝐫𝐫𝐲 𝐟𝐨𝐫 𝐚𝐥𝐥 𝐨𝐟 𝐭𝐡𝐢𝐬... 𝐈 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐠𝐞𝐭 𝐨𝐮𝐭 𝐨𝐟 𝐡𝐞𝐫𝐞 𝐪𝐮𝐢𝐜𝐤𝐥𝐲... 𝐖𝐡𝐨 𝐤𝐧𝐨𝐰𝐬 𝐰𝐡𝐚𝐭 𝐭𝐡𝐚𝐭 𝐥𝐮𝐧𝐚𝐭𝐢𝐜 𝐰𝐢𝐥𝐥 𝐝𝐨..."
  for c in senBRo3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  Hallway3()

def BRoom2():
  senBRoo1 = "𝐓𝐡𝐞𝐬𝐞 𝐭𝐡𝐢𝐧𝐠𝐬..."
  for c in senBRoo1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.01)
  time.sleep(0.5)
  print()
  print()
  senBRoo2 = "𝐀 𝐜𝐚𝐧𝐝𝐲 𝐰𝐫𝐚𝐩𝐩𝐞𝐫?... \n𝐀 𝐩𝐞𝐧?... \n𝐓𝐢𝐬𝐮𝐞𝐬?... \n𝐌𝐲 𝐨𝐥𝐝 𝐛𝐫𝐨𝐨𝐜𝐡?..."
  for c in senBRoo2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.01)
  time.sleep(0.5)
  print()
  print()
  senBRoo3 = "𝐓𝐡𝐞𝐬𝐞 𝐚𝐫𝐞 𝐭𝐡𝐞 𝐬𝐭𝐮𝐟𝐟 𝐈 𝐠𝐚𝐯𝐞 𝐚𝐰𝐚𝐲 𝐭𝐨 𝐭𝐡𝐚𝐭 𝐤𝐢𝐝... 𝐘𝐮𝐫—"
  for c in senBRoo3:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.01)
  time.sleep(0.7)
  print()
  print()
  senBRoo4 = "𝒀𝒐𝒖 𝒓𝒆𝒎𝒆𝒎𝒃𝒆𝒓𝒆𝒅 𝒎𝒆... \n𝑰 𝒄𝒂𝒏'𝒕 𝒃𝒆𝒍𝒊𝒆𝒗𝒆 𝒊𝒕... \n𝒀𝒐𝒖 𝒇𝒊𝒏𝒂𝒍𝒍𝒚 𝒓𝒆𝒎𝒆𝒎𝒃𝒆𝒓𝒆𝒅 𝒎𝒆, 𝒅𝒆𝒂𝒓𝒆𝒔𝒕... \n𝑨𝒇𝒕𝒆𝒓 𝒂𝒍𝒍 𝒕𝒉𝒆𝒔𝒆 𝒚𝒆𝒂𝒓𝒔..."
  for c in senBRoo4:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.7)
  print()
  print()
  senBRoo5 = "𝐘𝐨𝐮'𝐫e 𝐭𝐡𝐚𝐭 𝐤𝐢𝐝 𝐭𝐞𝐧 𝐲𝐞𝐚𝐫𝐬 𝐚𝐠𝐨... \n𝐓𝐡𝐞 𝐨𝐧𝐞 𝐰𝐡𝐨 𝐤𝐞𝐩𝐭 𝐜𝐥𝐢𝐧𝐠𝐢𝐧𝐠 𝐨𝐧𝐭𝐨 𝐦𝐞 𝐰𝐡𝐞𝐧 𝐈 𝐬𝐚𝐯𝐞𝐝 𝐡𝐢𝐦... \n𝐅𝐫𝐨𝐦 𝐭𝐡𝐞..."
  for c in senBRoo5:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.7)
  print()
  print()
  senBRoo6 = "𝑻𝒉𝒆 𝒃𝒖𝒍𝒍𝒊𝒆𝒔, 𝒚𝒆𝒔..."
  for c in senBRoo6:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.7)
  print()
  print()
  senBRoo7 = "𝐖𝐇𝐘 𝐃𝐈𝐃 𝐘𝐎𝐔 𝐃𝐎 𝐓𝐇𝐈𝐒???!!!"
  for c in senBRoo7:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.7)
  print()
  print()
  senBRoo8 = "𝑫𝒐𝒏'𝒕 𝒚𝒐𝒖 𝒈𝒆𝒕 𝒊𝒕, 𝒉𝒐𝒏𝒆𝒚? \n𝑻𝒉𝒐𝒔𝒆 𝒇𝒍𝒊𝒆𝒔 𝒂𝒓𝒆𝒏'𝒕 𝒂𝒏𝒚 𝒈𝒐𝒐𝒅 𝒇𝒐𝒓 𝒚𝒐𝒖! \n𝑻𝒉𝒆𝒚 𝒂𝒓𝒆𝒏'𝒕 𝒚𝒐𝒖𝒓 𝒕𝒓𝒖𝒆 𝒍𝒐𝒗𝒆𝒓𝒔! \n𝑻𝒉𝒆𝒚 𝒄𝒐𝒖𝒍𝒅 𝒏𝒆𝒗𝒆𝒓, 𝑬𝑽𝑬𝑹 𝒄𝒂𝒓𝒆 𝒂𝒃𝒐𝒖𝒕 𝒚𝒐𝒖 𝒕𝒉𝒆 𝒘𝒂𝒚 𝑰 𝒅𝒐. \n𝑰 𝒌𝒏𝒐𝒘 𝒕𝒉𝒂𝒕 𝒕𝒉𝒆𝒚'𝒗𝒆 𝒅𝒆𝒄𝒆𝒊𝒗𝒆𝒅 𝒚𝒐𝒖, 𝒚𝒐𝒖'𝒓𝒆 𝒋𝒖𝒔𝒕 𝒕𝒐𝒐 𝒊𝒏𝒏𝒐𝒄𝒆𝒏𝒕 𝒂𝒏𝒅 𝒔𝒘𝒆𝒆𝒕 𝒕𝒐 𝒌𝒏𝒐𝒘 𝒂𝒏𝒚 𝒃𝒆𝒕𝒕𝒆𝒓. \n𝑩𝒖𝒕 𝒕𝒉𝒂𝒕'𝒔 𝒐𝒌𝒂𝒚."
  for c in senBRoo8:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.7)
  print()
  print()
  senBRoo9 = "𝐖𝐇𝐀𝐓 𝐌𝐀𝐊𝐄𝐒 𝐘𝐎𝐔 𝐓𝐇𝐈𝐍𝐊 𝐓𝐇𝐀𝐓 𝐈 𝐁𝐄𝐋𝐎𝐍𝐆 𝐓𝐎 𝐘𝐎𝐔?... 𝐘𝐎𝐔'𝐑𝐄 𝐉𝐔𝐒𝐓 𝐀 𝐋𝐔𝐍𝐀𝐓𝐈𝐂 𝐖𝐇𝐎 𝐂𝐀𝐍'𝐓 𝐆𝐄𝐓 𝐎𝐕𝐄𝐑 𝐇𝐈𝐒 𝐅𝐈𝐑𝐒𝐓 𝐋𝐎𝐕𝐄!!!"
  for c in senBRoo9:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.7)
  print()
  print()
  senBRoo10 = "𝑰 𝒌𝒏𝒆𝒘 𝒊𝒕... 𝒕𝒉𝒂𝒕'𝒔 𝒘𝒉𝒚 𝑰'𝒎 𝒈𝒐𝒊𝒏𝒈 𝒕𝒐 𝒕𝒂𝒌𝒆 𝒄𝒂𝒓𝒆 𝒐𝒇 𝒕𝒉𝒆𝒎, 𝒂𝒍𝒍 𝒐𝒇 𝒕𝒉𝒆𝒎. \n𝑬𝒗𝒆𝒓𝒚. 𝑳𝒂𝒔𝒕. 𝑳𝒊𝒕𝒕𝒍𝒆. 𝑭𝒍𝒚. \n𝑰 𝒋𝒖𝒔𝒕 𝒌𝒏𝒐𝒘 𝒕𝒉𝒂𝒕 𝒐𝒏𝒄𝒆 𝒚𝒐𝒖 𝒌𝒏𝒐𝒘 𝒎𝒆 𝒂 𝒃𝒊𝒕 𝒃𝒆𝒕𝒕𝒆𝒓, \n𝒚𝒐𝒖 𝒘𝒐𝒏'𝒕 𝒄𝒂𝒓𝒆 𝒇𝒐𝒓 𝒕𝒉𝒐𝒔𝒆 𝒂𝒏𝒏𝒐𝒚𝒊𝒏𝒈 𝒍𝒊𝒕𝒕𝒍𝒆 𝒇𝒍𝒊𝒆𝒔 𝒂𝒏𝒚𝒎𝒐𝒓𝒆. \n𝑰'𝒍𝒍 𝒔𝒘𝒂𝒕 𝒕𝒉𝒆𝒎 𝒇𝒂𝒓, 𝒇𝒂𝒓 𝒂𝒘𝒂𝒚 𝒂𝒏𝒅 𝒘𝒆 𝒄𝒂𝒏 𝒃𝒆 𝒉𝒂𝒑𝒑𝒚, 𝒎𝒆 𝒂𝒏𝒅 𝒎𝒚 𝒉𝒐𝒏𝒆𝒚! \n𝑨𝒏𝒅 𝒊𝒇 𝒕𝒉𝒐𝒔𝒆 𝒉𝒐𝒓𝒓𝒊𝒃𝒍𝒆 𝒍𝒊𝒕𝒕𝒍𝒆 𝒇𝒍𝒊𝒆𝒔 𝒑𝒆𝒓𝒔𝒊𝒔𝒕...𝒘𝒆𝒍𝒍, 𝑰 𝒄𝒂𝒏 𝒉𝒂𝒏𝒅𝒍𝒆 𝒕𝒉𝒆𝒎 𝒎𝒚𝒔𝒆𝒍𝒇. \n𝑰 𝒌𝒏𝒐𝒘 𝒕𝒉𝒂𝒕 𝒚𝒐𝒖 𝒎𝒂𝒚 𝒃𝒆 𝒂 𝒍𝒊𝒕𝒕𝒍𝒆 𝒖𝒑𝒔𝒆𝒕 𝒂𝒕 𝒇𝒊𝒓𝒔𝒕 𝒃𝒖𝒕 𝒚𝒐𝒖 𝒅𝒐𝒏'𝒕 𝒉𝒂𝒗𝒆 𝒕𝒐 𝒘𝒐𝒓𝒓𝒚. \n𝑴𝒚 𝒍𝒐𝒗𝒆 𝒘𝒊𝒍𝒍 𝒎𝒂𝒌𝒆 𝒚𝒐𝒖 𝒇𝒆𝒆𝒍 𝒂𝒍𝒍 𝒃𝒆𝒕𝒕𝒆𝒓! \n𝑾𝒊𝒕𝒉 𝒎𝒆 𝒂𝒕 𝒚𝒐𝒖𝒓 𝒔𝒊𝒅𝒆, 𝒚𝒐𝒖'𝒍𝒍 𝒏𝒆𝒗𝒆𝒓, 𝒆𝒗𝒆𝒓 𝒃𝒆 𝒍𝒐𝒏𝒆𝒍𝒚 𝒐𝒓 𝒔𝒂𝒅 𝒂𝒕 𝒂𝒍𝒍! \n𝒀𝒐𝒖'𝒍𝒍 𝒃𝒆 𝑴𝑼𝑪𝑯 𝒉𝒂𝒑𝒑𝒊𝒆𝒓 𝒘𝒊𝒕𝒉𝒐𝒖𝒕 𝒕𝒉𝒆𝒎, 𝒑𝒓𝒐𝒎𝒊𝒔𝒆."
  for c in senBRoo10:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.05)
  time.sleep(0.7)
  print()
  print()
  Finale()


def Finale():
  print("You picked up a nearby object...")
  print()
  time.sleep(x)
  print()
  senf1 = "𝑫𝒐𝒏'𝒕 𝒚𝒐𝒖 𝒅𝒂𝒓𝒆 𝒅𝒐 𝒘𝒉𝒂𝒕 𝑰 𝒕𝒉𝒊𝒏𝒌 𝒚𝒐𝒖'𝒓𝒆 𝒈𝒐𝒊𝒏𝒈 𝒕𝒐 𝒅𝒐... 𝒐𝒌𝒂𝒚?... 𝒅𝒐𝒍𝒍?..."
  for c in senf1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.7)
  act = ["Throw","No"]
  user = ""
  while user not in act:
    print("Interact: Throw/No")
    print()
    user = input()
    if user == "Throw":
        Hurt()
    elif user == "No":
        Lovely()
    else:
        print("Please enter a valid option.")


def Hurt():
  print()
  print()
  senH1 = "𝑭𝒖𝒄𝒌... \n𝑨𝒍𝒕𝒉𝒐𝒖𝒈𝒉 𝑰 𝒅𝒐 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖𝒓 𝒇𝒆𝒊𝒔𝒕𝒊𝒏𝒆𝒔𝒔... \n𝑻𝒉𝒊𝒔 𝒔𝒉𝒊𝒕 𝒈𝒐𝒕 𝒕𝒐 𝒔𝒕𝒐𝒑... \n𝑵𝑶𝑾 𝑪𝑶𝑴𝑬 𝑯𝑬𝑹𝑬!!!"
  for c in senH1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.7)
  print()
  print()
  print("Run away...")
  print()
  time.sleep(x)
  runn = ["Run","Stay"]
  user = ""
  while user not in runn:
    print("Interact: Run/Stay")
    print()
    user = input()
    if user == "Run":
        runs()
    elif user == "Stay":
        deds()
    else:
        print("Please enter a valid option.")


def Lovely():
  print()
  print()
  senl1 = "𝑮𝒐𝒐𝒅 𝒈𝒊𝒓𝒍... \n𝑳𝒆𝒕'𝒔 𝒋𝒖𝒔𝒕 𝒈𝒐 𝒃𝒂𝒄𝒌 𝒕𝒐 𝒐𝒖𝒓 𝒓𝒐𝒐𝒎 𝒂𝒏𝒅 𝒃𝒆 𝒂𝒍𝒍 𝒄𝒖𝒅𝒅𝒍𝒚 𝒐𝒌𝒂𝒚?... 𝒉𝒎𝒎?..."
  for c in senl1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.7)
  print()
  print()
  print("---𝗧𝗵𝗲 𝗹𝘂𝗻𝗮𝘁𝗶𝗰 𝗽𝘀𝘆𝗰𝗵𝗼 𝗯𝗿𝗼𝘂𝗴𝗵𝘁 𝘆𝗼𝘂 𝗯𝗮𝗰𝗸 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗿𝗼𝗼𝗺---")
  print()
  print()
  print("Play Again?")
  play = ["Yes","No"]
  user = ""
  while user not in play:
    print("Interact: Yes/No")
    print()
    user = input()
    if user == "Yes":
        Bedroom()
        print("okie") 
    elif user == "No":
        print("Thank you for playing") 
    else:
        print("Please enter a valid option.")


def runs():
  print()
  print()
  senr1 = "𝒀𝒐𝒖 𝒓𝒖𝒏 𝒔𝒐 𝒒𝒖𝒊𝒄𝒌𝒍𝒚 𝒍𝒊𝒌𝒆 𝒂 𝒃𝒖𝒏𝒏𝒚, 𝒃𝒖𝒏𝒏𝒚..."
  for c in senr1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.7)
  print()
  print()
  print("You found the exit door...")
  print()
  time.sleep(x)
  print()
  print("The door is locked and needs a pin code...")
  print()
  time.sleep(x)
  print()
  print("You can only try for three times...")
  print()
  print()
  time.sleep(y)
  Code = "071109"
  count = 0
  countlimit = 3
  while count < countlimit:
    count += 1
    try:
      print("Type the Six- Digit Code:")
      pin = input()
      if pin == Code:
          GoodEnd()
          break
      elif pin != Code:
        print()
        print("Wrong")    
    except ValueError:
        print("Only numbers are allowed")
  else:
    count = countlimit
    BadEnd()


def deds():
  print()
  print()
  send1 = "𝑾𝒉𝒚 𝒅𝒊𝒅 𝒚𝒐𝒖 𝒅𝒐 𝒕𝒉𝒂𝒕 𝒉𝒐𝒏𝒆𝒚?... Hmm?... \n𝑰 𝒐𝒏𝒍𝒚 𝒘𝒂𝒏𝒕 𝒘𝒉𝒂𝒕'𝒔 𝒃𝒆𝒔𝒕𝒔 𝒇𝒐𝒓 𝒚𝒐𝒖... "
  for c in send1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.7)
  print()
  print()
  send2 = "W̴̧̘̩͎̺̖͚̥̍̿̆H̷̱͇͚̱̱̙͑̊̐͒Y̸̡̨̖̝̙̾̒ ̷̞̣̤͚̭̋͋̄͘͝ͅC̷̯̼̩̭̏̃̀͑̊A̶͔̰̬̰̿̉͋̓̓̿͛̍͘͝Ṋ̵̗̲͚͓̦̠͍̍͐͋̊̂̒̾̊̾̌'̴̡̯͚̱͖̓̀͌̾̔̆̽͗͝͠Ţ̴̘̪̻̗͇͓̯͑ ̸̣̖̽Y̶̬̠̯̓́̇̉̌Ö̸̡͈͉͉́̐͛̋͠U̸͎̣̤̽͝ ̴͖͍̱̝͇͚͇͖̓͗̀̊̌̎͛͋̅͠U̴̢͓͓̥͛̉̂N̶̯̞̘̑̑̔̈́̕̚D̸̙͇̓̔̓̂̈́̆͘͝E̷̺̜̤͔̗̗̗̲͓̐̒͛̅͊͗R̴̛͋͜S̸̗̦̋͐͌T̷̢̢͓̖̙̮͘A̶̼̮̪̿N̶̪͋͌͒̊͛̏̃Ḋ̶̦ ̴̙̥̏̚͠T̶̨̨̢̩̬̩͖̏̎̅H̵̡̞͎̯͈͕͈̗̭͑̂̍̀͠A̶̧̦̭̼̞̖̩̍̓̒̀͑̓̉̊T̷̗̪̟̹͕̺̫͉͎̯̓?̵̩͕̻̮̱̠̇!̴̥̺͉͚̱͖̠̻͒̈́̎̿̽͠.̵̻͍̼͑̀͑̅̐͛͊̈́͘.̵̢̬̫̻͈̖̗̤̒̿́̇̿͋̅ͅ.̶̙͔͚̞͓͔̭̽̏̋̋́̕͠ \n \n \n𝑾𝒆𝒍𝒍, 𝒘𝒆 𝒉𝒂𝒗𝒆 𝒆𝒏𝒐𝒖𝒈𝒉 𝒕𝒊𝒎𝒆 𝒕𝒐 𝒎𝒂𝒌𝒆 𝒚𝒐𝒖 𝒖𝒏𝒅𝒆𝒓𝒔𝒕𝒂𝒏𝒅 𝒉𝒐𝒘 𝒎𝒖𝒄𝒉 𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖..."
  for c in send2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.1)
  time.sleep(0.5)
  print()
  print()
  print("---𝗧𝗵𝗲 𝗹𝘂𝗻𝗮𝘁𝗶𝗰 𝗽𝘀𝘆𝗰𝗵𝗼 𝗱𝗿𝗮𝗴𝘀 𝘆𝗼𝘂 𝗯𝘆 𝘆𝗼𝘂𝗿 𝗵𝗮𝗶𝗿 𝗯𝗮𝗰𝗸 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗿𝗼𝗼𝗺---")
  print()
  print()
  print("Play Again?")
  play = ["Yes","No"]
  user = ""
  while user not in play:
    print("Interact: Yes/No")
    print()
    user = input()
    if user == "Yes":
        Bedroom()
        print("okie") 
    elif user == "No":
        print("Thank you for playing") 
    else:
        print("Please enter a valid option.")


def GoodEnd():
  print()
  print()
  print("The pin code you entered was correct...")
  print()
  time.sleep(x)
  print()
  print("You are finally out of that house...")
  print()
  time.sleep(y)
  print()
  senge1 = "𝐈'𝐦 𝐟𝐢𝐧𝐚𝐥𝐥𝐲 𝐨𝐮𝐭... \n 𝐈 𝐬𝐭𝐢𝐥𝐥 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐫𝐮𝐧 𝐚𝐰𝐚𝐲... "
  for c in senge1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  print("As you walk futher more you see a car passing by...")
  print()
  time.sleep(x)
  print()
  print("You stopped the car...")
  print()
  time.sleep(y)
  print()
  senge2 = "𝐏𝐥𝐞𝐚𝐬𝐞 𝐡𝐞𝐥𝐩 𝐦𝐞... \n𝐏𝐥𝐞𝐚𝐬𝐞..."
  for c in senge2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.5)
  print()
  print()
  print("The driver, pitying you, allowed you inside her car... \nThe car drove off the distance leaving your anxieties behind...")
  print()
  print()
  print("------------𝓣𝓱𝓮 𝓔𝓷𝓭-----------")
  print("---𝓣𝓱𝓪𝓷𝓴 𝔂𝓸𝓾 𝓯𝓸𝓻 𝓟𝓵𝓪𝔂𝓲𝓷𝓰---")
  print()
  print()
  print("Play Again?")
  play = ["Yes","No"]
  user = ""
  while user not in play:
    print("Interact: Yes/No")
    print()
    user = input()
    if user == "Yes":
        Bedroom()
        print("okie") 
    elif user == "No":
        print("Thank you for playing") 
    else:
        print("Please enter a valid option.")


def BadEnd():
  print()
  print()
  senbe1 = "𝑳𝒆𝒂𝒗𝒊𝒏𝒈 𝒎𝒆 𝒂𝒍𝒍 𝒂𝒍𝒐𝒏𝒆 𝒍𝒊𝒌𝒆 𝒕𝒉𝒂𝒕... \n𝑻𝒉𝒂𝒕'𝒔 𝒏𝒐𝒕 𝒇𝒂𝒊𝒓 𝒅𝒂𝒓𝒍𝒊𝒏𝒈..."
  for c in senbe1:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(y)
  time.sleep(0.7)
  print()
  print()
  senbe2 = "W̴͍̜͔͉̼̣͚͗̐͒̒̂͆͑͌̕͜͝Ĥ̶̢͖͙͎̥ͅǍ̵̡͉͖̟͎̬̜͖͊̕ͅT̶̠̬͇̣̼͇̈͐̑̄̑̐̓͂̀ ̶̝͂̂͛̓̀̆̎M̴͕͔̰̭̹̳̺̜̐̒̓̚͝A̸̹͍̤̼̋̍̂͆̏̐́́͋K̵̡̨͈̲̫͉͙̬͂͋͋̉Ě̴̹̰̹̟̒̈Š̷̤̱̥̭̆͝͝ ̸͈̹̘̪̗̳͚̃͛Ẏ̴̫̭̰͈̘͚̪̄͒̎̈̈́̚̕Ȏ̶̧͙͔͓̽̊̚Ṷ̶̹̗̲͖͓͎̾ ̴̨̙̻͔̙̖̳̝̽̋̀͋̕T̸̨̞͉̱̖̪̠̦͇̈́̍̾̄͘̚H̷̻͙͖̔̃I̴̡̛̥̖͕͙̞͗̑̏̂͒̓N̶̡̘̖͕̜̣̣̖̓͝K̶̗̹̼͉̳̘̥̞̹̩͆̓̚ ̷̹͚̉̈́̎́̃̏͠Y̴̨̯͉̤͓͉̎̌̐̚͜Ö̵̗̖̞͔̺͖̣̙̱͖́̈́̔̈́́͐́̚͠Ụ̵̮̦̊̑̓͘ͅ ̶̧̤̤͔̻͔̗̎͂́̓̿̾͗͋͋̽C̸͈͕͖̩̺͖͎̦͉̓̈̊̃̀̽̐́̅̚͜Ȃ̶̡̬̹̐͐̇̋̕͝N̸̢̢͔̘͉͕̿̏̿́̂͒ͅ ̸̯̱̽͐̓̽̒Ḷ̷͈͎̼̾͂̎̆͛Ȩ̴̤̅̍̑͗͋̍Ȁ̴̪͚̞̲̫̗̯͊̓͒ͅV̶̤͕̮͊́̂͑̾̈͛͘̚͠E̵̟̺͈̒̾̄̀̔̔ ̸̨̝̰͕̘̝̖̮̳͆́̈́̀͌͆ͅḾ̶̨͓̠͚̗͎͈̳̟̀̏E̸̩̜͐̑̓̄̍\n \n \n𝑰'𝒍𝒍 𝒋𝒖𝒔𝒕 𝒎𝒂𝒌𝒆 𝒊𝒕 𝒔𝒐 𝒕𝒉𝒂𝒕 𝒚𝒐𝒖 𝒄𝒂𝒏 𝒏𝒆𝒗𝒆𝒓 𝒍𝒆𝒂𝒗𝒆 𝒎𝒆 𝒂𝒈𝒂𝒊𝒏..."
  for c in senbe2:
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(0.1)
  time.sleep(0.5)
  print()
  print()
  print("---𝗧𝗵𝗲 𝗹𝘂𝗻𝗮𝘁𝗶𝗰 𝗽𝘀𝘆𝗰𝗵𝗼 𝗰𝗵𝗮𝗶𝗻𝘀 𝘆𝗼𝘂 𝗶𝗻𝘁𝗼 𝘆𝗼𝘂𝗿 𝗿𝗼𝗼𝗺---")
  print()
  print()
  print("Play Again?")
  play = ["Yes","No"]
  user = ""
  while user not in play:
    print("Interact: Yes/No")
    print()
    user = input()
    if user == "Yes":
        Bedroom()
        print("okie") 
    elif user == "No":
        print("Thank you for playing") 
    else:
        print("Please enter a valid option.")


print()
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("꧁༺ 𝓛𝓸𝓿𝓮 𝓜𝓮 𝓝𝓸𝓽'𝓼 ༻꧂")
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print()
print("𝕊𝕥𝕒𝕣𝕥 𝔾𝕒𝕞𝕖")
print("Yes/No")
start = input()
if start == "no" or start == "No" or start == "NO":
    print()
    print("Alright...")
    time.sleep(3)
elif start == "yes" or start == "Yes" or start == "YES":
    Bedroom()
