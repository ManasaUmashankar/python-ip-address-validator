# IP Address Validator

A beginner-friendly Python command-line tool that validates IPv4 and IPv6 addresses and classifies them by address type.

## Features

- Validates IPv4 addresses
- Validates IPv6 addresses
- Identifies private and public addresses
- Identifies loopback and multicast addresses
- Handles invalid and empty input
- Accepts multiple IP addresses separated by commas
- Displays a validation summary
- Includes automated unit tests

## Project Structure

```text
python-ip-address-validator/
├── src/
│   └── validator.py
├── tests/
│   ├── test_validator.py
│   └── .gitkeep
├── main.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3.8 or later
- No external packages required

## Run the Project

```powershell
python main.py
```

Enter IP addresses separated by commas when prompted.

## Run Tests

```powershell
python -m unittest discover -s tests -v
```

## Example Input

```text
192.168.1.1, 8.8.8.8, 127.0.0.1, hello
```

## Concepts Practiced

- Python functions
- Conditional statements
- Loops
- Lists and string methods
- Exception handling
- Python's built-in `ipaddress` module
- Unit testing with `unittest`

## Learning Goal

This project is part of my Python and networking foundations journey, building practical skills for cybersecurity.

## Disclaimer

This tool classifies IP addresses for learning purposes. An address being classified as public does not guarantee that it is reachable from the internet.