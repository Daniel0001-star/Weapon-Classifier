import os
import shutil

LABEL_DIR = r"Simuletic_Weapon_Umbrella_Dataset\labels"
IMAGE_DIR =r"Simuletic_Weapon_Umbrella_Dataset\images"


#This is empty for now, we have not yet copies and pasted
OUTPUT_DIR = "data"
RIFLE_DIR = os.path.join(OUTPUT_DIR, "rifle")
UMBRELLA_DIR =os.path.join(OUTPUT_DIR, "umbrella")

os.makedirs(RIFLE_DIR, exist_ok=True)
os.makedirs(UMBRELLA_DIR, exist_ok=True)

WEAPON_CLASS_ID = 1
UMBRELLA_CLASS_ID =2 #This may change depedning on the dataset


#We need to know the exact file we are reading thats why we are describing the ppath
for label_file in os.listdir(LABEL_DIR):
    if label_file.endswith(".txt"):
        label_path = os.path.join(LABEL_DIR, label_file) #so this could work with both strings and variables

        with open(label_path, "r") as f: #f is that file opened in a read mode
            lines = f.readlines() #this return a list

    #veryyyyy crazyyy short cut
    class_ID = [int(line.split()[0]) for line in lines] #a short cut for processig loops, because we only need the first of every list

    
    image_name = label_file.replace(".txt", ".jpg")
    image_path = os.path.join(IMAGE_DIR, image_name) #This is to get the image path, quickly another cool trickkkkk

    if WEAPON_CLASS_ID in class_ID:
        shutil.copy(image_path, os.path.join(RIFLE_DIR, image_name))
    
    elif UMBRELLA_CLASS_ID in class_ID:
        shutil.copy(image_path, os.path.join(UMBRELLA_DIR, image_name))

print("Dataset Converted Succesffully")