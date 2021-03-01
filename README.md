# Information Retrieval at Innopolis University

This repository aggregates reading materials, lab templates, datasets and other electronic resourses useful to learn about search, recommendations and other IR things.

## Reading
- In 2021, there is still [THE BOOK](https://nlp.stanford.edu/IR-book/information-retrieval-book.html) which is both good and old. That is why this book is mandatory reading, because it covers all necessary topics. But unfortunately it was written right before multimedia retrieval, recommender systems and machine learning became a common place.

- Latent space approximation is an important topic, you can refer to discussion of [ALS](http://stanford.edu/~rezab/classes/cme323/S15/notes/lec14.pdf), [Word2Vec](https://arxiv.org/abs/1301.3781), [BERT](https://arxiv.org/abs/1810.04805).

- Indexing is the blood system of search. [Proximity graphs](http://math.sfsu.edu/beck/teach/870/brendan.pdf) lay on the 0th level of theory. Higher you will find NSW and [HNSW](https://arxiv.org/abs/1603.09320) graphs. In search trees don't forget to read about [Annoy](https://github.com/spotify/annoy). For modern inverted indices please refer to [this paper](https://arxiv.org/abs/1802.02422) and it's [predecessor](http://sites.skoltech.ru/app/data/uploads/sites/25/2014/12/TPAMI14.pdf).

- Written in 2003, still important paper of audio retrieval from [Shazam creator](https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf). Also consider [Query by Humming](https://cs.nyu.edu/~eugenew/publications/humming-summary.pdf), [Hum to Search by Google](https://blog.google/products/search/hum-to-search/).

- Images refrieval start with low level features, like [SIFT](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform), [Haralick](https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_glcm.html) and [Xerox](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.104.2585&rep=rep1&type=pdf) features. And continues with machine learning with [classifiers](https://techblog.commercetools.com/reverse-image-search-with-machine-learning-92786a07c142) and [autoencoders](https://towardsdatascience.com/find-similar-images-using-autoencoders-315f374029ea).

- Topic modelling is usually a side topic for IR, but it is very important when things come to clustering, debiasing, analysis. To leading approaches are PLSA and LDA. Here are some interesting materials: [topic modelling (rus)](http://www.machinelearning.ru/wiki/images/2/22/voron-2013-ptm.pdf), [tutorials](http://machinelearning.ru/wiki/images/1/1f/Voron14aist.pdf), [LDA original paper](https://jmlr.org/papers/volume3/blei03a/blei03a.pdf).

## Other courses with slides and labs

- [Access this course](https://github.com/sebastian-hofstaetter/teaching), especially advanced part, if you want to know more about IR with neural networks.
- [Here you can find IR-related labs](https://github.com/uzairakbar/info-retrieval), e.g. on LDA.
