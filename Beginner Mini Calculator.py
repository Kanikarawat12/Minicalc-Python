First = input('Enter First Number:')
Second = input('Enter Second Number:')
Operator = input('Enter Operator: (+,-,%,*,/,//)')

First = int(First)
Second = int(Second)

if Operator == '+':
    print(First+Second)

elif Operator == '-':
    print(First-Second)

elif Operator == '*':
    print(First*Second)

elif Operator == '/':
    print(First/Second)

elif Operator == '//':
    print(First//Second)

else:
    print('Invalid Operator')