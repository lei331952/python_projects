#!/usr/bin/env python

"""Retrieve and print words from a URL.

Usage:

python words.py <URL>
"""
from urllib.request import urlopen


def fetch_words(url: str):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of the UTF-8 text document.

    Returns:
        A list of strings containing the words from 
        the document
    """
    with urlopen(url) as story:
        story_words: list[str] = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_words(words: list[str]) -> None:
    """Print words in a list in one line separate by a space

    Args:
        words: a list of string
    """
    print(' '.join(words))


def main(url: str):
    """Print each word from a text document at a URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_words(words)


if __name__ == '__main__':
    import sys
    url: str = sys.argv[1]  # 'http://sixty-north.com/c/t.txt'
    main(url)
