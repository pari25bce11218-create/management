Hospital Management & Billing System

**1. Overview**

The Hospital Management & Billing System is a Python-based console application designed to manage patient check-in details and generate billing information based on ward type and number of days admitted.
The system allows hospital staff to register patient information, determine the patient’s condition, choose an appropriate ward, and automatically calculate hospitalization charges including GST.
This project demonstrates the use of loops, dictionaries, conditional statements, and basic billing logic in Python.

**2. Features**

a. Patient Admission Module
Collects patient's personal details.
Records health-related information.
Determines admission type (ICU or General Ward).
b. Ward & Billing System
Allows selection of ward type.
Automatically applies ward charges per day.
Calculates:
Base amount
GST (20%)
Total bill
c. User-Friendly Interaction
Repeatedly admits multiple patients.
Allows staff to stop admission anytime.
Stores the latest patient record.
d. Data Storage
Stores patient details in a dictionary.
Displays the final saved record at the end.

**3.Technologies/tools used**

--> Programming Language
Python 3.x
--> Python Concepts Used
Dictionaries
Loops
Conditional statements
String formatting
User input handling
Basic arithmetic operations

**4. Steps to install & run the project**

a. Install Python
Make sure Python 3.x is installed on your system:
https://www.python.org/downloads/
b. Create a Python File
Create a file named:
hospital_management.py
c. Paste Your Code
Copy your Hospital Management System code into this file.
d. Run the Program
Open terminal / command prompt and run:
python hospital_management.py
OR if using Python 3 specifically:
python3 hospital_management.py
e. Follow the On-Screen Instructions
Enter patient details
Select ward type
View the automatically generated bill.

**5. Instructions for testing**

To test the Hospital Management System, follow these steps:
Test Case 1 — General Flow
Run the program
Enter a sample patient name
Enter nationality, address, contact number
Enter health details 
Enter "Stable"
Select ward type 
Enter number of days
Verify that:
Ward charges are correct
GST = 20% of base amount
Total amount is calculated correctly
Test Case 2 — Critical Patient
Enter "Critical" as condition
Ensure program prints:
"Admit patient to ICU"
Test Case 3 — Invalid Input
Try entering:
Letters instead of numbers
Invalid ward number
Test Case 4 — Multiple Patients
After generating a bill, enter "yes" to admit another patient.
At the end, enter "no"
Check if patient_record prints the last admitted patient's details.
