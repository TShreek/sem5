################################################################################
# sentiment_analysis.py
################################################################################

# 1) INSTALL DEPENDENCIES (already done, but here is the reminder):
#    pip install numpy pandas nltk scikit-learn datasets matplotlib seaborn

# 2) IMPORT LIBRARIES
import ssl
import pandas as pd
import nltk
nltk.download('punkt')
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# For feature extraction and modeling
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# For evaluation
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

################################################################################
# STEP A: LOAD THE DATASET (IMDB) WITH HUGGING FACE
################################################################################
print("Loading IMDB dataset from Hugging Face 'datasets' library...")

# If not installed, run: pip install datasets
from datasets import load_dataset
imdb_dataset = load_dataset("imdb")  # Downloads ~50k reviews

# Convert training and test splits to pandas DataFrames
train_df = pd.DataFrame(imdb_dataset['train'])
test_df = pd.DataFrame(imdb_dataset['test'])

# Check the shape
print("Train set size:", train_df.shape)
print("Test set size:", test_df.shape)
print(train_df.head())

################################################################################
# STEP B: EXPLORATORY DATA ANALYSIS (EDA) [Optional but Recommended]
################################################################################
# For a quick label distribution:
print("Label distribution in training data:")
print(train_df['label'].value_counts())
print()

# Typically, 0 = negative, 1 = positive for IMDB


# 1) Disable SSL certificate verification (use with caution!)
ssl._create_default_https_context = ssl._create_unverified_context
################################################################################



# STEP C: PREPROCESSING TEXT
################################################################################
print("Downloading NLTK resources (stopwords, punkt, wordnet)...")
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """Convert text to lowercase, remove URLs/punctuation, tokenize, remove stopwords, and lemmatize."""
    # Lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    # Remove non-alphabetic characters
    text = re.sub(r'[^a-z\s]', '', text)
    # Tokenize
    tokens = nltk.word_tokenize(text)
    # Remove stopwords + lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    # Rejoin to form the cleaned sentence
    return ' '.join(tokens)

print("Cleaning text in the training and test sets...")
train_df['cleaned_text'] = train_df['text'].apply(clean_text)
test_df['cleaned_text'] = test_df['text'].apply(clean_text)

################################################################################
# STEP D: FEATURE EXTRACTION (TF-IDF)
################################################################################
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

################################################################################
# STEP E: TRAIN-TEST SPLIT (OPTIONAL)
################################################################################
# If your dataset doesn't have a predefined train/test split, use train_test_split here.
# But IMDB from 'datasets' library already has separate train/test.

# Example if needed:
# X_train_part, X_val, y_train_part, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

################################################################################
# STEP F: MODEL TRAINING (LOGISTIC REGRESSION)
################################################################################
print("Training Logistic Regression model...")
model = LogisticRegression(max_iter=200)  # Increase iterations for large data
model.fit(X_train, y_train)

################################################################################
# STEP G: MODEL EVALUATION
################################################################################
print("Predicting on the test set and evaluating performance...")
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", accuracy)

# Classification Report (Precision, Recall, F1-score)
report = classification_report(y_test, y_pred, target_names=['negative', 'positive'])
print("Classification Report:\n", report)

################################################################################
# STEP H: CONFUSION MATRIX & VISUALIZATION
################################################################################
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])  # 0=neg, 1=pos
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['neg','pos'], yticklabels=['neg','pos'])
plt.title("Confusion Matrix")
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()

print("All done! You now have a trained sentiment classifier on the IMDB dataset.")
################################################################################
