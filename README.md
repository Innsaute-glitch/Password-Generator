# 🔐 Password Generator

A secure command-line password generator written in Python that uses the `secrets` module for cryptographically strong password generation.

## ✨ Features

- Cryptographically secure random generation using Python's `secrets` module
- Customizable password length
- Includes uppercase, lowercase, digits, and special characters
- Input validation with error handling
- Option to generate multiple passwords in one session

## 🚀 Getting Started

### Prerequisites

- Python 3.x

No external libraries needed — only built-in Python modules are used.

### Running the Script

```bash
python New.py
```

## 📖 Usage

1. Run the script
2. Enter the desired password length when prompted
3. Your secure password will be generated and displayed
4. Choose whether to generate another password or exit

```
How many characters do you want in your password? 16
g#Km2@Xv!pL9qR4&
Try again? (y/n): n
Thanks for using this!
```

## 🛠️ How It Works

- Builds a character pool from uppercase letters, lowercase letters, digits, and special characters
- Uses `secrets.choice()` to pick each character independently and randomly
- Joins the characters into a final password string

## 📌 Notes

- `secrets` is used instead of `random` for stronger, cryptographically secure randomness — making it suitable for actual password generation
- Passwords are never stored or logged anywhere

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Built as a Python learning project* 🐍

(Current Objectives: Enhance user experience by usinh time module through adding time.sleep later)
