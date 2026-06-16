import os
import shutil

LABEL_DIR = r"Simuletic_Weapon_Umbrella_Dataset\labels"
IMAGE_DIR = r"Simuletic_Weapon_Umbrella_Dataset\images"

OUTPUT_DIR = "data"
RIFLE_DIR = os.path.join(OUTPUT_DIR, "rifle")
UMBRELLA_DIR = os.path.join(OUTPUT_DIR, "umbrella")

os.makedirs(RIFLE_DIR, exist_ok=True)
os.makedirs(UMBRELLA_DIR, exist_ok=True)

WEAPON_CLASS_ID = 1
UMBRELLA_CLASS_ID = 2

for label_file in os.listdir(LABEL_DIR):
    if not label_file.endswith(".txt"):
        continue

    label_path = os.path.join(LABEL_DIR, label_file)

    with open(label_path, "r") as f:
        lines = f.readlines()

    class_ids = [int(line.split()[0]) for line in lines]

    image_name = label_file.replace(".txt", ".jpg")
    image_path = os.path.join(IMAGE_DIR, image_name)

    if not os.path.exists(image_path):
        continue

    # weapon → rifle folder
    if WEAPON_CLASS_ID in class_ids:
        shutil.copy(image_path, os.path.join(RIFLE_DIR, image_name))

    # umbrella → umbrella folder
    elif UMBRELLA_CLASS_ID in class_ids:
        shutil.copy(image_path, os.path.join(UMBRELLA_DIR, image_name))

print("Dataset converted successfully.")