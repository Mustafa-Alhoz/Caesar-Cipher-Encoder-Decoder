alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba,  ,adPPYba,  ,adPPYYba,  8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88  I8[    ""  ""     `Y8  88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""   `"Y8ba,   ,adPPPPP88  88          
"8a,   ,aa 88,    ,88 "8b,   ,aa  aa    ]8I  88,    ,88  88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"'  `"YbbdP"'  `"8bbdP"Y8  88   


                          88
           88             88                                 
           ""             88                                                                  
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


print(logo)
print("\nWelcome To The Best Encryption Programme Ever !! ")
print("\nThis Programme Was Made By The Best Programmer Ever @mustafa_alhoz")

direction = input("\nType 'E' to encrypt, type 'D' to decrypt:  ").lower()
text = input("\nType your message:  ").lower()
shift = int(input("\nType the shift number: "))




def ceaser_cipher(text_user,shift_amount,cipher_direction):
  end_text=""
  dir="ENCRYPTED"
  if shift_amount >26:
     shift_amount=round(shift_amount % 26)
  
  if cipher_direction=="d":
    shift_amount*= -1
    dir="DECRYPTED"
  for letter in text_user:
    if letter in alphabet: 
      letter=alphabet[alphabet.index(letter)+shift_amount]
      end_text+=letter 
    else: 
      end_text+=letter
  print(f"\nHere is the {dir} result: {end_text}")        




ceaser_cipher(text,shift,direction)

while 5<10:               
  decision=input("\nDo you want to run the programme again if yes type 'Y' otherwise type 'N' : ").lower() 
  if decision=="n":
    print("\nGOOD BYE! \n")
    break 
  elif decision=="y":
   direction = input("\nType 'E' to encrypt, type 'D' to decrypt:  ").lower()
   text = input("\nType your message:  ").lower()
   shift = int(input("\nType the shift number: "))
   ceaser_cipher(text,shift,direction)
  else:
   decision
