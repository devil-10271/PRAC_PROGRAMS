pr_set={'a','b','c','d','e','f','g','h','i','j','k','l','p','q','r','s','t','u','v','w','x','y','z'}

def Enc_rev(value):
    a=""
    ret_li=list()
    # print(type(value),len(value))
    if (type(value) != type(list())):
        if(len(value)<=3):
            for i in value:
                a=i+a
        return a
    else:
        an=""
        for i in value:
            a=""
            if len(i)<=3:
                for j in i:
                    a=j+a
                ret_li.append(a)
            else:
                an=i[1:len(i)]
                an=an+i[0]
                for j in range(3):
                    b=pr_set.pop()
                    an=b+an
                for p in range(3):
                    b=pr_set.pop()
                    an=an+b
                ret_li.append(an)
    return ret_li
                
       



def Encode(value):
    li=[]
    # print(type(value),len(value))
    if(len(value)<=3):
        ans=Enc_rev(value)
        return ans
    else:
        li=value.split(' ')
        ans=Enc_rev(li)
        ans=' '.join(ans)
        return ans



def dec_rev(value):
    a=""
    ret_li=list()
    if (type(value) != type(list())):
        if(len(value)<=3):
            for i in value:
                a=i+a
        return a
    else:
        an=''
        for i in value:
            if(len(i)<=3):
                a=''
                for j in i:
                    a=j+a
                ret_li.append(a)
            else:
                jus_li=list()
                for j in i:
                    jus_li.append(j)
                # print(jus_li)
                for j in range(3):
                    del jus_li[0]
                for j in range(3):
                    del jus_li[-1]
                jus_li.insert(0,jus_li[-1])
                del jus_li[-1]
                # print(juss_li)
                an=''.join(jus_li)
                # print(an)
                ret_li.append(an)
    return ret_li          




def Decode(value):
    li=[]
    if(len(value)<=3):
        ans=dec_rev(value)
        return ans
    else:
        li=value.split()
        ans=dec_rev(li)
        ans=' '.join(ans)
        return ans




# MAIN ##############################################################################
message=input('\nenter the string : '.capitalize())
fun=input(f'''Press Given number to Perform action on String
        1--->Encode 
        2--->Decode
            : ''')
if(fun=='1'):
    a=Encode(message)
    print(a)
elif(fun=='2'):
    a=Decode(message)
    print(a)
else:
    print(f'Invalid Input 1')
