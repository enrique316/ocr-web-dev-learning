"""
What does accessing nested dictionary mean?

👉 It means:

“Getting values from dictionaries inside dictionaries”

👉 Since nested dictionaries contain multiple levels:

we access them level by level.

2. Basic syntax
dictionary[outer_key][inner_key]
3. Basic example
d = {
    'student': {
        'name': 'John',
        'age': 25
    }
}

print(d['student']['name'])
"""

data = {
    'name': {
        'shubhankar': True, 
        'Dimple': False
    }
}
print(data['name']['shubhankar'])

# another example # 

School = {
    'class':{
        'Section':{
           'A1': "35_Students",
           'A2': "32 Students"
        }

    }
}
print(School)
print(School['class']['Section']['A2'])