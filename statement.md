**1.Problem Statement**

Managing patient admissions and billing in hospitals manually is time-consuming and prone to errors. Hospital staff must record patient details, determine their condition, select an appropriate ward, and calculate charges including taxes.
Without an automated system, this process becomes:
Slow and inefficient
Prone to calculation mistakes
Difficult to maintain records
Hard to manage multiple patients
To solve this, a simple and efficient Python-based console application is needed to automate patient check-in and generate accurate bills.


**2.Scope of the Project**

The scope of this project includes:
a. Patient Information Handling
The system collects basic patient details such as:
Name
Address
Contact number
Blood group
Health issue
Body temperature & blood pressure
Check-in and check-out dates
b. Admission Decision
Based on the patient’s condition (Critical / Stable), it recommends:
ICU
General Ward
c. Billing System
The program:
Allows selecting a ward type
Calculates ward charges based on stay duration
Adds GST (20%)
Generates a complete billing summary.

**3.Target Users**

The main users of the Hospital Management & Billing System are:
 a. Hospital Receptionists
For entering patient details and generating bills.
 b. Billing & Accounts Staff
To compute hospital charges quickly and error-free.
 c. Small Clinics
Who need a lightweight, non-database billing solution.
 d. Beginners in Python
Learning how to build a functional Python console project.

**4.High-Level Features**

 a. Patient Registration
Allows staff to enter complete patient information
Records medical details (temperature, blood pressure, issue).
 b. Admission Suggestion
Determines whether the patient goes to ICU or General Ward.
c. Ward Selection
Different types of wards with different daily charges.
d. Automatic Billing
Calculates:
Ward fee × number of days
GST at 20%
Total payable amount
Displays a formatted billing summary
e. Multi-Patient Support
Allows admitting multiple patients in one run.
Stops when the user chooses “no".

