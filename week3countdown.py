def countdown(x) :
    while x >= 0:
        print (x)
        x = x - 1
        
def fact(x):
    y = 1
    while x > 1:
        y = y * x
        print(y)
        x = x - 1
        

while True:
    x = int(input('\nPlease Enter a Number: '))
    while x <= 1 :
        print('Enter Number above 1')
        x = int(input('Please Enter a Number: '))
   
    
    y = input('Choose 1 for Countdown or 2 for Factorials: ')
    if y == '1':
        countdown(int(x))              
    if y == '2':
        fact(int(x))
    print('complete!\n')

    if input('Do you want to repeat(y/n)')== 'n' :
        print('\nThank You!')
        break


