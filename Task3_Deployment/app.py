from fastapi import FastAPI
from pydantic import BaseModel

import tensorflow as tf
import pandas as pd
import numpy as np
import re

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

app = FastAPI()

# --------------------
# Paths
# --------------------

DATASET_PATH = "../datasets/resume_dataset.csv"

MODEL_PATH = "../Task2_DeepLearning/resume_classifier.keras"

# --------------------
# Load dataset
# --------------------

df = pd.read_csv(DATASET_PATH)

# --------------------
# Clean text
# --------------------

def clean_text(text):

    text = str(text)

    text = re.sub(r"http\\S+|www\\S+", "", text)

    text = re.sub(r"&\\w+;", " ", text)

    text = re.sub(r"[^a-zA-Z ]", " ", text)

    text = text.lower()

    text = re.sub(r"\\s+", " ", text)

    return text.strip()

df["clean_resume"] = df["Resume"].apply(clean_text)

# --------------------
# Label encoder
# --------------------

encoder = LabelEncoder()

encoder.fit(df["Category"])

# --------------------
# Tokenizer
# --------------------

vocab_size = 5000

max_length = 400

tokenizer = Tokenizer(

    num_words=vocab_size,

    oov_token="<OOV>"
)

tokenizer.fit_on_texts(

    df["clean_resume"]
)

# --------------------
# Load trained model
# --------------------

model = tf.keras.models.load_model(

    MODEL_PATH
)

# --------------------
# Input schema
# --------------------

class ResumeInput(BaseModel):

    resume: str

# --------------------
# Home route
# --------------------

@app.get("/")

def home():

    return {

        "message": "Resume Classification API"
    }

# --------------------
# Prediction route
# --------------------

@app.post("/predict")

def predict(data: ResumeInput):

    text = clean_text(

        data.resume
    )

    sequence = tokenizer.texts_to_sequences(

        [text]
    )

    padded = pad_sequences(

        sequence,

        maxlen=max_length,

        padding="post",

        truncating="post"
    )

    prediction = model.predict(

        padded,

        verbose=0
    )

    class_index = np.argmax(

        prediction
    )

    confidence = float(

        np.max(prediction)
    )

    category = encoder.classes_[

        class_index
    ]

    return {

        "category": category,

        "confidence": f"{confidence*100:.2f}%"
    }