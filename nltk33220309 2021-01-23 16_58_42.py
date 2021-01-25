import nltk
#get tokenizer models 
nltk.download('punkt')
#initiate paragraph example, save it in variablename:text
text = "today is a very sunny day. this is the time for me to do some exercises and learnings. No checking 33220309@yahoo.com or aripratiwi@test.itb for today!"
print(text)
#get function sentence splitter 
from nltk.tokenize import sent_tokenize
tokenized_text = sent_tokenize (text)
print('sentences in the paragraph')
print(tokenized_text)

#get function word splitter / tokenize
from nltk.tokenize import word_tokenize
tokenized_word = word_tokenize (text)
print ('words in the parapgraph')
print(tokenized_word)

#get function stemming and lemmatizer
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
word_lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer
word_stemP = PorterStemmer()

from nltk.stem.lancaster import LancasterStemmer
word_stemL = LancasterStemmer()

punctuations = "?:;!?,."
for word in tokenized_word:
	if word in punctuations:
		tokenized_word.remove(word)
		
		
tokenized_word
print("{0:20}{1:20}{2:20}{3:20}".format("word","lemma","porterStem","lancasStem"))
for word in tokenized_word:
	print("{0:20}{1:20}{2:20}{3:20}".format(word,word_lem.lemmatize(word), word_stemP.stem(word), word_stemL.stem(word)))
	
	
#get functions POS tagger
nltk.download('averaged_perceptron_tagger')
print('P O S tagger')
nltk.pos_tag(tokenized_word)


#defined the pattern
pattern = 'Noun Phrase : {<DT>?<JJ>*<NN>}'

#applied the pattern
cp = nltk.RegexpParser(pattern)

#identifying the pattern based on POS tagging in the given text, if any (Phare chunker)
cs = cp.parse(nltk.pos_tag(tokenized_word))

print (cs)


#get regular expression function
import re
#defined email pattern
email = re.compile ('\w+@\w+\.[a-z]{3}')

email.findall(text)

#masking any content in text where the patteren defined are matched
text_mask = email.sub('_email_',text)

print('masking text : ',text_mask)

	



	
