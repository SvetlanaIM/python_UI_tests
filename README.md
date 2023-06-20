#### This project contains automated UI tests using Page Object Model (POM).

- URL: https://selenium1py.pythonanywhere.com/
- Programming language: Python
- Tools used: pytest, Selenium Webdriver

#### To run the tests locally, follow these steps:
1.	Clone the project repository.
2.	Open the repository's directory.
3.	Install the required dependencies:
```
pip install --no-cache-dir -r requirements.txt
```

The tests can be run on Chrome or Firefox, and in different languages (the default browser is Chrome with English language):
```
pytest -v --tb=line
```

To run the tests on Firefox in Russian (or any other language of your choice), use the following command:
```
pytest -v --tb=line --language=ru --browser_name=firefox 
```

Ensure that you have the appropriate version of the Firefox driver installed and configured as well.
