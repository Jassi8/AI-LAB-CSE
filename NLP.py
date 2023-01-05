import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.The sky is
pinkish-blue. You shouldn't eat cardboard"""

import re
text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
words = text.split()
print(words)

from nltk.corpus import stopwords
print(stopwords.words("english"))
words = [w for w in words if w not in stopwords.words("english")]
print(words)

from nltk.stem.porter import PorterStemmer

# Reduce words to their stems
stemmed = [PorterStemmer().stem(w) for w in words]
print(stemmed)
from nltk.stem.wordnet import WordNetLemmatizer

# Reduce words to their root form
lemmed = [WordNetLemmatizer().lemmatize(w) for w in words]
print(lemmed)

from nltk import pos_tag,RegexpParser

tagged=pos_tag(lemmed)

chunker = RegexpParser("""
NP: {} #To extract Noun Phrases
P: {}#To extract Prepositions
V: {}#To extract Verbs
PP: {} #To extract Prepositional Phrases
VP: {} #To extract Verb Phrases """ )
output = chunker.parse(tagged)
print("After Extracting", output)