
# Student College Gate Entry Verification System

print("======================================")
print("  COLLEGE GATE ENTRY VERIFICATION")
print("======================================")

# Get student details
student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

print("\nAnswer the following questions with yes or no.")

# Check college entry requirements
identity_card = input("Are you wearing your identity card? ").strip().lower()
proper_shirt = input("Are you wearing a proper shirt? ").strip().lower()
full_pants = input("Are you wearing full-length pants? ").strip().lower()
proper_shoes = input("Are you wearing proper shoes? ").strip().lower()

# Verify all requirements
if (
    identity_card == "yes"
    and proper_shirt == "yes"
    and full_pants == "yes"
    and proper_shoes == "yes"
):
    print("\n--------------------------------------")
    print("STUDENT NAME:", student_name)
    print("STUDENT ID:", student_id)
    print("RESULT: ENTRY ALLOWED")
    print("Welcome to the college!")
    print("--------------------------------------")

else:
    print("\n--------------------------------------")
    print("STUDENT NAME:", student_name)
    print("STUDENT ID:", student_id)
    print("RESULT: ENTRY DENIED")
    print("Please follow the college dress code.")

    # Display the missing requirements
    if identity_card != "yes":
        print("- Please wear your identity card.")
    if proper_shirt != "yes":
        print("- Please wear a proper shirt.")
    if full_pants != "yes":
        print("- Please wear full-length pants.")
    if proper_shoes != "yes":
        print("- Please wear proper shoes.")

    print("--------------------------------------")
    
