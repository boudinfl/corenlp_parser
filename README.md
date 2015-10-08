# corenlp_parser

Minimal CoreNLP XML Parser in Python

To install this module:

    pip install git+https://github.com/boudinfl/corenlp_parser.git

A typical usage of this module is:

    from corenlp_parser import MinimalCoreNLPParser

    parse = MinimalCoreNLPParser('path/to/file')

    for sentence in parse.sentences:
        print ' '.join(sentence["words"])

