# Random Password Generator (Beginner)

This project is a command-line tool that generates random passwords based on user-specified criteria. It aims to help beginners learn Python by incorporating concepts such as randomisation, user input validation, and character set handling.

## Features

- **Random Password Generation:** Create passwords with a specified length and character set.
- **Character Types:** Include uppercase and lowercase letters, numbers, and symbols.
- **User Input Validation:** Ensures valid input for password length and character types.

## Getting Started

### Prerequisites

- Python 3.11.5

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/eadewusic/OIBSIP.git
   cd oibsip_task1
   ```

2. **Run the script:**
   ```bash
   python password_generator.py
   ```

## Usage

1. **Specify the password length:**

   - When prompted, enter the desired length of the password.

2. **Select character types to include:**

   - You will be asked whether to include uppercase letters, lowercase letters, numbers, and symbols. Enter 'y' for yes and 'n' for no.

3. **Get the generated password:**
   - The script will generate and display the password based on your specifications.

### Example

```
Enter the desired password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): n

Generated password: B6cD3aF9bH2g
```

## Code Overview

### `password_generator.py`

- **Imports:**

  - `random`: For generating random characters.
  - `string`: For accessing different character sets.

- **Functions:**
  - `get_user_input()`: Prompts the user for password length and character types.
  - `validate_input()`: Validates the user input for length and character types.
  - `generate_password()`: Generates the password using the validated inputs.
  - `main()`: Main function that drives the script.

## Learning Objectives

1. **Randomisation:**
   - Using the `random` module to generate random characters.
2. **User Input Validation:**
   - Ensuring the user inputs a valid password length and selects at least one character type.
3. **Character Set Handling:**
   - Managing different character sets (letters, numbers, symbols) and combining them based on user preferences.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
