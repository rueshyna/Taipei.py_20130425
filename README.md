# Taipei.py_20130425

Demo at Taipei.py on 2013/04/05.

Slides : http://www.slideshare.net/rueshyna/text-mining-20087054

Video : https://www.youtube.com/watch?v=svGf5Vxyx60&feature=c4-feed-u

### Notification

If you have large data then you take more time to run program...

### Requirement

  - [Nltk](http://nltk.org/)
  - [Numpy](http://www.numpy.org/)
  - [Matplot](http://matplotlib.org/)

### Data

I used title column in train-sample file from [Stack Overflow](http://www.kaggle.com/c/predict-closed-questions-on-stack-overflow) as example in this talk.


## Demo 1 - Trem Frequency Analysis

It will count terms and plot a chart.

    > python freq.py

## Demo 2 - Tagged Sentence

Need to download tagged model first.

    >>> import nltk  
    >>> nltk.download('maxent_treebank_pos_tagger')

This model use [Penn Treebank II Tags](http://bulba.sdsu.edu/jeanette/thesis/PennTags.html) style.

    > python pos.py

## Demo 3 - Term Frequency with POS tag

In here, the Penn Treebank II Tags was too detail, so I simplified tags. Please refer to NLTK api doc for simplified tags.

    > python freq_pos.py

## Demo 4 - Collocation

In here, window size of collocation was set 5 which means it will observe next 5 words.

I forgot to preprocess lower case problem in this program, please careful about case problem.

    > python collocation.py

## Demo 5 - Make a Sentence

Use language model to make sentence.

    > python lm.py

