from flask import Flask, render_template, request
import json
from fuzzywuzzy import fuzz, process

app = Flask(__name__)

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
            return data[current_key]
        elif current_key.casefold() < word_.casefold():
            left = mid + 1
        else:
            right = mid - 1

    return None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word_ = request.form['word']
        definition = binary_search(word_)
        if definition:
            return render_template('index.html', word=word_, definition=definition)
        else:
            word_list = list(data.keys())
            similar_words_list = process.extract(word_, word_list)
            similar_words_list = similar_words_list[1:]
            similar_words = [similar_word[0] for similar_word in similar_words_list if similar_word[1] >= 75]
            return render_template('index.html', word=word_, similar_words=similar_words)
    else:
        return render_template('index.html')


@app.route('/definition/<word>')
def definition(word):
    result = binary_search(word)
    if result:
        return render_template('definition.html', word=word, definition=result)
    else:
        return "Definition not found for the word."


if __name__ == '__main__':
    app.run(debug=True)
