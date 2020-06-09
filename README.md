# The bot project
### A simple chatbot application
This is a small app working out how to use the NLTK package within a Django app.

#### Installation
1. Clone and cd into the cloned dir
2. Create a new pipenv: `pipenv sync`
3. Download the necessary NLTK-data:
    
    - Use the NLTK Downloader to obtain the resources
    - In your pipenv dir type: `python` to start the interpreter
    - Type the following to satisfy the dependencies
    - `>>> import nltk`
    - `>>> nltk.download('punkt')`
    - `>>> nltk.download('averaged_perceptron_tagger')`

4. Start the django server with `./manage.py runserver`