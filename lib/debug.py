#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    # print("HELLO! :) let's debug :vibing_potato:")
    author_1 = Author("Carry Bradshaw")
    author_2 = Author("Nathaniel Hawthorne")

    magazine_1 = Magazine("Vogue", "Fashion")
    magazine_2 = Magazine("AD", "Architecture")

    article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
    article_2 = Article(author_2, magazine_2, "Dating life in NYC")
    article_2 = Article(author_1, magazine_1, "Dating life in NYC")

    print(author_1.magazines())

    # don't remove this line, it's for debugging!
    # ipdb.set_trace()
