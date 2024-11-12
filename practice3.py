# Program 3: Create a dictionary to store a person's information from user input
def person_info():
    person = {}
    person['name'] = input("Enter your name: ")
    person['age'] = input("Enter your age: ")
    person['favorite_color'] = input("Enter your favorite color: ")
    return person


# Program 3
person = person_info()
print("Person Information:", person)