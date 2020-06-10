import click
import requests


@click.command()
@click.option('--question', prompt='Hello, how can I help you?',
              help='The question.')
def bot(question):
    click.echo(f"So you want to know: {question}")
    question_data = {'question': question}
    resp = requests.get('http://0.0.0.0:8000/api/search',
                        params=question_data)
    records = resp.json()
    answers = records['answers']
    print("Total rows are:  ", len(answers))
    for answer in answers:
        print(answer)
        print("\n")


if __name__ == '__main__':
    bot()
