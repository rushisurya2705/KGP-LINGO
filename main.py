import json
from fuzzywuzzy import fuzz, process

# Open the JSON file and load the data into a dictionary
with open('output.json') as f:
    data = json.load(f)


# Function to perform a binary search in the dictionary
def binary_search(word_):
    sorted_keys = sorted(data.keys())
    left = 0
    right = len(sorted_keys) - 1

    while left <= right:
        mid = (left + right) // 2
        current_key = sorted_keys[mid]
        if current_key.casefold() == word_.casefold():
            print(data[current_key])
            return 1
        elif current_key.casefold() < word_.casefold():
            left = mid + 1
        else:
            right = mid - 1

    return 0

# Prompt the user to enter a word
word__=input("Enter Lingo: ")

# Fuzzywuzzy require data in list format
word_list = list(data.keys())

# Perform the binary search
if binary_search(word__)==0:
    print("Lingo not found!")

    # Find similar words using process.extract() method of fuzzywuzzy library
    # In this format we get 2 values {similar_word, similarity%}, so we have to handle that carefully.
    similar_words_list = process.extract(word__, word_list)
    similar_words_list = similar_words_list[1:]
    if len(similar_words_list):
        para=1
        print("Did you mean?")
        for i in similar_words_list:
            # print(str(para) + "." + i + "   ", end=" ")
            if i[1]>=65:
                print(f"{para}.{i[0]}   ", end=" ")
                para += 1
        choice=input("\nPress N if No or enter choice number, (default is N) : ")
        if choice.isdigit() and int(choice) < para:
            choice = int(choice) - 1
            binary_search(similar_words_list[choice][0])
        elif choice not in ('N', 'n'):
            while True:
                print("Your input is not valid. Please provide a correct input")
                choice=input("\nPress N if No or enter choice number, (default is N) : ")
                if choice.isdigit() and int(choice) < para:
                    choice = int(choice) - 1
                    binary_search(similar_words_list[choice][0])
                    break
                elif choice in ('N', 'n'):
                    break
