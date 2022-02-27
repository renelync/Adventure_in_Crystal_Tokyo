print('''
                       _.._
                     .' .-'`
                    /  /
                    |  |
                    \  '.___.;
             jgs     '._  _.'
                        ``
                       .|        ,       +
             *         | |      ((             *
                       |'|       `    ._____
         +     ___    |  |   *        |.   |' .---"|
       _    .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
print("Welcome to Crystal Tokyo.")
print("Your mission, should you choose to accept it, is to find the Moon Princess before the collapse of the city!.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input('You\'ve got to decide which way to go first. Type "left" or "right."\n').lower()
if choice1 == "left":
  choice2 = input('Along this path, you find yourself standing on a frozen lake, and can see three buildings across the lake. Type "wait" to wait for the Sailor Scouts to teleport you. Type "walk" to try to walk across.\n').lower()
  if choice2 == "wait": 
    choice3 = input('With the the help of the Sailor Scouts, you arrive at the three buildings safely. You know the Moon Princess has to be in one of them, but each one has a different colored door. One red, one yellow, and one blue. Which color do you choose?\n').lower()
    if choice3 == "blue":
      print("You\'ve entered a building full of sweets! But, no Moon Princess. Game over!")
    elif choice3 == "red":
      print("You\'ve entered a building filled with fun arcade games...But, no Moon Princess. Game over!")
    elif choice3 == "yellow":
      print("You\'ve found the Moon Princess! She calls upon the power of her Silver Crystal to save the city from collasping! Hooray!")
    else:
      print("Sorry, you've chosen a non-existent color, and the ice beneath your feet has melted inexplicably! Game over.")
  else:
    print("On your first step, the ice melted and you fell into the freezing lake. Game over!")
else:
  print("Unfortunately, you\'ve fallen over a cliff! Game over!")
 