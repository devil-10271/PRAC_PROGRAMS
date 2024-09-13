print(f'hello'.capitalize())

name=input(f'what is Your name : '.capitalize())
amount=0
game=f'KBC'

print(f'Hello {name} well come to {game} .\n You have {amount} amount'.capitalize(),'\n')
request=f'!!! Please enter in number !!!'.capitalize()

# ouestion 1
one=int(input(f'''
          This question is for 1,000 rupees
1.) Who is the prime minister of India?
    1 ---> Naraendra Modi
    2 ---> Rahul Gandhi
    3 ---> Sonia Gandhi
    4 ---> abz          
            {request}
:'''))
match one:
    case 1 :
        print(f'Correct answer you won 1000')
        amount+=1000
        print("amount = ",amount)
    case _ :
        print('You lose in Game')
        print('you won no thing. .')


# question 2
two=int(input(f'''
          This question is for 10,000 rupees
1.) Which is the national bird of India?
    1 ---> Peacock
    2 ---> Piegion
    3 ---> Dove
    4 ---> Crow         
            {request}
:'''))

match two:
    case 1 :
        print(f'Correct answer you won 10,000')
        amount+=10000
        print("amount = ",amount)
    case _ :
        print('You lose in Game')
        print('you won no thing. .')


# question 3
three=int(input(f'''
          This question is for 1,00,000 rupees
1.) Which is national game of India ?
    1 ---> hockey
    2 ---> Cricket
    3 ---> Carrom
    4 ---> Ice Hockey       
            {request}
:'''))

match three:
    case 1 :
        print(f'Correct answer you won 1,00,000')
        amount+=100000
        print("amount = ",amount)
    case _ :
        print('You lose in Game')
        print('you won no thing. .')


print(f'\n\nYou won {amount} in this game'.center(100))