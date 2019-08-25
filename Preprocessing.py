import PyPDF2 
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import string

#--------------------------------------------------------------------#
# creating a pdf file object 
pdfFileObj = open('C:/Users/HP/Dropbox/Sem 8/Masters/Coding/Resources/10.1002@bmc.3721.pdf', 'rb') 
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
#  ---------------------------------------------------------------------- 

# printing number of pages in pdf file 
# print(pdfReader.numPages) 

# creating a page object 
# pageObj = pdfReader.getPage(0) 
  
# extracting text from page 
# print(pageObj.extractText()) 
print("---------------------------------------------------------------------")
print("Page contents")

for i in range(pdfReader.numPages):
      page_to_print = pdfReader.getPage(i)
      print(page_to_print.extractText())

num_pages = pdfReader.numPages
count = 0
text = ""
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
print("---------------------------------------------------------------------")

# -------------------------------------------------------------------------------------
# Tokenizations
print("Tokenizations")
tokenization_words = word_tokenize(text)
# keywords = [word for word in word_tokenize(text,'english',True)]
print(tokenization_words)


# -------------------------------------------------------------------------------------
# Removed punctuation
punctuation_words = [word for word in tokenization_words if word.isalpha()]
print(punctuation_words)
print("---------------------------------------------------------------------")

# -------------------------------------------------------------------------------------
print("---------------------------------------------------------------------")
print("Stopwords")
stop_words = set(stopwords.words('english'))
result = [word for word in tokenization_words if not word in stop_words]
print(result)
print("---------------------------------------------------------------------")
# -------------------------------------------------------------------------------------
print("---------------------------------------------------------------------")
print("POS Tag")

tag = nltk.pos_tag(tokenization_words)
print(tag)
# -------------------------------------------------------------------------------------
print("---------------------------------------------------------------------")
print("Stemming")

porter = PorterStemmer()
stemmed = [porter.stem(word) for word in tokenization_words]
print(stemmed)