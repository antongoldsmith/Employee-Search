employees = {
    'Adam' : '001',
    'Brian' : '002',
    'Carl' : '003',
    'David' : '004',
    'Earl' : '005',
    'Frank' : '006'
    }
reversed_roster = dict(map(reversed, employees.items())) # reverses order
# so ID number becomes keys

def emp_name_search(): # searching by employee's name
    emp_name = input('Enter name of employee: ')
    if emp_name in employees:
        print(f"{emp_name}'s ID Number is {employees[emp_name]}.")
    else:
        print(f"{emp_name} is not on the roster.")
        return emp_name_search()

def emp_id_search(): # searching by employee's id number
    emp_id = input('Enter ID Number of employee: ')
    res = dict((v,k) for k,v in employees.items())
    if emp_id in reversed_roster:
        print(f"ID Number {emp_id} belongs to {res[emp_id]}.")
    else:
        print(f"ID Number {emp_id} is not on the roster.")
        return emp_id_search()

def name_or_id(): # determines to search by name or id number
    search = input('Are you searching by name or ID? ')    
    if search == 'name':
        emp_name_search() # initiates search by name
    if search == 'id':
        emp_id_search() # initiates search by id number
name_or_id()
