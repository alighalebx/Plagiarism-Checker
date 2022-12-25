# n-gram char

import nltk

sent1 = "It might help to re-install Python if possible."
sent2 = "It can help to install Python again if possible."
sent3 = "It can be so helpful to reinstall C++ if possible."
sent4 = "help It possible Python to re-install if might."  # This has the same words as sent1 with a different order.
sent5 = "I love Python programming."

ng1_chars = set(nltk.ngrams(sent1, n=3))
ng2_chars = set(nltk.ngrams(sent2, n=3))
ng3_chars = set(nltk.ngrams(sent3, n=3))
ng4_chars = set(nltk.ngrams(sent4, n=3))
ng5_chars = set(nltk.ngrams(sent5, n=3))

jd_sent_1_2 = nltk.jaccard_distance(ng1_chars, ng2_chars)
jd_sent_1_3 = nltk.jaccard_distance(ng1_chars, ng3_chars)
jd_sent_1_4 = nltk.jaccard_distance(ng1_chars, ng4_chars)
jd_sent_1_5 = nltk.jaccard_distance(ng1_chars, ng5_chars)

print(jd_sent_1_2, "Jaccard Distance between sent1 and sent2 with ngram 3")
print(jd_sent_1_3, "Jaccard Distance between sent1 and sent3 with ngram 3")
print(jd_sent_1_4, "Jaccard Distance between sent1 and sent4 with ngram 3")
print(jd_sent_1_5, "Jaccard Distance between sent1 and sent5 with ngram 3")

# n-gram tokens
import nltk

sent1 = "It might help to re-install Python if possible."
sent2 = "It can help to install Python again if possible."
sent3 = "It can be so helpful to reinstall C++ if possible."
sent4 = "help It possible Python to re-install if might."  # This has the same words as sent1 with a different order.
sent5 = "I love Python programming."

tokens1 = nltk.word_tokenize(sent1)
tokens2 = nltk.word_tokenize(sent2)
tokens3 = nltk.word_tokenize(sent3)
tokens4 = nltk.word_tokenize(sent4)
tokens5 = nltk.word_tokenize(sent5)

ng1_tokens = set(nltk.ngrams(tokens1, n=3))
ng2_tokens = set(nltk.ngrams(tokens2, n=3))
ng3_tokens = set(nltk.ngrams(tokens3, n=3))
ng4_tokens = set(nltk.ngrams(tokens4, n=3))
ng5_tokens = set(nltk.ngrams(tokens5, n=3))

jd_sent_1_2 = nltk.jaccard_distance(ng1_tokens, ng2_tokens)
jd_sent_1_3 = nltk.jaccard_distance(ng1_tokens, ng3_tokens)
jd_sent_1_4 = nltk.jaccard_distance(ng1_tokens, ng4_tokens)
jd_sent_1_5 = nltk.jaccard_distance(ng1_tokens, ng5_tokens)

print(jd_sent_1_2, "Jaccard Distance between tokens1 and tokens2 with ngram 3")
print(jd_sent_1_3, "Jaccard Distance between tokens1 and tokens3 with ngram 3")
print(jd_sent_1_4, "Jaccard Distance between tokens1 and tokens4 with ngram 3")
print(jd_sent_1_5, "Jaccard Distance between tokens1 and tokens5 with ngram 3")

# Edit Distance algorithm
import nltk

sent1 = "It might help to re-install Python if possible."
sent2 = "It can help to install Python again if possible."
sent3 = "It can be so helpful to reinstall C++ if possible."
sent4 = "help It possible Python to re-install if might."
# sent 4 has the same words as sent1 with a different order.
sent5 = "I love Python programming."
ed_sent_1_2 = nltk.edit_distance(sent1, sent2)
ed_sent_1_3 = nltk.edit_distance(sent1, sent3)
ed_sent_1_4 = nltk.edit_distance(sent1, sent4)
ed_sent_1_5 = nltk.edit_distance(sent1, sent5)
print(ed_sent_1_2, 'Edit Distance between sent1 and sent2')
print(ed_sent_1_3, 'Edit Distance between sent1 and sent3')
print(ed_sent_1_4, 'Edit Distance between sent1 and sent4')

# Word Correction
import nltk

mistake = "ligting"

words = ['apple', 'bag', 'drawing', 'listing', 'linking', 'living', 'lighting', 'orange', 'walking', 'zoo']

for word in words:
    ed = nltk.edit_distance(mistake, word)
    print(word, ed)

# Wildcard Query using regular expressions
import re

regex = re.compile('th.s')
l = ['this', 'is', 'just', 'a', 'test']
matches = [string for string in l if re.match(regex, string)]
print(matches)
