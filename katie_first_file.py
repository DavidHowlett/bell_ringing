print('Hello World')
print('Hello David')
print('I am really bad at this')
x = 10/3
print(x)
y = [1, 3, 5]
y = y+[7, 9]
print(y)
print(y[2])

x = 'an example piece of text'
print(x)

rounds = [1, 2, 3, 4, 5, 6]


def swap(change, a, b):
    # print(change,a ,b)
    temp = change[a]
    change[a] = change[b]
    change[b] = temp


for i in range(3):
    print('Katie is learning quickly')


print('Go Plain Hunt!')
print(rounds)

for i in range(6):
    swap(rounds, 0, 1)
    swap(rounds, 2, 3)
    swap(rounds, 4, 5)
    print(rounds)
    swap(rounds, 1, 2)
    swap(rounds, 3, 4)
    print(rounds)

print("That's All!")
