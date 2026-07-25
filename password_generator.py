import random
import string
import pyperclip

while True:
  length= int(input('enter length : '))
  use_letters= input('Include letters?(y/n)')
  use_digits= input ('Include digits? (y/n)')
  use_symbols= input ('Include symbols? (y/n)')




  characters = '' 
  if use_letters == 'y' :
      characters += string.ascii_letters
  if use_digits == 'y':
      characters += string.digits
  if use_symbols == 'y' :
      characters += string.punctuation

  if characters == '':
      print('Error :you must choose at least one character type.' )
      exit()
  password ='' 

  for z in range(length):
      next_character =random.choice(characters)
      password += next_character


  print (f'your random password is : {password}')

  if length < 8 :
      print('Password strength : weak')
  elif length <12 and length >8 :
      print ('password strength : medium')
  else :
      print('password strength : strong')

  pyperclip.copy(password)
  print('Password copied to clipboard!')

  again = input('generate another password?(y/n)')
  if again !='y':
      print('Goodbye!')
      break