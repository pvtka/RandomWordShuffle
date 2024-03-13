import random
import re

word = input("Enter a word consisting of 5 lowercase letters: ")

while re.match("^[a-z]{5}$", word) == None:
    print("The string is invalid, please try again\n")
    word = input("Enter a word consisting of 5 lowercase letters: ")
else:
    print("The entered string is valid\n")

list_of_letters = list(word)
dictionary = {}

for i in range(0, 1200):
    random.shuffle(list_of_letters)
    string_from_list = "".join(list_of_letters)
    if (dictionary.get(string_from_list) == None):
        dictionary[string_from_list] = 1
    else:
        dictionary[string_from_list] += 1

# print(dictionary)

x = str(len(dictionary))

print("The number of letter combinations is: " + x)

max_value = 1
for i in dictionary:
    if dictionary[i] > max_value:
        max_value = dictionary[i]

min_value = max_value
for i in dictionary:
    if dictionary[i] < min_value:
        min_value = dictionary[i]

max_combinations = []
for i in dictionary:
    if dictionary[i] == max_value:
        max_combinations.append(i)

max_combinations_str = ', '.join(max_combinations)
print("The most frequent combination is: " + max_combinations_str)

min_combinations = []
for i in dictionary:
    if dictionary[i] == min_value:
        min_combinations.append(i)

min_combinations_str = ', '.join(min_combinations)

handle = open('result.txt', 'a')
handle.write("Input string: " + word + "\n")
handle.write("Dictionary: \n" + str(dictionary) + "\n")
handle.write("The most frequent combination is: " + max_combinations_str + " \n")
handle.write("The least frequent combination is: " + min_combinations_str + " \n")
handle.close()
