#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
12 December 2017
.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

User intents extracted from transcripts

'''
from fuzzywuzzy import fuzz

intents = {
            'greeting': [
                "hey",
                "hallo",
                "hi",
                "yo",
                "hello",
                ],

            'confirm': [
                "ja",
                "perfekt",
                "perfect",
                "exactly",
                "yes",
                "ok",
                "good",
                "correct",
                "great",
                "yea",
                "okay",
                "sure"
            ]
           }

test_greeting = [
                 "Hello, anybody there?",
                 "Hello?",
                 "Yo.",
                 "Hi?",
                ]


def match_intent(message, intent):
    message = message.lower()
    for sample in intents[intent]:
        # Edit distance of largest common substring (scaled)
        partial = fuzz.partial_ratio(message, sample)
        # print message, sample, partial
        if partial == 100:
            return True


def test_match_intent():
    for message in test_greeting:
        assert match_intent(message, 'greeting') == True


if __name__ == '__main__':
    test_match_intent()
