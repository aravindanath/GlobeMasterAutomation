# Storing company Employee Table Data using a list and a Dict
# Try this program
Employees ={}


# Adding list into dictionary
Employees['EmployeeName'] = ['Ratan', 'Tata', 'Steve', 'Mark']
"""
Employees = {"YearOfJoining": 2019, 'Department': "ClaimsPro", 'JobTitle': "Senior Quality Analyst",
         'Location': 'Bangalore'}"""
Employees['YearOfJoining'] = 2019
Employees['Department'] = "ClaimsPro"
Employees['JobTitle'] = "Senior Quality Analyst"
Employees['Location'] = 'Bangalore'

# Adding dict into dict (nested dict)
Employees['Employee_ID']={'Ratan': 706260, 'Tata': 706261, 'Steve': 706262, 'Mark': 706263}

Employees['other_Details'] = {"JobType": 'FullTime', "ReportsTo": "Bill Gates"}
print("Employees Details: ", Employees)
print("Employee Name: ", Employees['EmployeeName'][0])
print("Employee ID:", Employees['Employee_ID']['Ratan'])
print("Employees Department: ", Employees['Department'])
print("Employees YearOfJoining: ", Employees['YearOfJoining'])
print("Employees JobTitle: ", Employees['JobTitle'])
print("Employee Manager:", Employees['other_Details']['ReportsTo'])




