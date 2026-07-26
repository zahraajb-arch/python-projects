# made by zahraa

print('caesar cipher')


def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

while True:
    text= input('Enter the text:')

    while True:
        try:
            shift= int(input('Enter shift (1_25):'))
            break
        except ValueError:
            print('Please enter a valid number .')
    while True:
      choice= input('Encrypt or Decrypt ? (e/d)').lower()
      if choice == 'e' or choice=='d':
          break
      else: 
       print('enter e or d please ')
        
    if choice == 'e':
        print(encrypt (text, shift))
    else:
        print (decrypt(text, shift))

    again= input("try again ? (y/n)").lower()

    if again != 'y':
        print('Goodbye!')
        break