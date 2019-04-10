#!/usr/bin/env python3

from random import random
import build_ngram_model

coefficient = random()
print(coefficient)


def make_dictionaries():
    unigram_dict = {}
    return unigram_dict


def unigrams():
    sentence = "<s> "
    current = ""
    prob_total = 0
    probability = 0.5
    while current is not "</s>":
        if prob_total > coefficient:
            prob_total += probability(current)
        if prob_total <= coefficient:
            sentence += current
            sentence += " "
    sentence += " </s>"
    return sentence


#   i need to make dictionaries from the other file that are (ngram, probability) ??
#   i think my unigram function makes sense logically though? as soon as probability(current) means something

