#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != '':
        char_1 = sentence[0]
    else:
        char_1 = None
    return (len(sentence), char_1)
