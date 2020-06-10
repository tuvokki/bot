import sqlite3

import click

import backend


@click.command()
@click.option('--question', prompt='Hello, how can I help you?',
              help='The question.')
def bot(question):
    click.echo(f"So you want to know: {question}")
    pointers = backend.get_pointers_from_question(question)
    try:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        intents_query = f"SELECT intent_id FROM 'BotApp_intentpointer' WHERE pointer in ({','.join(['?'] * len(pointers))})"
        cursor.execute(intents_query, pointers)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        for row in records:
            answers_query = f"SELECT answer FROM 'BotApp_intent' WHERE id={row[0]}"
            cursor.execute(answers_query)
            answer = cursor.fetchone()
            print(answer)
            print("\n")

        cursor.close()
    except sqlite3.Error as error:
        print(f"Cannot connect to data: {error}")
    finally:
        if (conn):
            conn.close()


if __name__ == '__main__':
    bot()
