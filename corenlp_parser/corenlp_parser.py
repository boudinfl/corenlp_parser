#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from lxml import etree

class MinimalCoreNLPParser:
    """ Minimal CoreNLP XML Parser in Python. """
    def __init__(self, path):
        self.sentences = []
        tree = etree.parse(path)
        for sentence in tree.xpath("/root/document/sentences/sentence"):
            self.sentences.append({
              "words" : [u.text for u in sentence.xpath("tokens/token/word")],
              "lemmas" : [u.text for u in sentence.xpath("tokens/token/lemma")],
              "POS" : [u.text for u in sentence.xpath("tokens/token/POS")]
            })

if __name__ == "__main__":
    parse = MinimalCoreNLPParser(sys.argv[1])
    for sentence in parse.sentences:
        print ' '.join(sentence["words"])