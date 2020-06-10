import logging

import nltk

logger = logging.getLogger(__name__)


def get_pointers_from_question(question):
    tokens = nltk.word_tokenize(text=question)
    pos_tagged = nltk.pos_tag(tokens)
    logger.debug(f"pos_tagged {pos_tagged}")
    nouns = list(filter(lambda x: x[1] == 'NN', pos_tagged))
    logger.debug(f"nouns {nouns}")
    verbs = list(filter(lambda x: x[1] == 'VB', pos_tagged))
    logger.debug(f"verbs {verbs}")

    pointers = [noun[0] for noun in nouns] + [verb[0] for verb in verbs]
    return pointers
