""" Overview """
# Write a Python program that:
# Stores information about employees in a list of dictionaries.

"""Each dictionary should have the following keys:"""
# "name" → employee name
# "department" → e.g., Sales, IT, HR, etc.
# "salary" → monthly salary(integer)
# "years_of_service" → number of years they’ve worked

"""Performs analysis to find:"""
# The average salary across all employees.
# The highest and lowest salary and the corresponding employee(s).
# The total salary paid by the company.
# The average salary per department.
# Any employee(s) who qualify for a 5 % bonus (if they’ve worked for ≥ 5 years).


""" Test case """
# {"name": "Alice Johnson", "department": "Sales", "salary": 4500, "years_of_service": 6},
# {"name": "Bob Smith", "department": "IT", "salary": 5200, "years_of_service": 3},
# {"name": "Charlie Brown", "department": "HR", "salary": 4100, "years_of_service": 5},
# {"name": "Diana Prince", "department": "Sales", "salary": 4800, "years_of_service": 8},
# {"name": "Ethan Hunt", "department": "IT", "salary": 6000, "years_of_service": 10},
# {"name": "Fiona Wells", "department": "HR", "salary": 3900, "years_of_service": 2}


""" =========================================================================================================== """

try:
    # Get number of employees needed for this analysis
    numEmployee = int(
        input("Number of employee information to be provided: \n"))

    """ Check if number of employee is not empty"""
    if numEmployee < 1:
        print("Number of employee can not be zero(0)!")
        exit()
    else:
        bonusYear = int(input(
            "How many years of service does an employee needs to qualify for bonus?: \n"))

except ValueError:
    print("You entered a wrong value, it must be an integer")

else:
    employeeData = []  # Hold employeed records
    employeeSalary = []  # Hold Salary information for employees

    # Get informations about employees
    for i in range(numEmployee):
        name = input(f"Name of employee {i+1}: \n").title().strip()
        department = input(f"{name}'s Department: \n").strip()
        salary = int(input(f"{name}'s Salary: \n"))
        years_of_service = int(input(f"{name}'s years in service: \n"))

        # store each information in a dictionary
        employee_dic = {
            "name": name,
            "department": department,
            "salary": salary,
            "years_of_service": years_of_service
        }

        # store each employee record in a general data
        employeeData.append(employee_dic)

        # Print line break to differentiate each employee
        print("="*96)

    def salaryEmployee():
        """ create function to find total and average salary across company """

        totalSalary = 0  # -- Holds total salary
        for emp in employeeData:
            totalSalary += emp["salary"]

        # Find the average salary
        avgSalary = round(totalSalary/len(employeeData), 2)

        # Value to be returned by the function
        return totalSalary, avgSalary

    def lowHighSalary():
        # Store each employee's salary in list
        empSalaries = sorted([emp["salary"] for emp in employeeData])
        lowestName = ""
        highestName = ""

        # Get employees that are either lowest earner or highest earner
        # Lowest employee(s)
        lowestEarner = [emp["name"]
                        for emp in employeeData if emp["salary"] == empSalaries[0]]
        # Highest employee(s)
        highestEarner = [emp["name"]
                         for emp in employeeData if emp["salary"] == empSalaries[-1]]

        # Get name of lowest name as string
        for i in range(len(lowestEarner)):
            lowestName = (lowestName + " " +
                          lowestEarner[i]).strip().replace(" ", ", ")

        # Get name of highest name as string
        for i in range(len(highestEarner)):
            highestName = (highestName + " " +
                           highestEarner[i]).strip().replace(" ", ", ")

        return empSalaries[0], empSalaries[-1], lowestName, highestName

    def avgDeptSalary():
        """ This function calculate the average salary of each department"""

        empDept = []  # Hold employee department

        # Get all department for submitted employee
        for emp in employeeData:
            if emp["department"] not in empDept:
                empDept.append(emp["department"])

        # Find the average salary of each department
        for dept in empDept:  # Loop through each department list
            totalDeptSalary = 0
            deptEmp = 0
            for emp in employeeData:  # loop through each employee record
                # check if the employee dept record matches the current department in check
                if emp["department"] == dept:
                    # Add up salary if it matches
                    totalDeptSalary += emp["salary"]
                    deptEmp += 1  # count the numbers of employee

            # Print each department average salary
            print(f"--> {dept}: £{round(totalDeptSalary/deptEmp, 2)}")

    def empBonus():
        """ Any employee(s) who qualify for a 5% bonus (if they’ve worked for ≥ bonusYears specified) """
        qualified = [emp['name']
                     for emp in employeeData if emp["years_of_service"] >= bonusYear]

        # print out qualified name
        if len(qualified) > 0:
            for name in qualified:
                print(f"--> {name}")
        else:
            print("No employee qualified")

    """ Get values from all functions for analysis"""
    totalSalary, avgSalary = salaryEmployee()
    lowestSalary, highestSalary, lowestEarner, highestEarner = lowHighSalary()

    """                                              
        ---> Print out all Analysis reports 
    """
    # Print line break to differentiate each employee
    print("="*96)

    # Prints total salary paid by company
    print(f"Total Salary Paid: £{totalSalary}")

    # Prints average salary across company
    print(f"Average Salary: £{avgSalary}")

    # Prints lowest salary and earner(s)
    print(f"Lowest Salary: £{lowestSalary} ({lowestEarner})")

    # Prints highest salary and earner(s)
    print(f"Highest Salary: £{highestSalary} ({highestEarner})")

    # Prints average salary of each department
    print(f"Average Salary per Department:")
    avgDeptSalary()  # -- Function to calculate average salary per department

    # Prints employees eligible for 5% bonus
    print(f"Employees Eligible for Bonus:")
    empBonus()  # -- Function to calculate eligible employees
