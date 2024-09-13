try:
    i=int(input(f'Enter Number : '))
# except Exception:
#     print(Exception) #### for any errror
except ValueError:
    print('not is int')
except NameError:
    print('helo')

## to imp for raise errror