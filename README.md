# Password Cracking Tool

This is an educational tool designed to demonstrate the concept of dictionary-based password cracking. It uses a simple list of common passwords to attempt to gain access to a target system or service.

## Overview

A dictionary-based password cracking tool written in Python.

## Usage

### Prerequisites

* Python 3.x
* Install dependencies with: `pip install -r requirements.txt`
* A wordlist file (`wordlist.txt`) containing common passwords.

### Steps

1. Clone or download the repository.
   ```bash
   git clone https://github.com/SaiGawand12/password-cracking-tool.git
   cd password-cracking-tool
   ```
2. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```
3. Update a wordlist file (`wordlist.txt`) containing common passwords.
4. Add your target username in in `config.py`.
5. Run to start the cracking attempt.
   ```bash
   python app.py
   ```

Website will run on http://127.0.0.1:5000

![Output]("[templates/Screenshot 2024-11-23 133758.png](https://github.com/SaiGawand12/password-cracking-tool/blob/main/templates/Screenshot%202024-11-23%20133758.png)")

### Important Notes

* This tool is for educational purposes only. Use it responsibly and legally.
* Always ensure you have the necessary permissions before attempting to crack a password.
* Be aware of the potential consequences of using this tool.

## Requirements

* Python 3.x
* `requirements.txt` for dependencies.
* `wordlist.txt` for common passwords.
* `config.py` for target username.
* `app.py` for the main application.


## Code structrue
* HTML/CSS/JS for frontend.
* Python(flask) for backend.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update the requirements.txt file if you add any new dependencies.


## License
MIT License
Copyright (c) 2022 your-username
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

