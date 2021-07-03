guests = [
    'Andy',
    'Angela',
    'Sherry',
]
# dictionary
califonia_symbol = {
    'bird': 'califonia qucil',
    'animal': "califonai frog"
}

print(guests[1])
# itiration with the for loop
for guest in guests:
    print(guest)
# itiration through dictionary
print(califonia_symbol["animal"])

# iterate with the while loop
i = 5
print("counting numbers")
while i <= 100:
    print(i)
    i += 5
print('done!')

# name reverser
Surname = input('Enter your full name ')
print(Surname[::-1])
