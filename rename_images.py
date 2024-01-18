import os

os.getcwd()

collection = "folder_path_to_images"

img_type = ".jpg" #change if needed

for i, filename in enumerate(os.listdir(collection)):
    os.rename(collection + filename, collection + str(i) + img_type)
