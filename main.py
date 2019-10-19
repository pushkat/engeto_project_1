'''
author = Jana Pušová
'''
texts = [
    '''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''', 

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

users = {
    'bob' : '123',
    'ann' : 'pass123',
    'mike' : 'password123',
    'lizz' : 'pass123'
    }

# Greeting user
print()
print('-' * 60)
print('WELCOME TO THE TEXT ANALYZER')
print('-' * 60)
print()

# Checking credentials, showing texts to be selected
print('YOUR CREDENTIALS:')
username = input('Username: ')

if username not in users:
    print("Username doesn't exist, try again")
else:
    password = input('Password: ')
    if users[username] == password:
        print('-' * 60)
        print('ACCESS GRANTED')
        print('-' * 60)
        print()
        print('OUR TEXTS: ')
        print('1: ' + str(texts[0]))
        print()
        print('2: ' + str(texts[1]))
        print()
        print('3: ' + str(texts[2]))
        print()
    else:
        print('ACCESS DENIED')
        exit()

# Getting number of text to be analyzed
choice = int(input('Please select the requested text (1, 2, 3): '))
print()
if choice not in [1, 2, 3]:
    print('Wrong number, try again')
else:
    print('-' * 60)
    print('STATISTICS FOR THE TEXT NUMBER ' + str(choice) + ':')
    print('-' * 60)

# Statistics: number of words in total
preselection = texts[choice-1].split(' ')
selection = [x.replace(',','').replace('.','').strip() for x in preselection]
print('Number of words in total: ' + str(len(selection)))

# Statistics: number of words starting with capital
titled = 0
i = 0

while i < len(selection):
    if selection[i].istitle():
        titled += 1
        i += 1
    else:
        i += 1
        continue
print('Number of words starting with capital letter: ' + str(titled))

# Statistics: number of uppercase words
uppercase = 0
i = 0

while i < len(selection):
    if selection[i].isupper() and selection[i].isalpha():
        uppercase += 1
        i += 1
    else:
        i += 1
        continue
print('Number of uppercase words: ' + str(uppercase))

# Statistics: number of lowercase words
lowercase = 0
i = 0

while i < len(selection):
    if selection[i].islower():
        lowercase += 1
        i += 1
    else:
        i += 1
        continue
print('Number of lowercase words: ' + str(lowercase))

# Statistics: number of numeric-only words
numeric = 0
numbers = []
i = 0

while i < len(selection):
    if selection[i].isnumeric():
        numeric += 1
        numbers.append(float(selection[i])) 
        i += 1
    else:
        i += 1
        continue
print('Number of numeric-only words: ' + str(numeric))
print('-' * 60)

# Statistics: bar charts - frequencies of word lengths in the text
lenght = [len(x) for x in selection]
unique = list(set(lenght))
    
i = 0
    
while unique:
    if i < len(unique):
        lenght.count(unique[i])
        print(str(unique[i]) + ' ' + str(lenght.count(unique[i]) * '*') + ' ' + str(lenght.count(unique[i])))
        i += 1
    else:
        break
                
print('-' * 60)

# Statistics: sum of numeric words
print('Sum of all numeric words: ' + str(sum(numbers)))
print('-' * 60)
print()

# End of statistics
print('THANK YOU FOR USING OUR TEXT ANALYZER!')
print()