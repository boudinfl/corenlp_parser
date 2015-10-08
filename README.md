# corenlp_parser

Minimal CoreNLP XML Parser in Python

A typical usage of this module is:

    from corenlp_parser import MinimalCoreNLPParser

    parse = MinimalCoreNLPParser('path/to/file')

    for sentence in parse.sentences:
        print ' '.join(sentence["words"])