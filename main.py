print('''

          ___
        //\\\\\\         `    \`..(@)      '
       :     \\\\          (@)(@) / /(@)       ,
       \ ~L~ )\\\\    \ \    '\(__``',..   '
       /\_~ / ||||     \  ,  |  ~~~--/__       `
      ////| |////            //     / ^\\\\
     ||||^    ~~~~~~--------~/    / x)  //
     /  ( (    _____---~~~~~\|   <      @)   SPLAT!
    (  )|      /        /   /    /(     |
     \^\ \____/        /    \   /  ~~~\ \ _        _  __
      \ \/    \              \ |\\|)   |~~ ~~\_  /^\/^\ \
       ))      )         '    ~ \__/\  / /    \ \|     | |
        |      |       `     ,     \ \/ /-      \ \   / /
        |______|                    \  /  \      \ /-/ /
         | || |        ,          `  ~~    /~~~~~~)`--''
         ( || |                 '        /   /   /
          \ | |         ,               <   <   <
           \| /                     ,    \ __\\__\
           /_^||                        /~___|~___|                W<

''')
print("Welcome to Date or Pop the balloon.")
print("Your mission is to impress me.") 

Doors = input('You are at a party, and you see two doors. One is Yellow and the other is Green. Which one do you choose? Type "Yellow" or "Green": \n').lower()

if Doors == "yellow":
    lovelanguage = input('You walk into a yellow room, and you see five love notes. One says "Time", the other says "Service", another says "Affirmation", the next says "Gifts", and the last says "Touch". Type which one you want to read: \n').lower()

    if lovelanguage == "time" or lovelanguage == "touch" or lovelanguage == "affirmation":
        invitation = input('You read the love note and it is an invitation to a date with Ashley. Do you accept? Type "Yes" or "No": \n').lower()

        if invitation == "yes":
            print("You go on a date with Ashley, get married, and live happily ever after. YOU WIN!")
        else:
            print("Ashley pops your balloon. GAME OVER!")

    elif lovelanguage == "service" or lovelanguage == "gifts":
        print("You read the love note but Ashley is not impressed. So you pop the balloon. GAME OVER.")

    else:
        print("Invalid choice.")

else:
    print("You've walked into a green room, and you see a balloon. You pop it and it explodes. Tuh tuh tuh! GAME OVER.")


