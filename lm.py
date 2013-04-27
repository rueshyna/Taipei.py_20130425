#!/usr/bin/env python
# -*- coding: utf-8

from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import LineTokenizer
from nltk.model import NgramModel
from nltk.probability import LidstoneProbDist
import pickle

corpus_root = './data'
fileids = 'data_title'
example = ["Python", "is"]

corpus = PlaintextCorpusReader(corpus_root,
    fileids,
    sent_tokenizer=LineTokenizer(),
    encoding='utf-8')

est = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
lm = NgramModel(3, corpus.words(), estimator=est)

sent = lambda n, example: ' '.join(lm.generate(n, example))

print "Let's make a sentence!!!"
print "give a seed : Python is ..."
print "sentence :"
print sent(5, example)

