#!/usr/bin/python3
"""
Protype: text_indentation(text):
prints a text with 2 new lines after 
each of these characters: ., ? and :

"""

def text_indentation(text):
    """
    Returns a text with 2 new lines after 
    each of these characters: ., ? and :

    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    
    for textIndent in ".:?":
        text = (textIndent + "\n\n").join(
            [line.strip(" ") for line in text.split(textIndent)])

    print(f"{text}", end="")
