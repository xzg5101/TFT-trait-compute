import json
import pickle
import urllib.request
import urllib3
import codecs
import html2text
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import re
import itertools

patch = "13.9.1"

CHAMP_PATH = "data/champ.html"
TRAIT_PATH = "data/trait.html"

def load_champs(path:str)->list:
    htmlFile = open(path, "r")
    soup = BeautifulSoup(htmlFile, 'html.parser')
    l = soup.get_text()
    l = l.replace(' ', '.')
    l = l.replace('\n', ' ')
    K = '@'
    rep = re.sub(r'\d', K, l)
    champs = rep.split(K)

    cl = [i.split() for i in champs]
    cl2 = [[i.replace('.', '') for i in k if len(i.replace('.', '')) > 0] for k in cl]
    cl3 = [[i[0], i[1:]] for i in cl2 if len(i) > 1]
    print(cl3)
    return cl3


def load_traits(path:str)->list:
    htmlFile = open(path, "r")
    soup = BeautifulSoup(htmlFile, 'html.parser')
    l = soup.get_text()
    l2 = l.split('\n')
    l3 = [i.strip() for i in l2 if len(i.split()) == 1 and not i[-1] == '.' ]
    for i, j in enumerate(l3):
        if i > 0 and not j.isnumeric() and not l3[i-1].isnumeric():
            l3.remove(j)
    for i, j in enumerate(l3):
        if not j.isnumeric():
            l3[i] = "@ " + l3[i]
    
    l4 = [i.split() for i in l3]
    l5 = [item for sublist in l4 for item in sublist]
    l6 = [int(i) if i.isnumeric() else i for i in l5]
    l7 = [list(y) for x, y in itertools.groupby(l6, lambda z: z == '@') if not x]
    l8 = [[i[0], i[1:]] for i in l7 if len(i) > 1]
    print(l8)

def count_trait(champs: list, traits: list)->int:
    pass

champs = load_champs(CHAMP_PATH)
trait = load_traits(TRAIT_PATH)

