def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 35:
        return "D"
    else:
        return "F"


def main():
    print("=== Student Grade Calculator ===")

    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        grade = calculate_grade(marks)
        result = "Pass" if marks >= 35 else "Fail"

        print("\n--- Result ---")
        print("Student:", name)
        print(f"Marks: {marks:g}/100")
        print(f"Grade: {grade}")
        print("Status:", result)

    except ValueError:
        print("Please enter a valid number for marks.")


if __name__ == "__main__":
    main()
