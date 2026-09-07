import csv
import os

file_name = "students.csv"

def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    file_exists = os.path.isfile(file_name)
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age])
    print("Student added.")

def display_students():
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row]
        if not rows:
            print("No student records found.")
            return
        print("\nID\tName\tAge")
        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")
    except FileNotFoundError:
        print("No student records found.")

def search_student():
    search_id = input("Enter ID to search: ")
    found = False
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == search_id:
                    print("Student found:", row)
                    found = True
        if not found:
            print("Student not found.")
    except FileNotFoundError:
        print("No student records found.")

def update_student():
    update_id = input("Enter ID to update: ")
    found = False
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row]

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] == update_id:
                    found = True
                    print("Current record:", row)
                    name = input("Enter new name (leave blank to keep same): ").strip()
                    age = input("Enter new age (leave blank to keep same): ").strip()
                    new_name = name if name else row[1]
                    new_age = age if age else row[2]
                    writer.writerow([row[0], new_name, new_age])
                    print("Student updated.")
                else:
                    writer.writerow(row)

        if not found:
            print("Student not found.")
    except FileNotFoundError:
        print("No student records found.")

def delete_student():
    delete_id = input("Enter ID to delete: ")
    found = False
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row]

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] == delete_id:
                    print("Record deleted:", row)
                    found = True
                else:
                    writer.writerow(row)

        if not found:
            print("Student not found.")
    except FileNotFoundError:
        print("No student records found.")

def main():
    print("Student Management System (For Teachers and Parents)")
    while True:
        print("\n1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
