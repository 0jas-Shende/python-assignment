import pandas as pd

# Load the dataset
# Note: Ensure openpyxl is installed (pip install openpyxl) to read .xlsx files
try:
    df_emp = pd.read_excel('employee.xlsx')
except FileNotFoundError:
    print("Error: The file 'employee.xlsx' was not found.")
    # Creating dummy data for demonstration purposes if file is missing
    emp_data = {
        'Employee ID': [101, 102, 103, 104],
        'Employee Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Department': ['Automotive', 'IT', 'Automotive', 'Sales'],
        'Designation': ['Developer', 'Manager', 'Tester', 'Developer']
    }
    df_emp = pd.DataFrame(emp_data)

# a) Print list of employees working for "Automotive" domain
print("--- Employees in Automotive Department ---")
automotive = df_emp[df_emp['Department'] == 'Automotive']
print(automotive)

# b) Print details of an employee with employee ID given by an end user
try:
    search_id = int(input("\nEnter Employee ID to search: "))
    details = df_emp[df_emp['Employee ID'] == search_id]
    
    if not details.empty:
        print(f"Details for Employee ID {search_id}:")
        print(details)
    else:
        print("No employee found with that ID.")
except ValueError:
    print("Invalid input. Please enter a numerical ID.")

# d) Print the list of all the Developers of Infosys
print("\n--- List of Developers ---")
developers = df_emp[df_emp['Designation'] == 'Developer']
print(developers)
