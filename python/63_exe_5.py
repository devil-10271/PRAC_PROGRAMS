import random

user_name=input("Enter your name : ")
print(f"Hello, {user_name}. I am computer lets play game.\n")

com_sco=0
user_sco=0


def retu(ua,):
    com=random.randint(1,3)
    if(ua==5):
        return 0
    elif(ua==4):
        return 1
    else:
        if(ua==com):
            print(f'{user_name} : Stone VS Computer : Stone\n !!!!! tie !!!!!\n' if ua==1 else '',f'{user_name} : Paper VS Computer : Paper\n !!!!! tie !!!!!\n' if ua==2 else '',f'{user_name} : Seisor VS Computer : Seisor\n !!!!! tie !!!!!\n' if ua==3 else '')
            return 7
        elif(ua==1 and com==2):
            print(f'{user_name} : Stone VS Computer : Paper\n !!!!! Computer Win !!!!!\n')
            return 10
        elif(ua==2 and com==3):
            print(f'{user_name} : Paper VS Computer : Seisor\n !!!!! Computer Win !!!!!\n')
            return 10
        elif(ua==3 and com==1):
            print(f'{user_name} : Seisor VS Computer : Stone\n !!!!! Computer Win !!!!!\n')
            return 10
        # user win condition
        elif(ua==1 and com==3):
            print(f'{user_name} : Stone VS Computer : Seisor\n !!!!! {user_name} Win !!!!!\n')
            return 9
        elif(ua==2 and com==1):
            print(f'{user_name} : Paper VS Computer : Stone\n !!!!! {user_name} Win !!!!!\n')
            return 9
        elif(ua==3 and com==2):
            print(f'{user_name} : Seisor VS Computer : Paper\n !!!!! {user_name} Win !!!!!\n')
            return 9
    

while True:
    user_ans=int(input(f"""Enter the number given below:
        1-----> Stone
        2-----> Paper
        3-----> Seisor
        4-----> Display Score
        5-----> Quit & Display Score 
        
        >>> """))
    print()
    a=retu(user_ans)
    match a:
        case 0:
            print(f"{user_name} : {user_sco}\nComputer : {com_sco}\n\n")
            break
        case 1:
            print(f'{user_name} : {user_sco}\nComputer : {com_sco}\n\n')
        case 7:
            pass
        case 9:
            user_sco+=1
        case 10:
            com_sco+=1
        case _:
            print(' !!!!!!!!!!!!!!!!     errror   !!!!!!!!!!!!!!!!')

print(f"{user_name} : {user_sco}\nComputer : {com_sco}")