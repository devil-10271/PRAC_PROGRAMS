questions=[
    [ '1. What is National bird of  India ?',
      '1-->Peacock', '2-->Pegion', '3-->Crow', '4-->Saparrow'],

    [ '2. Which language is used fo make a website ?',
      '1-->C', '2-->Python', '3-->HTML', '4-->SQL'],

    [ '3. Which are escape sequence characters?',
      '1-->#', '2-->print()', '3-->\\n', '4-->def'],

    [ '4. Which is full form of CPU ? ',
      '1-->Control Process Unit', '2-->Central Process Unit', '3-->Central Program Unit', '4-->Central Processing Unit'],
    
    [ '1. Which is keyword is used to make a funtion in python ?',
      '1-->Function', '2-->def', '3-->Define', '4-->Def'],
    ]

answers={1:1,
         2:3,
         3:3,
         4:4,
         5:2,}

print('\n')

prices=[1000,2000,30000,400000,500000]
acc=0

for i in range(len(questions)):
    print(f'!!!!! This questions for {prices[i]} Ru. !!!!!')
    print(questions[i][0])
    print(f'''\t{questions[i][1]}\t{questions[i][2]}
    \t{questions[i][3]}\t{questions[i][4]}\
    ''')
    ans=input(f'\b\t(give answer):'.capitalize())


    if int(ans) == answers[i+1] :
        print(f'Correct answer you won {prices[i]}.\n'.capitalize())
        acc=prices[i]
    else:
        print(f'Sorry you can lose the Game.')
        break

print(f'\nYour amount is {acc}')
