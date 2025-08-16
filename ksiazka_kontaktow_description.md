# Python Address Book – Quick Overview

A simple Python program to manage contacts with persistent storage.

## Features

- Add new contacts
- Update existing contacts
- Delete contacts
- View contact names or full address book
- Save contacts to a JSON file

## Implementation / Techniques Used

- **Dictionary (`dict`)** for storing contacts as `{"Name": "Email"}`
- **`while True` loop** for the main menu
- **`for` loops** to iterate through contacts
- **`if/elif/else` statements** for menu options and input validation
- **`json` module** for saving and loading contacts
- **`os.path.exists`** to check if the data file exists
- **Input validation** to ensure correct user entries (e.g., avoid duplicates)
- **Pretty-printing JSON** with `indent=4` and `sort_keys=True` for readability
- Supports **non-ASCII characters** (e.g., Polish letters) in names and emails

## Usage Notes

- Run the program in a terminal or command prompt
- Enter the number corresponding to the desired menu option
- Follow prompts to add, update, delete, or view contacts
- Remember to save changes before exiting to keep data in `plik_z_danymi.json`
