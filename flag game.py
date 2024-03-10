print('In this game there are 21 flags and the player who picks up last flag(s) will be the winner of the game')
start_1 = input('if you want to start the game press 1 : ')
x=21
if int(start_1) == 1:
    who = 'me'
    if who == 'me':
        while True:
            first = input('how many flags you want to take? ')
            if int(first)<0 or int(first)>3:
                print('please select at least 1 and at most 3 flags')
            else:
                break
            
        pc1 = x - 17 - int(first)
        x = x - pc1 - int(first)
        print('I played ', pc1, ' remaining: ', x)
        while True:
            second = input('how many flags do you want to take? ')
            if int(second)<0 or int(second)>3:
                print('please select at least 1 and at most 3 flags')
            else:
                break
        
        pc2 = x - 13 - int(second)
        x = x - pc2 - int(second)
        print('I played ', pc2, 'remaining: ', x)

        while True:
            third = input('how many flags do you want to take? ')
            if int(third)<0 or int(third)>3:
                print('please select at least 1 and at most 3 flags')
            else:
                break
        
        pc3 = x - 9 - int(third)
        x = x - pc3 - int(third)
        print('I played ', pc3, 'remaining: ', x)

        
        while True:
            fourth = input('how many flags do you want to take? ')
            if int(fourth)<0 or int(fourth)>3:
                print('please select at least 1 and at most 3 flags')
            else:
                break
        
        pc4 = x - 5 - int(fourth)
        x = x - pc4 - int(fourth)
        print('I played ', pc4, 'remaining: ', x)

        while True:
            fifth = input('how many flags do you want to take? ')
            if int(fifth)<0 or int(fifth)>3:
                print('please select at least 1 and at most 3 flags')
            else:
                break

        pc5 = x - int(fifth)
        x = x - pc5 - int(fifth)
        print('I played ', pc5, 'remaining:', x, ' So, I win!')