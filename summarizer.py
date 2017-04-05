# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import os

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
# from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "portuguese"
SENTENCES_COUNT = 2


if __name__ == "__main__":
    # for urls
    # url = "http://www.zsstritezuct.estranky.cz/clanky/predmety/cteni/jak-naucit-dite-spravne-cist.html"
    # parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    for root, dirs, files in os.walk("PriberamCompressiveSummarizationCorpus/PT2012-2013/docs/"):
        for filename in files:
            if filename.endswith(".sents"):
                file_path = os.path.join(root, filename)
                print(file_path)

                print()
                parser = PlaintextParser.from_file(file_path, Tokenizer(LANGUAGE))
                stemmer = Stemmer(LANGUAGE)

                for summarizer in [LsaSummarizer, TextRankSummarizer, LexRankSummarizer, SumBasicSummarizer, LuhnSummarizer]:
                    print(summarizer.__name__)
                    summarizer = summarizer(stemmer)
                    summarizer.stop_words = get_stop_words(LANGUAGE)

                    for sentence in summarizer(parser.document, SENTENCES_COUNT):
                        print(sentence)
                    print()
                print("------------------------------------------------------------------------------")