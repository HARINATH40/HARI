import random
import string

while True:
    try:
        length=int(input("Enter the desired number (8-15): ").strip())

        if length < 8:
            print("Password is too short, keep it atleast 8")
        elif length > 15:
            print("Password is large, keep it under 15 ")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

use_digits=input("Include digits? (yes/no): ").strip().lower()
use_symbols=input("Symbols? (yes/no): ").strip().lower()
    
characters=string.ascii_letters
    
if use_digits=="yes":
    characters+=string.digits
    
if use_symbols=="yes":
    characters+=string.punctuation 
        
if not characters:
    print("No characters are selected for password...!")
    
password="".join(random.choices(characters,k=length))     
print("Generated Password: ",password)
    
   


