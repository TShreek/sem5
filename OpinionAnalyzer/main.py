# Topic : Lexical Analysis to detect users opinion
# Done based on IMDB Movie ratings, on movie reviews

# 1) INSTALL DEPENDENCIES (already done):
#    pip install numpy pandas nltk scikit-learn datasets matplotlib seaborn

# 2) IMPORT LIBRARIES
import ssl
import pandas as pd
import nltk
#nltk.download('punkt')
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from anytree import Node, RenderTree


# For feature extraction and modeling
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# For evaluation
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
#For unscrambling sentence and words
from itertools import permutations
from nltk.corpus import words

# STEP A: LOAD THE DATASET (IMDB) WITH HUGGING FACE
print("Loading IMDB dataset from Hugging Face 'datasets' library...")

# run: pip install datasets
from datasets import load_dataset
imdb_dataset = load_dataset("imdb")  # Downloads approx 50k movie reviews

# Convert training and test splits to pandas DataFrames
train_df = pd.DataFrame(imdb_dataset['train'])
test_df = pd.DataFrame(imdb_dataset['test'])

# Check the shape
print("Train set size:", train_df.shape)
print("Test set size:", test_df.shape)
print(train_df.head())

# STEP B: EXPLORATORY DATA ANALYSIS (EDA)
# For a quick label distribution:
print("Label distribution in training data:")
print(train_df['label'].value_counts())
print()

# 0 = negative, 1 = positive for the IMDB data

# 1) Disable SSL certificate verification (use with caution!)
ssl._create_default_https_context = ssl._create_unverified_context

# STEP C: PREPROCESSING TEXT
print("Downloading NLTK resources (stopwords, punkt, wordnet)...")
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
stop_words.remove('not')
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """Convert text to lowercase, remove URLs/punctuation, tokenize, remove stopwords, and lemmatize."""
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

print("Cleaning text in the training and test sets...")
train_df['cleaned_text'] = train_df['text'].apply(clean_text)
test_df['cleaned_text'] = test_df['text'].apply(clean_text)

# STEP D: FEATURE EXTRACTION (TF-IDF)
print("Extracting features using TfidfVectorizer...")
vectorizer = TfidfVectorizer(
    ngram_range=(1,2),   # Use unigrams + bigrams
    max_features=20000   # Limit vocabulary size for efficiency
)

# Fit on train, transform both train and test
X_train = vectorizer.fit_transform(train_df['cleaned_text'])
y_train = train_df['label']  # 0 or 1

X_test = vectorizer.transform(test_df['cleaned_text'])
y_test = test_df['label']

# Optional: check the shape of TF-IDF feature matrices
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

# STEP E: TRAIN-TEST SPLIT 
# (Not needed for IMDB dataset as it comes with predefined train/test splits)
# If your dataset doesn't have a predefined train/test split, use train_test_split here.

# Example:
# X_train_part, X_val, y_train_part, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# STEP F: MODEL TRAINING (LOGISTIC REGRESSION)
print("Training Logistic Regression model...")
model = LogisticRegression(max_iter=250)  # Increase iterations for large data
model.fit(X_train, y_train)

print("Predicting on the test set and evaluating performance...")
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", accuracy)

report = classification_report(y_test, y_pred, target_names=['negative', 'positive'])
print("Classification Report:\n", report)

# STEP H: CONFUSION MATRIX & VISUALIZATION
################################
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])  # 0=neg, 1=pos
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['neg','pos'], yticklabels=['neg','pos'])
plt.title("Confusion Matrix")
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()

print("All done! You now have a trained sentiment classifier on the IMDB dataset.")

# Unscrambling words and sentences
# unscrambling each word in a sentence
def unscramble_word(scrambled):
    """Unscrambles a scrambled word using a dictionary lookup."""
    word_list = set(words.words())  # Use NLTK's English word list
    scrambled_permutations = set([''.join(p) for p in permutations(scrambled)])
    valid_words = scrambled_permutations.intersection(word_list)
    return valid_words if valid_words else {scrambled}  # Return original if no match


#unscrambling the whole sentence
def unscramble_sentence(sentence):
    """Unscrambles each word in a sentence."""
    scrambled_words = sentence.split()
    unscrambled_words = [list(unscramble_word(word))[0] for word in scrambled_words]
    return ' '.join(unscrambled_words)

# implenenting abstract syntax tree

def build_ast_from_tokens(tokens):
    from anytree import Node
    root = Node("Sentence")
    skip_next = False

    for i, token in enumerate(tokens):
        if skip_next:
            skip_next = False
            continue

        if token == "not" and i+1 < len(tokens):
            # Combine 'not' + next token into one node
            Node(f"not_{tokens[i+1]}", parent=root)
            skip_next = True
        else:
            Node(token, parent=root)

    return root



while True:
    user_review = input("\nEnter a review (scrambled or normal, or type 'quit' to exit): ")
    if user_review.lower() == 'quit':
        break

    # Unscramble the input
    unscrambled_review = unscramble_sentence(user_review)
    print(f"Unscrambled Input: {unscrambled_review}")

    # Clean the unscrambled input
    cleaned_input = clean_text(unscrambled_review)

    # Tokenize and build AST
    cleaned_tokens = nltk.word_tokenize(cleaned_input)
    ast_root = build_ast_from_tokens(cleaned_tokens)
    print("\nAbstract Syntax Tree (AST) for your input:")
    for pre, fill, node in RenderTree(ast_root):
        print(f"{pre}{node.name}")

    # Transform and predict
    input_features = vectorizer.transform([cleaned_input])
    prediction = model.predict(input_features)[0]

    if prediction == 1:
        print("Predicted feedback is : POSITIVE")
    else:
        print("Predicted feedback is : NEGATIVE")







## Lexical Analysis	    Tokenizing, removing stopwords, and normalizing text.
## Syntax Analysis	    Feature extraction (TF-IDF) treats phrases (e.g., bigrams like "not good") as structured data.
## Semantic Analysis	Sentiment classification using the trained Logistic Regression model.
## Code Optimization	Limiting features (e.g., 20,000) in TF-IDF for efficiency.
## Code Generation	    Generating predictions (e.g., POSITIVE/NEGATIVE).
