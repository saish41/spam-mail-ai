import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


DATASET_PATH = "dataset/spam_emails.csv"

MODEL_PATH = "model/spam_model.pkl"


print("\n========================================")
print("        SPAM AI TRAINING")
print("========================================")


# Load dataset

df = pd.read_csv(
    DATASET_PATH
)


print("\nDataset loaded")

print(
    "Total emails:",
    len(df)
)


# Remove missing values

df = df.dropna(
    subset=["email", "label"]
)


# Normalize labels

df["label"] = (
    df["label"]
    .astype(str)
    .str.lower()
    .str.strip()
)


# Features

X = df["email"]

y = df["label"]


print("\nClass distribution:")

print(
    y.value_counts()
)


# Split dataset

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y
)


print("\nTraining:", len(X_train))

print("Testing :", len(X_test))


# TF-IDF + Logistic Regression

pipeline = Pipeline([

    (
        "tfidf",

        TfidfVectorizer(

            lowercase=True,

            stop_words="english",

            ngram_range=(1, 2),

            min_df=2,

            max_df=0.98,

            sublinear_tf=True,

            max_features=50000
        )
    ),

    (
        "classifier",

        LogisticRegression(

            max_iter=2000,

            C=2.0,

            class_weight="balanced"
        )
    )
])


# Train

print("\nTraining model...")

pipeline.fit(
    X_train,
    y_train
)


print("Training complete!")


# Evaluate

predictions = pipeline.predict(
    X_test
)


accuracy = accuracy_score(
    y_test,
    predictions
)


print("\n========================================")
print("           MODEL RESULTS")
print("========================================")


print(
    f"\nAccuracy: {accuracy * 100:.2f}%"
)


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        predictions
    )
)


print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        predictions
    )
)


# Save

os.makedirs(
    "model",
    exist_ok=True
)


joblib.dump(
    pipeline,
    MODEL_PATH
)


print("\n========================================")
print("MODEL SAVED SUCCESSFULLY")
print("========================================")

print(
    MODEL_PATH
)