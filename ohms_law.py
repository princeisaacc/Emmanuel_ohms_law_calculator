# ============================================================
# OHM'S LAW AND POWER CALCULATOR
# Author: Segbedeji Folorunsho Emmanuel
# ND1 Mechatronics Engineering, YabaTech
# ------------------------------------------------------------
# This program calculates Voltage, Current, Resistance or Power
# using Ohm's Law (V = I x R) and the Power formula (P = V x I).
#
# MY OWN TWIST:
# A "Smart Solve" mode where the user enters ANY TWO known
# values and the program works out ALL FOUR quantities
# (Voltage, Current, Resistance, Power) at once.
# It also keeps a calculation history for the session.
# ============================================================

# This list stores every successful calculation as a text string,
# so the user can review past results during the session.
history = []


# ------------------------------------------------------------
# FUNCTION: smart_solve
# The "own twist" feature. The user gives any two values,
# and we compute the rest using Ohm's Law and Power formulas.
# V = I * R,  P = V * I,  R = V / I,  I = V / R
# ------------------------------------------------------------
def smart_solve():
    print("\n--- SMART SOLVE (enter any TWO known values) ---")
    print("Leave a value blank if you don't know it.")
    print("You must provide exactly two values.\n")

    # Collect inputs. Blank means "unknown".
    v_in = input("Voltage (V)     : ")
    i_in = input("Current (A)     : ")
    r_in = input("Resistance (Ohm): ")
    p_in = input("Power (W)       : ")

    # Convert only non-blank inputs to float. Catch bad input.
    try:
        voltage = float(v_in) if v_in.strip() else None
        current = float(i_in) if i_in.strip() else None
        resistance = float(r_in) if r_in.strip() else None
        power = float(p_in) if p_in.strip() else None
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    # Count how many values the user actually gave.
    given = [voltage, current, resistance, power]
    known_count = sum(1 for v in given if v is not None)

    if known_count != 2:
        print("Please enter EXACTLY two known values.")
        return

    # Now figure out the two unknowns.
    # We check each possible pair and solve accordingly.

    # Case 1: Voltage and Current known -> find Resistance & Power
    if voltage is not None and current is not None:
        if current == 0:
            print("Error: Current cannot be zero (division by zero).")
            return
        resistance = voltage / current
        power = voltage * current

    # Case 2: Voltage and Resistance known -> find Current & Power
    elif voltage is not None and resistance is not None:
        if resistance == 0:
            print("Error: Resistance cannot be zero (division by zero).")
            return
        current = voltage / resistance
        power = voltage * current

    # Case 3: Voltage and Power known -> find Current & Resistance
    elif voltage is not None and power is not None:
        if voltage == 0:
            print("Error: Voltage cannot be zero (division by zero).")
            return
        current = power / voltage
        resistance = voltage / current

    # Case 4: Current and Resistance known -> find Voltage & Power
    elif current is not None and resistance is not None:
        voltage = current * resistance
        power = voltage * current

    # Case 5: Current and Power known -> find Voltage & Resistance
    elif current is not None and power is not None:
        if current == 0:
            print("Error: Current cannot be zero (division by zero).")
            return
        voltage = power / current
        resistance = voltage / current

    # Case 6: Resistance and Power known -> find Voltage & Current
    elif resistance is not None and power is not None:
        if resistance == 0:
            print("Error: Resistance cannot be zero (division by zero).")
            return
        voltage = (power * resistance) ** 0.5   # V = sqrt(P * R)
        current = voltage / resistance

    # Show the full result.
    print("\n===== SMART SOLVE RESULT =====")
    print(f"Voltage    = {voltage:.2f} V")
    print(f"Current    = {current:.2f} A")
    print(f"Resistance = {resistance:.2f} Ohm")
    print(f"Power      = {power:.2f} W")

    # Save this result to history.
    history.append(
        f"Smart Solve -> V={voltage:.2f}V, I={current:.2f}A, "
        f"R={resistance:.2f}Ohm, P={power:.2f}W"
    )


# ------------------------------------------------------------
# FUNCTION: calculate
# The original single-unknown calculator. The user picks which
# quantity to find, gives the other known values, and gets the
# answer.
# ------------------------------------------------------------
def calculate():
    print("\n1. Voltage   (V = I x R)")
    print("2. Current   (I = V / R)")
    print("3. Resistance(R = V / I)")
    print("4. Power     (P = V x I)")

    choice = input("Choose calculation (1-4): ")

    try:
        if choice == "1":
            # Voltage = Current x Resistance
            current = float(input("Enter current (A): "))
            resistance = float(input("Enter resistance (Ohm): "))
            result = f"Voltage = {current * resistance:.2f} V"

        elif choice == "2":
            # Current = Voltage / Resistance
            voltage = float(input("Enter voltage (V): "))
            resistance = float(input("Enter resistance (Ohm): "))
            if resistance == 0:
                print("Error: Resistance cannot be zero (division by zero).")
                return
            result = f"Current = {voltage / resistance:.2f} A"

        elif choice == "3":
            # Resistance = Voltage / Current
            voltage = float(input("Enter voltage (V): "))
            current = float(input("Enter current (A): "))
            if current == 0:
                print("Error: Current cannot be zero (division by zero).")
                return
            result = f"Resistance = {voltage / current:.2f} Ohm"

        elif choice == "4":
            # Power = Voltage x Current
            voltage = float(input("Enter voltage (V): "))
            current = float(input("Enter current (A): "))
            result = f"Power = {voltage * current:.2f} W"

        else:
            print("Invalid choice. Please select 1 to 4.")
            return

        # Print and store the result.
        print("\nRESULT:", result)
        history.append(result)

    except ValueError:
        # This catches any bad number input from the user.
        print("Invalid input! Please enter numbers only.")


# ------------------------------------------------------------
# MAIN MENU
# The program keeps running until the user chooses to quit.
# ------------------------------------------------------------
while True:
    print("\n===== OHM'S LAW CALCULATOR =====")
    print("1. Perform Calculation")
    print("2. Smart Solve (enter any two values)")
    print("3. View Calculation History")
    print("4. Clear History")
    print("5. Quit")

    option = input("Enter your choice (1-5): ")

    if option == "1":
        calculate()

    elif option == "2":
        smart_solve()

    elif option == "3":
        # Show history if there is any, otherwise tell the user.
        if not history:
            print("No calculation history available.")
        else:
            print("\n===== CALCULATION HISTORY =====")
            for index, item in enumerate(history, start=1):
                print(f"{index}. {item}")

    elif option == "4":
        history.clear()
        print("History cleared successfully.")

    elif option == "5":
        print("Thank you for using the calculator. Goodbye!")
        break   # exit the loop, ending the program

    else:
        print("Invalid option! Please choose 1 to 5.")
