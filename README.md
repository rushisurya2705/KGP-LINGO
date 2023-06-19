
# KGP LINGO

This project consists of two files: `main.py` `scraping_to_json.py`


It performs web scraping on a specific URL to extract Lingo words and their definitions from the website. The extracted data is stored in a JSON file, and the `main.py` file provides a command-line interface to search for Lingo words and display their definitions.

Used Algorithm for searching word : Binary search

Used library for finding similar word : fuzzywuzzy

The reference has been taken from: https://wiki.metakgp.org/w/Lingo_of_IIT_Kharagpur. With any change in the https://wiki.metakgp.org/w/Lingo_of_IIT_Kharagpur , the dictionary can be updated by running the scraping_to_json.py file.

## Installation

1. Clone the repository :
   ```bash
   git clone https://github.com/rushisurya2705/KGP-LINGO.git
   cd KGP-LINGO
   ```
2. Install the required dependencies using pip :
   ```bash
   pip install BeautifulSoup
   pip install requests
   pip install fuzzywuzzy
   ```
3. Run the scraping_to_json.py script to scrape lingo words from the website and store them in a JSON file :
   ```bash
   python -u scraping_to_json.py
   ```

## Usage

Run the main.py script to search for lingo words:
```bash
python -u main.py
```
The script will prompt you to enter a Lingo word. It will perform a binary search on the data in the `output.json` file and display the definition of the word if found. If the word is not found, it will suggest similar words and ask for your input to choose a word from the suggestions or enter 'N' or 'n' to indicate no match.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)


