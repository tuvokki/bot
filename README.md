# The bot project
### A simple chatbot application
This is a small app working out how to use the NLTK package within a Django app.

#### Installation
1. Clone and cd into the cloned dir
2. Create a (new) pipenv: `pipenv sync`
3. Use the NLTK Downloader to obtain the necessary data:
    - In your pipenv dir type: `python` to start the interpreter
    - Type the following to satisfy the dependencies
    - `>>> import nltk`
    - `>>> nltk.download('punkt')`
    - `>>> nltk.download('averaged_perceptron_tagger')`
4. Start the django server with `./manage.py runserver`

There is no need to migrate the database and/or create a super user since the data is already in the sqlite db file.
Logging in to the admin can be done with:

    username: wouter
    password: 1qaz2wsx

#### Importing questions
Create a csv file with the following format:

    answer,intent_name,pointers|separated|by|pipes

Read the file with the following manage-command:

    ./manage.py import_keywords --path ./data.csv

You can add comments by starting a line with a `#`
 