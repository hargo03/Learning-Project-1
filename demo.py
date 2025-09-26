#!/usr/bin/env python3
"""
Demo script to show how to use the user_info_gui module.
Run this script to see the GUI in action.
"""

import sys
import os

def main():
    """Main function to demonstrate the GUI."""
    print("User Information GUI Demo")
    print("=" * 30)
    print()
    
    print("This script demonstrates a simple Tkinter GUI that:")
    print("• Collects user's name and age")
    print("• Validates the input (age must be a number between 0-150)")
    print("• Shows the entered information")
    print("• Provides clear and submit buttons")
    print("• Supports Enter key for form submission")
    print()
    
    # Check if we're in a display environment
    if not os.environ.get('DISPLAY'):
        print("Note: No display environment detected.")
        print("To run the GUI, you need a display environment with X11 forwarding or GUI support.")
        print()
        print("To run the GUI:")
        print(f"  python3 {os.path.dirname(os.path.abspath(__file__))}/user_info_gui.py")
        print()
        print("The GUI features:")
        print("• Input validation with error messages")
        print("• Clean, professional interface using ttk widgets") 
        print("• Results display area")
        print("• Keyboard shortcuts (Enter to submit)")
        return
    
    try:
        # Try to import and run the GUI
        from user_info_gui import main as gui_main
        print("Starting GUI application...")
        gui_main()
    except Exception as e:
        print(f"Error running GUI: {e}")
        print("Make sure you have tkinter properly installed.")
        

if __name__ == "__main__":
    main()