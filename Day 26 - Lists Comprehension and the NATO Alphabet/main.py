import random
import pandas
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Freddie"]
#
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)
#
# passed_studens = {student:score for (student, score) in students_scores.items() if score >= 60}
#
# print(passed_studens)
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)
#
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
#
# print(weather_f)
#
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# student_dataframe = pandas.DataFrame(student_dict)
# print(student_dataframe)
#
dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for (index, row) in dataframe.iterrows()}
#
# print(nato_alphabet)
#
word = input("Enter a word: ").upper()
result = [nato_alphabet[letter] for letter in word]
print(result)