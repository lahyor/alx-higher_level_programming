#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        my_score = list(a_dictionary.keys())
        score = 0
        lead = ""
        for x in my_score:
            if a_dictionary[x] > score:
                score = a_dictionary[x]
                lead = x
        return lead
