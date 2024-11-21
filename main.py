import string

def encrypt(message,shift):
  alphabet = string.ascii_lowercase
  encrypted_message = ""
  
  for letter in message:
    if letter.lower() in alphabet:
      original_positiin = alphabet.index(letter.lower())
      new_position = (original_positiin + shift) % 26
      encrypted_letter = alphabet[new_position]
      if letter.isupper():
        encrypted_letter = encrypted_letter.upper()
      encrypted_message += encrypted_letter
    else:
      encrypted_message += letter
  print(encrypted_message)
  
message = input("Enter the sentence: ")
shift = int(input("Enter the code shift: "))

encrypt(message,shift)

def encrypt1(message1,shift1):
  alphabet = string.ascii_lowercase
  encrypted_message = ""
  
  for letter in message1:
    if letter.lower() in alphabet:
      original_positiin = alphabet.index(letter.lower())
      new_position = original_positiin - shift1
      encrypted_letter = alphabet[new_position]
      if letter.isupper():
        encrypted_letter = encrypted_letter.upper()
      encrypted_message += encrypted_letter
    else:
      encrypted_message += letter
  print(encrypted_message)
message1 = input("Enter the sentence: ")
shift1 = int(input("Enter the code shift: "))
encrypt1(message1,shift1)