import os
import json

print('*'*5,'English Dictionary App','*'*5)

def opt1():
    word = input('Enter the word: ')
    meaning = input('Enter the meaning: ')
    if os.path.isfile('words1.txt'):
        f = open('words1.txt','r')
        temp = json.load(f) 
        temp[word] = meaning 
        f.close()

        f = open('words1.txt','w')
        json.dump(temp,f) 
        f.close()
    else:
        f = open('words1.txt','w')
        dict1 = {word:meaning}
        json.dump(dict1,f)
        f.close()
        
def opt2():
    with open('words1.txt') as f:
        x = json.load(f)
        word = input('Enter a word to find its meaning : ')
        for i in x:
            if word in x:
                print ('The synonym of',word,'is',x[word])
                break
            else:
                print('This dictionary does not have an entry for',word)
                break

                
def opt3():
    y = input('Enter a word of which you want to update the meaning : ')
    z = input('Enter the meaning of the word : ')
    with open('words1.txt') as f:
        x = json.load(f)
        xcopy = {**x}
        for i in xcopy:
            if y not in x:
                print("Error: The entered word doesn't exist in the dictionary. Please try again.")
                break
        else:
            x[y] = z
            print('The updated meaning of',y,'is',z)                
            print(x)
    f = open('words1.txt','w')
    json.dump(x,f)
    f.close()

def opt4():
    print('Thank for choosing us!\n Exiting now...')
    exit()
    
def mainmenu():

    print('\nMain Menu\n')


    print('1. Add a new word\n')


    print('2. Find the meaning\n')


    print('3. Update a word\n')


    print('4. Exit\n')


    x = int(input('Enter a choice: '))

    if x == 1:
        opt1()
        mainmenu()
    elif x == 2:
        opt2()
        mainmenu()
    elif x == 3:
        opt3()
        mainmenu()
    else:
        opt4()
    
mainmenu()
