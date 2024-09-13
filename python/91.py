def my_gen(x):
    for i in range(1,11):
        i*=x
        yield i

tableof=3

gen=my_gen(tableof)
for j in range(10):
    print(f'{tableof} x {j} = {next(gen)}')
