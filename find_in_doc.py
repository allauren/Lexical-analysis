from docx import Document
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import re
from docx.enum.text import WD_COLOR_INDEX
import copy
import inspect

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def tokenizer(line):
    ps = PorterStemmer()
    if type(line) == str :
        word_list = word_tokenize(line)
    else :
        word_list = line
    token = []
    for w in word_list:
        token.append(ps.stem(w))
    return token

def check_words(file, words):
    document = Document(file)
    newdoc = Document()
    print(words)
    twords = tokenizer(words)
    for paragraph in document.paragraphs :
        tsentence = tokenizer(paragraph.text)
        nparagraph = newdoc.add_paragraph()
        font = nparagraph.add_run().font
        nparagraph.paragraph_format.alignment = paragraph.paragraph_format.alignment
        for word in tsentence :
            found = 0
            for fword in twords :
                if fword == word:
                    found = 1
            if found :
                print('caca')
                nparagraph.add_run(word + ' ').bold = True
                print(font.highlight_color)
                font.highlight_color = WD_COLOR_INDEX.TURQUOISE
                print(font.highlight_color)
            else :
                nparagraph.add_run(word + ' ').bold = False
    newdoc.save('newdoc.docx')