# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:38:32 2019

@author: Shriram
"""

#import nltk
#from nltk.tokenize import word_tokenize
import pandas as pd
#nltk.download('punkt')
#ltk.download('averaged_perceptron_tagger')


##################################################################3
text = "The CalCOFI data set represents the longest (1949-present) and most complete (more than 50,000 sampling stations) time series of oceanographic and larval fish data in the world. It includes abundance data on the larvae of over 250 species of fish; larval length frequency data and egg abundance data on key commercial species; and oceanographic and plankton data. The physical, chemical, and biological data collected at regular time and space intervals quickly became valuable for documenting climatic cycles in the California Current and a range of biological responses to them. CalCOFI research drew world attention to the biological response to the dramatic Pacific-warming event in 1957-58 and introduced the term “El Niño” into the scientific literature.The California Cooperative Oceanic Fisheries Investigations (CalCOFI) are a unique partnership of the California Department of Fish & Wildlife, NOAA Fisheries Service and Scripps Institution of Oceanography. The organization was formed in 1949 to study the ecological aspects of the sardine population collapse off California. Today our focus has shifted to the study of the marine environment off the coast of California, the management of its living resources, and monitoring the indicators of El Nino and climate change. CalCOFI conducts quarterly cruises off southern & central California, collecting a suite of hydrographic and biological data on station and underway. Data collected at depths down to 500 m include: temperature, salinity, oxygen, phosphate, silicate, nitrate and nitrite, chlorophyll, transmissometer, PAR, C14 primary productivity, phytoplankton biodiversity, zooplankton biomass, and zooplankton biodiversity."
BAD_CHARS = ".!?,\'\""

# transform text into a list words--removing punctuation and filtering small words
words = [ word.strip(BAD_CHARS) for word in text.strip().split() if len(word) > 4 ]

word_freq = {}

# generate a 'word histogram' for the text--ie, a list of the frequencies of each word
for word in words :
  word_freq[word] = word_freq.get(word, 0) + 1
  
type(word_freq)


# sort the word list by frequency 
# (just a DSU sort, there's a python built-in for this, but i can't remember it)
tx = [ (v, k) for (k, v) in word_freq.items()]
tx.sort(reverse=True)
word_freq_sorted = [ (k, v) for (v, k) in tx ]

# eg, what are the most common words in that text?
print(word_freq_sorted)
type(word_freq_sorted)
df = pd.DataFrame(word_freq_sorted)
# returns: [('which', 4), ('other', 4), ('like', 4), ('what', 3), ('upon', 3)]
# obviously using a text larger than 50 or so words will give you more meaningful results

#term_importance = lambda word : 1.0/word_freq[word]

# select document keywords from the words at/near the top of this list:
#l = map(term_importance, str(word_freq.keys()))

df.columns = ['tag', 'tag_frequency']
df = df[~df.tag.str.contains(r'\d')]
df.to_csv('tags.csv',index=False)