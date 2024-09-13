import time as a

b=a.strftime('%H:%M:%S')

if(b>='07:00:00' and b<='10:00:00'):
    print('Hello Good Morning')
elif(b>='10:00:00' and b<='12:00:00'):
    print("have a nice day")
elif(b>='12:00:00' and b<='14:00:00'):
    print("good afternoon")
elif(b>='14:00:00' and b<='19:00:00'):
    print("are you tired")
elif(b>='19:00:00' and b<='21:00:00'):
    print("are you hungry")
elif(b>='21:00:00' and b<='00:00:00'):
    print("let time sleep")
elif(b>='00:00:00' and b<='07:00:00'):
    print("\t!!!!!alert your sleeping time!!!!!\t")
