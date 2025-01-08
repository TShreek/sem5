import ssl
import nltk
nltk.download('all')


# 1) Disable SSL certificate verification (use with caution!)
ssl._create_default_https_context = ssl._create_unverified_context

text = "Hello world! This is a test."
tokens = nltk.word_tokenize(text)
print(tokens)
