alphabet = 'abcdefghijklmnopqrstuvwxyz'

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


def encrypt(message, shift):
    encrypted = ''
    for x in message:
        if x in alphabet:
            new_position = (alphabet.index(x) + shift) % len(alphabet)
            encrypted += alphabet[new_position]
    print(f"Here is the encoded message: {encrypted}")


def decrypt(message, shift):
    decrypted = ''
    for y in message:
        original_position = (alphabet.index(y) - shift) % len(alphabet)
        decrypted += alphabet[original_position]
    print(f"Here is the decoded message: {decrypted}")


print(logo)
answer = 'y'
while answer == 'y':
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if choice != 'encode' and choice != 'decode':
        print('Wrong input!', end=' ')
    else:
        message = input('Type your message:\n')
        shift = input('Type the shift number:\n')
        while True:
            try:
                shift = int(shift)
                break
            except ValueError:
                shift = input('Wrong input! Please type the integer:\n')
        if choice == 'encode':
            encrypt(message=message.lower(), shift=shift)
        elif choice == 'decode':
            decrypt(message=message.lower(), shift=shift)
    answer = input('Would you like to continue? (y/n) ')
else:
    print('Goodbye!')
