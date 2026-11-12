# Ohm's Law and Power Calculator

## What it does
A Python command-line calculator for mechatronics students and engineers.
It solves for Voltage, Current, Resistance or Power using Ohm's Law and the
power formula. It also has a "Smart Solve" mode where you enter any two known
values and get all four quantities at once, plus a calculation history.

## How to run it
Install Python 3, then run:

```bash
python3 ohms_law.py
```

## Sample output
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
