
# LINGOPEDIA 

## A Web-based Dictionary for IIT Kharagpur Lingo

Lingopedia is a Flask-based web application that serves as a dictionary for the unique lingo used at IIT Kharagpur. It allows users to search for definitions of specific words or phrases commonly used within the IIT Kharagpur community.


## Features

- Search for word definitions: Users can enter a word or phrase in the search bar to retrieve its definition from the dictionary.
- Fuzzy search: If the exact word is not found, Lingopedia suggests similar words that closely match the user's input.
- Interactive user interface: The application provides an intuitive user interface that allows users to easily search for definitions and view the results.

## Requirements

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

## Installation

1. Clone the repository to your local machine :
   ```bash
   git clone https://github.com/rushisurya2705/KGP-LINGO.git
   ```

2. Navigate to the project directory:
    ```bash
    cd KGP-LINGO
    ```

3. Install the required Python packages using pip :
   ```bash
   pip install -r requirements.txt
   ```
3. Delete `output.json` file from your device.

4. Run the `scraping_to_json.py` script to make output.json file  :
   ```bash
   python -u scraping_to_json.py
   ```
5. Run `app.py` to check the working of server

## Usage

1. Run the Flask application:

```bash
flask --app app run
```
2. Open your web browser and access the application at `http://127.0.0.1:5000`.

3. Enter a word or phrase in the search bar and click "Search" to retrieve its definition.
4. 
## Contributing

Contributions to Lingopedia are welcome! If you'd like to contribute to the project, please follow these steps:

- Fork the repository on GitHub.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive commit messages.
- Push your changes to your forked repository.
- Submit a pull request to the main repository.


## User Interface

The application provides a web-based user interface for searching Lingo words and retrieving information about them. Simply enter the Lingo word or similar word in the search box, click "Search", and a list of matching words will be displayed. Click on a Lingo word to view additional details.
For Demo : visit `https://lingopedia.onrender.com`

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

[@rushisurya2705](https://github.com/rushisurya2705)


