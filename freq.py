#!/usr/bin/env python
# -*- coding: utf-8

from nltk.probability import FreqDist
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import LineTokenizer

FIRST = 0
END = 150

corpus_root = './data'
fileids = 'data_title_sample'

wordlists = PlaintextCorpusReader(corpus_root,
    fileids,
    sent_tokenizer=LineTokenizer(),
    encoding='utf-8')

tokens = []
for word in wordlists.words() :
  try :
    tokens += [ word.lower() ]
  except :
    pass

fdist = FreqDist(tokens)

fdist.plot(FIRST,END)

for k,v in fdist.items() :
  print "{} {}".format(k.encode("utf-8"),v)
