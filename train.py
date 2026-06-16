import os
import numpy as np
import joblib
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

from preprocess import preprocess_image

DATA_DIR = "data"

X = []
y = []

# rifle = 1
for img in os.listdir(os.path.join(DATA_DIR, "rifle")): #This tells you where to look for, like the path
    path = os.path.join(DATA_DIR, "rifle", img)
    X.append(preprocess_image(path))
    y.append(1) #This is their labels

# umbrella = 0
for img in os.listdir(os.path.join(DATA_DIR, "umbrella")):
    path = os.path.join(DATA_DIR, "umbrella", img)
    X.append(preprocess_image(path))
    y.append(0)

X = np.array(X)
y = np.array(y)

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# train model
model = SGDClassifier(random_state=42)
model.fit(X_train, y_train)

# save model
joblib.dump(model, "model.pkl")

print("Model trained and saved")