# List comprehension

numbers = [1,2,3]
new_numbers = [number+1 for number in numbers]

name = "Eduardo"
name_list = [letter for letter in name]

new_range = [n*2 for n in range(1,5)]

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_names = [name.upper() for name in names if len(name) >= 5]

import random
students_scores = {student:random.randint(1, 100) for student in names}

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionary
# for (key, value) in student_dict.items():
#     print(value)

import pandas as pd

# student_data_frame = pandas.DataFrame(student_dict)
#
# print(student_data_frame)


# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # print(row.student)
#     if row.student == "Angela":
#         print(row.score)


# PROJECT

# TODO 1. Create a dictionary in this format
# {"A": "Alfa", "B": "Bravo"}

alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter : row.code for (_, row) in alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs
word = input("Enter a word:\n")

word_list = [alphabet[letter.upper()] for letter in name]
print(word_list)
