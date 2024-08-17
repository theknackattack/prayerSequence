import csv

class Person:
    def __init__(self, id, first_name, last_name, suffix, date_of_birth, phone_number, christian_status, public_figure_status, status, description):
        self.id = int(id)
        self.first_name = first_name
        self.last_name = last_name
        self.suffix = suffix
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.christian_status = christian_status.lower() == 'true'
        self.public_figure_status = public_figure_status.lower() == 'true'
        self.status = status.lower() if status.lower() in {'alive', 'deceased', 'unknown'} else 'unknown'
        self.description = description

def print_selected_info(person, fields):
    for field in fields:
        if hasattr(person, field):
            value = getattr(person, field)
            print(f"{field.replace('_', ' ').title()}: {value}")
    print()
    

def main():
    csv_file = 'database.csv'
    people = []
    
    with open(csv_file, mode = 'r', newline = '') as file:
        reader = csv.DictReader(file)
        for row in reader:
            person = Person(
                id = row['id'],
                first_name = row['first_name'],
                last_name = row['last_name'],
                suffix = row['suffix'],
                date_of_birth = row['date_of_birth'],
                phone_number = row['phone_number'],
                christian_status = row['christian_status'],
                public_figure_status = row['public_figure_status'],
                status = row['status'],
                description = row['description']
            )
            people.append(person)
            
    fields_to_print = ['first_name', 'last_name', 'status']
    for person in people:
        print_selected_info(person, fields_to_print)

if __name__ == "__main__":
    main()