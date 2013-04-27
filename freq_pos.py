#!/usr/bin/env python
# -*- coding: utf-8

from nltk.probability import ConditionalFreqDist
from nltk.corpus import TaggedCorpusReader
from nltk.tag import simplify

FIRST = 0
END = 150
POS = "V"
#POS = "N"
#POS = "ADJ"

corpus_root = './data'
fileids = 'tagged_sent'

corpus = TaggedCorpusReader(corpus_root,
    fileids,
    encoding='utf-8')

processing = [(simplify.simplify_wsj_tag(tag), word.lower()) for (word, tag) in corpus.tagged_words()]
cfd_corpus = ConditionalFreqDist(processing)

for term,freq in cfd_corpus[POS].items():
  print term.encode("utf-8"),freq
