#!/usr/bin/env python
# -*- coding: utf-8

import nltk
from nltk.probability import FreqDist
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import LineTokenizer

OUTPUTFILE = './data/tagged_sent'

pair_str_pos = lambda x : '/'.join(x)

corpus_root = './data'
fileids = 'data_title_sample'

corpus = PlaintextCorpusReader(corpus_root,
    fileids,
    sent_tokenizer=LineTokenizer(),
    encoding='utf-8')

output = open(OUTPUTFILE,'w')

for sent in  corpus.sents() :
  tokens = map(pair_str_pos,nltk.pos_tag(sent))
  sent = ' '.join(tokens)
  output.write(sent+"\n")
