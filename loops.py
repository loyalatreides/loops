count = 0
while count < 5:
    print(count)
    count = count + 1

count = 6
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

count = 0
while count < 10:
    print(count)
    count = count + 1
    if count == 4:
        break # we use break when we like to get out of or stop the loop

count = 0
while count < 5:
    if count == 3:
        continue # we use continue statement to skip the current itertion, and continue with the next
    print(count)
    count = count + 1

#loop and list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

#loop and string
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

#loop and tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

#loop and dictionary
person = {
    'first_name': 'Kamran',
    'last_name': 'Habib',
    'age': 25,
    'country': 'Finland',
    'is_married': False,
    'skills': ['Python','SQL','HTML'],
    'address': {
        'street': 'Park Avenue',
        'city': 'New York City'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

#loop and set
it_companies = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
for company in it_companies:
    print(company)

#Break and Continue 2
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 4:
        break

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue #the step after the condition is skipped
    print('Next number should be ', number + 1) if number != 5 else print ("loop's end")
print('Outside the loop')

for iterator in range(0,20,2):
    print(iterator)

person = {
    'first_name': 'Kamran',
    'last_name': 'Habib',
    'age': 25,
    'country': 'Finland',
    'is_married': False,
    'skills': ['Python','SQL','HTML'],
    'address': {
        'street': 'Park Avenue',
        'city': 'New York City'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

for number in range(11):
    print(number)
else:
    print('The loop stops at', number)

#Exercise-Level-1
#1
for number in range(10):
    print(number)

count = 0
while count < 10:
   print(count)
   count = count + 1

#2
count = 10
while count > -1:
    print(count)
    count = count - 1
