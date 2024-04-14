import random

start_id = 100
first_names = ["John", "Jane", "Mark", "Emma"]
last_names = ["Smith", "Anderson", "Wilson", "Davis"]

def create_data():
    global start_id
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    dict = {
        'id': start_id,
        'employee_name': f"{first_name} {last_name}",
        'email': f"{first_name.lower()}{last_name.lower()}@email.com",
        'salary': round(random.gauss(70000, 5000)),
        'department': random.choice(["Sales", "Marketing", "Management", "Human Resources"]),
        'years_experience': random.randint(0, 30),
        'performance_rating': round(random.uniform(1, 5), 1)
    }
    
    start_id += 1
    return dict

def print_data(data):
    print(f"Id: {data['id']}")
    print(f"Name: {data['employee_name']}")
    print(f"Email: {data['email']}")
    print(f"Salary: {data['salary']}")
    print(f"Department: {data['department']}")
    print(f"Years experience: {data['years_experience']}")
    print(f"Performance rating: {data['performance_rating']}")