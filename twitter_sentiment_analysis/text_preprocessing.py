import json

# with open('python.json','r') as f:
#     line = f.readline()
#     tweet = json.loads(line)
#     print json.dumps(tweet,indent = 4)


# from nltk.tokenize import word_tokenize
 
# tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
# print(word_tokenize(tweet))
# # ['RT', '@', 'marcobonzanini', ':', 'just', 'an', 'example', '!', ':', 'D', 'http', ':', '//example.com', '#', 'NLP']

import re
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 
tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
print(preprocess(tweet))

from nltk.corpus import stopwords
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['RT','via']

import operator
from collections import Counter

# with open('python.json', 'r') as f:
#     count_all = Counter() 
#     for line in f:
#         tweet = json.loads(line)
#         terms_all  =[ term for term in preprocess(tweet['text']) if term not in stop]
#         count_all.update(terms_all)

#     print count_all.most_common(5)
    
f = open('python.json','r') 
counter = Counter()
search_word ="Dhoni"
from collections import defaultdict
com = defaultdict(lambda : defaultdict(int))
for line in f:
    tweet = json.loads(line)
    terms_only = [term for term in preprocess(tweet['text']) if term not in stop and not term.startswith(('#','@'))]
    # print terms_only
    if search_word in terms_only:
        counter.update(terms_only)

    for i in range(len(terms_only)-1):
        for j in range(i+1,len(terms_only)):
            w1,w2 = sorted([terms_only[i],terms_only[j]])
            if w1!= w2:
                com[w1][w2] +=1
                
print  counter.most_common(20)

com_max = []
for t1 in com:
    t1_max_terms = sorted(com[t1].items(),key = operator.itemgetter(1),reverse=True)[:5]
    for t2,t2_count in t1_max_terms:
        com_max.append(((t1,t2),t2_count))
terms_max = sorted(com_max, key=operator.itemgetter(1),reverse=True)
print terms_max[:1000]




