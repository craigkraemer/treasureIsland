print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
path = input("\n\nWalking a path in an ancient forest, the path splits. Do you choose the left or the right? Type left or right.\n").lower()
if path == "left":
   river = input("\nYou are now at the river. Do you wait for the boat or swim? Type wait or swim.\n").lower()
else:
   print(f"\nThere is a huge golden statue ahead. YOU HAVE FOUND IT, THE TREASURE! You reach out for it.\nWhen you touch it, a trap door opens from under, and you fall 50 feet to your death.\nYou lost, game over.")
   exit()
if river == "wait":
   door = input("\nAfter a long journey by boat you come upon three doors.\nDo you choose the left, the right, or the front door? Type left, right, or front.\n").lower()
else:
   print(f"\nYou started stretching, and warming up. Carefully eased into the river.\nStarted to swim with confidence, then the current got strong. But you cleverly got out of the under toe.\nYou are 40 feet from the bank of the opposite shore. Then your legs cramp, and you drowned to your death.\nYou lost, game over.")
   exit()
if door == "front":
   print(f"\nYou have found the treasure, and you have won the game.")
else:
   print(f"\nYou got attacked by a pack of wild wofves. You lost, game over.")