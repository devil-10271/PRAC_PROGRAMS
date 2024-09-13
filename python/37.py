def for_fin():
    try:
        value=int(input(f'Enter an number : '))
        return None
    except ValueError:
        print('Entered value is not number.')
        return None
    finally:
        print(100,f'%')
    
    # print('hello') for this reason we use finally

for_fin()