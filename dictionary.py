#!/usr/bin/env python

import json
from difflib import get_close_matches as gcm

data_dict = json.load(open("data.json", "r"))

w = input("Please type the word to get its definition: ")

def definition_searcher(word):

    # to catch close matches if one of the letters of the word is typed by a suser in upper case, for instance Rain
    match_list_A = gcm(word.lower(), data_dict.keys(), cutoff=0.8)

    # to catch close matches if the searched word starts with a capital letter and user types it all in lower case, like Paris
    match_list_B = gcm(word.title(), data_dict.keys(), cutoff=0.8)

    # to catch close matches when a user types a word which should be all in uppercase but he/she makes a typo, for instance UUSA, NAATO
    match_list_C = gcm(word.upper(), data_dict.keys(), cutoff=0.7)

    # to concatenate the lists, later used to provide a user with options of close matches if a user makes a typo
    match_list_all = match_list_A + match_list_B + match_list_C
    match_list_all = list(set(match_list_all))

    # returns a definition of the word if user enters the searched term correcly
    if word.lower() in data_dict.keys():
        return data_dict[word]
    elif word.title() in data_dict.keys():
        return data_dict[word.title()]
    elif word.upper() in data_dict.keys():
        return data_dict[word.upper()]

    # offerring the user close matches if he/she makes a mistake in typing the word
    elif len(match_list_all) > 0:
        c = 1
        for word in match_list_all:
            print(f"{c} - {word}")
            c = c + 1

        user_q = input("Please pick a word from the options above by typing the number. Or type 0 if none of them is correct:")
        user_q = int(user_q)

        if user_q > 0:
            return data_dict[match_list_all[user_q - 1]]
        else:
            return "Sorry that we couldn't find the word."

    else:
        return "Sorry. We couldn't undestand your entry."

output = definition_searcher(w)

if type(output) == list:
    print(10 * "*")
    for line in output:
        print(line)
        print(10 * "*")
else:
    print(output)
