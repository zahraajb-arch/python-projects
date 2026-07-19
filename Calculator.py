print('Simple Calculator' )
while True :
 operator= input ('Enter an operator( + - * /) :')
 num_1=float(input('enter the 1st number :'))
 num_2=float(input('enter the 2nd number :'))
 if operator=='+':
     result=num_1+num_2
     print(f'Result:{round(result, 3)}')
 elif operator =='-':
     result=num_1 - num_2
     print(f'Result:{round(result,3)}')
 elif operator=='*':
     result=num_1 * num_2
     print(f'Result:{round(result,3)}')    
 elif operator=='/':
     if num_2 ==0:
        print('cannot divide by zero')
        continue
     else: result= num_1/num_2
     print(f'Result:{round(result,3)}')
 else:
    print('Invalid operator')
 again=input('Do another calculation? (y/n)')
 if again != 'y':
    print ('Goodbye!')
 break


