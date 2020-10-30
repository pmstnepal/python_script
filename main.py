count = (2, 2, 2, 2, 5, 5)
max = count[0]
for repeat in count:
    print('x' * repeat)
for supposed in count:
    if supposed > max:
        max = supposed
        print(max)

print(f'lets play a simple game')
started = False
while True:
    cmt = input('> ').upper()

    if cmt == 'HELP':
        print('''
start - to start the game
stop - to stop the game
quit - to exit''')
    elif cmt == "START":
        if started :
            print("game is already started")
        else:
            started = True
            print(f"game is starting")
            break
    elif cmt == "STOP":
        if not started:
            print("game is alredy stopped")
        else:
            started = False
            print(f"game is stoping")
    elif cmt == "QUIT":
        exit()
    else:
        print('I dont understant that ...')
print(f'Guess the no to win, 3 chance, if you win you will go to next level')
screte_no = 6
count_no = 0
cout_limit = 3
while count_no < cout_limit:
    guess = int(input('Guess: '))
    count_no += 1
    if guess == screte_no:
        print('You Won')
        break
else:
    print('you lose')
    exit()
x = (10 + 2) * 2 ** 3 - 15
print(x)
course = '''Personal Detail Section'''
course1 = '''please answer the following questions'''
print(course.upper())
print(course1 [0:])
first_name = input('What is your first name? ')
last_name = input('what is your last name? ')
address = input('where do you live? ')
dob = input('what is your date of birth year? ')
age = 2020 - int(dob)
weight_kg = int(input('weight (kg): '))
weight_lbs = weight_kg / 0.45
msg = f'{first_name} {last_name} who lives in {address} whos age is {age} having {weight_lbs} lbs weight'
print(msg)
credit = input('Do your annual income access $ 100,000? Yes or No ')
if credit.upper() == "YES":
    interest = 100000 * 0.10
    print(f"you are eligible for the 10% down payment scheme that is $ {interest}")
elif credit.upper() == "NO":
    interest = 100000 * 0.20
    print(f"you are not eligible for the 10% scheme so 20% down payment that is $ {interest}")
print('have nice day')
