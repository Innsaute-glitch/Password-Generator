# Gets the necessary modules
import secrets
import time
import string

# Set the variables
spl = "!@#$%&/\\"

def get_restart(input_statement, y_statement, n_statement, yes_var, no_var):
    """Prompt user for a yes/no decision with custom message.
Repetedly asks for y or n.

Arguments:
    input_statement (str): The question to prompt the user with
    y_statement (str): Message to display if user chooses yes_var
    n_statement (str): Message to display if user chooses no_var
    yes_var: Yes variables like yes or true or whatever
    no_var: No variables like no or False or whatever

What it gives back? => str: Either yes_var or no_var based on user's validated input...
    """
    while True:
        var = input(input_statement)
        if var.lower() == yes_var:
            print(y_statement)
            return yes_var
        elif var.lower() == no_var:
            print(n_statement)
            return no_var
        else:
            print(f">>> Please enter either {yes_var} or {no_var}!")

def get_strength():
    if_ascii = get_restart("Do you want any ASCII characters in ur password?(y/n) ", ">>> Confirmed", ">>> Rejected", 'y', 'n')
    if_digits = get_restart("Do you want any digits in ur password?(y/n) ", "Confirmed", "Rejected", 'y', 'n')
    if_special = get_restart("Do you want any special characters in ur password?(y/n) ", "Confirmed", "Rejected", 'y', 'n')
    all_chars = ""
    if if_ascii == 'y':
        all_chars += string.ascii_letters
    if if_digits == 'y':
        all_chars += string.digits
    if if_special == 'y':
        all_chars += spl
    return all_chars

#Try out a function
def main():
    """Gets a secure password"""
    chr = []
    # Make a loop for error handling
    while True:
        time.sleep(0.2)
        letters = int(input("How many characters do you want in your password? "))
        time.sleep(0.2)
        if letters <= 0:
            print(f""">>> A password can't be {letters} characters long T-T
Please try again..""")
        else:
            break
        time.sleep(0.2)
        print(">>> This is not a number.. Please input a valid integer!")
    all_chars_final = get_strength()
    for i in range(letters):
        chr.append(secrets.choice(all_chars_final))
    return ''.join(chr)

while True:
    try:
        password = main()
        print("!!! Your generated password is:", password)
        if_again = get_restart("Do you want to generate another one?(y/n) ", ">>> Confirmed", ">>> Rejected", 'y', 'n')
        if if_again == 'y':
            continue
        else:
            print(">>> Exiting Successfully...")
            break
    except KeyboardInterrupt:
        print()
        print(">>> Keyboard Interrupt Detected.. Exiting..")
        break
    except EOFError:
        print()
        print(">>> EOF Error Detected.. Exiting..")
        break
    except ValueError:
        print(">>> This is not a valid number.. Please try again!")
    except Exception as e:
        print()
        print(f">>> An error occurred: {e}. Please try again.")
        break
