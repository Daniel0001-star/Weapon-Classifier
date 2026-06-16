import os #for file handing
import numpy as np #machines loves array, still look into this
import cv2 #computer vision
import joblib #for saving your model
import matplotlib.pyplot as plt

from sklearn.metrics import (
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    roc_curve,
    auc
)

from sklearn.model_selection import train_test_split

DATA_DIR = "data"
IMG_SIZE = 64

# --- same preprocessing as training ---
def preprocess(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    return img.flatten()

# --- load dataset again ---
X = []
y = []

for img in os.listdir(os.path.join(DATA_DIR, "rifle")): #The labelin was done here
    X.append(preprocess(os.path.join(DATA_DIR, "rifle", img)))
    y.append(1)

for img in os.listdir(os.path.join(DATA_DIR, "umbrella")):
    X.append(preprocess(os.path.join(DATA_DIR, "umbrella", img)))
    y.append(0)

X = np.array(X)
y = np.array(y)

# split same way
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- load model ---
model = joblib.load("model.pkl")


y_pred = model.predict(X_test)

#We actually testing it out, I mean getting the confusion matrix, precisin, so i can tweak some hyperparameters
print("\nCONFUSION MATRIX") #This is where false positive an dtrue positive coems into play
print(confusion_matrix(y_test, y_pred))

print("\nPRECISION:", precision_score(y_test, y_pred))
print("RECALL:", recall_score(y_test, y_pred))
print("F1 SCORE:", f1_score(y_test, y_pred)) #We want a high f1 score!!
#f1 score is like a balanced score between precision and recall


y_scores = model.decision_function(X_test)


fpr, tpr, thresholds = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)
print("Thresholds:", thresholds)

plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0, 1], [0, 1], "--")  # random baseline
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()

