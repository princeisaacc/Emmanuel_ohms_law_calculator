# Ohm's Law and Power Calculator

**Student:** Segbedeji Folorunsho Emmanuel  
**Programme:** ND1 Mechatronics Engineering, YabaTech

## Introduction
This project is a Python command-line calculator for solving electrical quantities using Ohm's Law and the power formula. It can calculate Voltage, Current, Resistance, or Power. Its Smart Solve feature accepts any two known values and calculates all four quantities. The program also keeps a calculation history during the session.

## What I learned
While working on this project, I learned how to:
- Use Ohm's Law (`V = I × R`) and the power formula (`P = V × I`) in a program.
- Collect input from a user with Python's `input()` function and convert numeric input to `float` values.
- Use conditional statements to select calculations and handle different combinations of known values.
- Create and call functions to organize a program.
- Handle invalid input and prevent division by zero.
- Store results in a list and display or clear the calculation history.

## Requirements
- Python 3 installed on your computer.
- The `ohms_law.py` file downloaded or cloned from this repository.

## Step-by-step instructions to run the program
1. Install Python 3 if it is not already installed. On Windows, select the option to add Python to PATH during installation.
2. Download or clone this repository to your computer.
3. Open a terminal or command prompt.
4. Change to the folder containing `ohms_law.py`. For example:
   ```bash
   cd path/to/Emmanuel_ohms_law_calculator
   ```
5. Run the program using the command for your system:
   ```bash
   python3 ohms_law.py
   ```
   On Windows, you can also try:
   ```bash
   py ohms_law.py
   ```
6. Choose an option from the menu by entering its number. For Smart Solve, enter exactly two known values and leave the other fields blank.
7. To finish, choose option `5` (Quit).

## Sample output
The example below shows Smart Solve with a voltage of 12 V and a current of 2 A. The calculator finds the resistance and power, then displays the calculation history.

```text
===== OHM'S LAW CALCULATOR =====
1. Perform Calculation
2. Smart Solve (enter any two values)
3. View Calculation History
4. Clear History
5. Quit
Enter your choice (1-5): 2

--- SMART SOLVE (enter any TWO known values) ---
Leave a value blank if you don't know it.
You must provide exactly two values.

Voltage (V)     : 12
Current (A)     : 2
Resistance (Ohm):
Power (W)       :

===== SMART SOLVE RESULT =====
Voltage    = 12.00 V
Current    = 2.00 A
Resistance = 6.00 Ohm
Power      = 24.00 W

===== OHM'S LAW CALCULATOR =====
1. Perform Calculation
2. Smart Solve (enter any two values)
3. View Calculation History
4. Clear History
5. Quit
Enter your choice (1-5): 3

===== CALCULATION HISTORY =====
1. Smart Solve -> V=12.00V, I=2.00A, R=6.00Ohm, P=24.00W
```
