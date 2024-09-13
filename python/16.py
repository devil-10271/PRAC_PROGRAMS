age = int(input('enter the age : '))

match age:
    case 18:
        print('\neligible for voteing')
    
    case _ if(age >= 18):
        print('\nyou are eligible for voting')
    case _ if(age <= 18):
        print(f'\ncome after {18-age} years for voteing')