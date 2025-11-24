print("       Hospital Management       ")
patient_record={}

def hospital_billing_system():
    ward_charges = {1: 1800, 2: 2500, 3: 3500, 4: 5000}
    gst_rate = 0.20
    
    while True:
        print("\n--- patient Check-in & Billing ---")
        name = input("Enter patient Name: ")
        citizen = input("Enter patient Nationality: ")
        address=input("Enter patient address: ")
        phone = int(input("Enter patient Contact Number: "))
        bloodgroup = input("Enter patient Blood Group: ")
        in_time= input("Enter the check-in date: ")
        check_out= input("Enter the check_out date: ")
        problem= input("Enter the issue happening with the patient : ")
        BodyTemprature = int(input("Enter the patient Body Temperature: "))
        BloodPressure = input("Enter patient Blood Pressure: ")
                             
        PresentCondition = input("Enter patient contidion (Critical,Stable): ")
        if PresentCondition == "Critical":
            print("Admit patient to ICU")
        else:
            print ("Admit patient to General Ward")
        patient_record={"patient_name":name, "problem": problem, "address": address, "in_time":in_time, "check_out": check_out}


        print("Ward Types (per day): 1: 1,800 | 2: 2,500 | 3: 3,500 | 4: 5,000")
        
        sel = int(input("Select+9 ward (1-4): "))
        num_days = int(input("Enter no. of days of stay: "))
        
        ward_fee = ward_charges.get(sel, 5000)

        base_amount = ward_fee * num_days
        gst = base_amount * gst_rate
        total_amount = base_amount + gst

        print("\n--- Billing Summary ---")
        print("Ward Fee per Day:", f"{ward_fee:,.2f}")
        print("Amount (excluding GST) :", f"{base_amount:,.2f}")
        print("GST Amount :", f"{gst:,.2f}")
        print("Total Amount (including GST) :", f"{total_amount:,.2f}")

        next_entry = input("\nAdmit next patient? (yes/no): ").lower()
        if next_entry == "no":
            break

if __name__ == "__main__":
    hospital_billing_system()
    print(patient_record)

