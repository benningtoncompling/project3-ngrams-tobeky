#!/usr/bin/env python3

import nltk
import math
sentences = []


def open_files():
    with open("dickens_training.txt", "r") as input_file:
        for line in input_file.readlines():
            text = line.lower()
            text = text.replace("\n", "")
            sentence = "<s> " + text + " </s>"
            sentences.append(sentence)
        return sentences


formatted_text = open_files()


#   Unigrams
def unigrams(sentences):
    uni_dictionary = {}
    uni_word_total = 0
    for sentence in sentences:
        for word in sentence.split(" "):
            if word not in uni_dictionary:
                uni_dictionary[word] = 1
                uni_word_total += 1
            elif word in uni_dictionary:
                uni_dictionary[word] = uni_dictionary[word] + 1
                uni_word_total += 1
    return uni_dictionary, uni_word_total


def reformat_list(sentences):
    all_unigrams = []
    for sentence in sentences:
        all_unigrams += sentence.split(" ")
    return all_unigrams


new_sentences = reformat_list(sentences)
bigrams = nltk.bigrams(new_sentences)


def bigramifier(bigrams):
    bi_tally = 0
    bi_everything = 0
    bi_dictionary = {}
    for bigram in bigrams:
        if bigram[0] == "</s>":
            continue
        bi_everything += 1
        if bigram[0] not in bi_dictionary:
            bi_dictionary[bigram[0]] = {}
        if bigram[1] not in bi_dictionary[bigram[0]]:
            bi_dictionary[bigram[0]][bigram[1]] = 1
            bi_tally += 1
        elif bigram[1] in bi_dictionary[bigram[0]]:
            bi_dictionary[bigram[0]][bigram[1]] += 1
    return bi_dictionary, bi_tally, bi_everything


def trigraminator(new_sentences):
    return new_sentences


print("\\data\\")
(uni_result, uni_total) = unigrams(sentences)
uni_types = len(uni_result)
print("ngram 1: types= " + str(uni_types) + " tokens= " + str(uni_total))

(bi_result, bi_types, bi_tokens) = bigramifier(bigrams)
print("ngram 2: types= " + str(bi_types) + " tokens= " + str(bi_tokens))

print("ngram 3: types= " + " tokens= ")

print("\\1-grams")
for key in uni_result:
    count = uni_result[key]
    prob = float(count) / uni_total
    log_prob = math.log10(prob)
    unig = key
    print(str(count) + " " + str(prob) + " " + str(log_prob) + " " + str(key))

print("\\2-grams")
for key in bi_result:
    for key2 in bi_result[key]:
        bicount = bi_result[key][key2]
        biprob = float(bicount) / uni_result[key]
        bilog_prob = math.log10(biprob)
        bikeys = str(key + " " + key2)
    print(str(bicount) + " " + str(biprob) + " " + str(bilog_prob) + " " + bikeys)

print("\\3-grams")
