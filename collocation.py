#!/usr/bin/env python
# -*- coding: utf-8

from nltk.corpus import PlaintextCorpusReader
from nltk.text import Text
from nltk.collocations import BigramCollocationFinder
from nltk.collocations import BigramAssocMeasures
from nltk.tokenize import LineTokenizer

corpus_root = './data'
fileids = 'data_title_sample'
distance = 5

corpus = PlaintextCorpusReader(corpus_root,
    fileids,
    sent_tokenizer=LineTokenizer(),
    encoding='utf-8')

bgm = BigramAssocMeasures()

finder = BigramCollocationFinder.from_words(corpus.words(), distance)
scored = finder.score_ngrams(bgm.raw_freq)

prefix_keys = {}

for pair, score in scored:
  word1, word2 = pair
  value = prefix_keys.setdefault(word1, []) + [(word2, score)]
  prefix_keys[word1] = value

for keyword, wordlist in prefix_keys.items() :
  try :
    print keyword, [(word.encode('utf-8'), scored) for (word, scored) in wordlist]
  except :
    pass
