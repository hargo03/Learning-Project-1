# Learning-Project-1

A simple Python GUI application using Tkinter to collect user information.

## Features

- **Simple GUI Interface**: Clean and user-friendly design using Tkinter
- **Input Validation**: Validates name (required) and age (must be a number between 0-150)
- **Real-time Results**: Displays entered information immediately
- **Keyboard Support**: Press Enter to submit the form
- **Error Handling**: Clear error messages for invalid input

## Files

- `user_info_gui.py` - Main GUI application
- `demo.py` - Demo script with usage instructions
- `test_gui.py` - Test script for validation logic

## Requirements

- Python 3.x
- tkinter (usually included with Python, or install via `sudo apt install python3-tk` on Ubuntu/Debian)

## Usage

### Run the GUI Application

```bash
python3 user_info_gui.py
```

### Run the Demo

```bash
python3 demo.py
```

The GUI will open a window where you can:

1. Enter your name in the first field
2. Enter your age in the second field
3. Click "Submit" or press Enter to validate and display the information
4. Use "Clear" button to reset the form

## Input Validation

- **Name**: Cannot be empty
- **Age**: Must be a whole number between 0 and 150

If validation fails, an error dialog will appear with specific instructions.