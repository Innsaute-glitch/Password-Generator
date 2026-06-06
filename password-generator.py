# Gets the necessary modules
import secrets
import time
import string

# Set the variables
spl = "!@#$%&/-"
strength = string.ascii_letters + string.digits + spl

#Try out a function
def password():
    """Gets a secure password"""
    chr = []
    # Make a loop for error handling
    while True:
        try:
            time.sleep(0.5)
            letters = int(input("How many characters do you want in your password? "))
            time.sleep(0.5)
            if letters <= 0:
                print(f"""A password can't be {letters} characters long T-T
Please try again..""")
            else: break
        except:
            time.sleep(0.5)
            print("This is not a number.. Please input a valid integer!")  
    for i in range(letters):
        chr.append(secrets.choice(strength))
    return ''.join(chr)

passw = password()
print(passw)

while True:
    try_again = input("Try again?")
    if try_again == "y":
        time.sleep(0.5)
        passw = password()
        print(passw)
    elif try_again == "n":
        time.sleep(0.5)
        print("Thanks for using this script :)")
        print()
        break
    else:
        time.sleep(0.5)
        print('Please input either "y" or "n"')

# Comments:
# This one was quite hard to do - Logic chains and all was self made, but had to use ai to ask for coding doubts abour about 4 times..
# Will try the again later tommorow..

# Noted past errors for reference: (Resolved now)
# - local vs global variables - returning 'none' Error
# - break logic messing up the 'while True:' chains
# - infinite loop of 'please input either x or y'
# - over complication by making several loops