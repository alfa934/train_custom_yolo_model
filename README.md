# train_custom_yolo_model
A very detailed explanation on how to train your own YOLO v8 model

> **📌 Note: This tutorial uses YOLO v8, thus may subject to change for future versions**

<br>

## 1. Prepare Dataset and Files
### A. Take photos (as much as possible) with variety in position and lighting

### B. Rename photos for easy organisation

### C. Label photos using Roboflow, Make Sense AI, etc...

### D. Organise images and label into **<custom_data_folder>**
- Make an image folder and separate the images into train and val folder.

- Make a label folder and separate the **_.txt_** files into train and val folder

### E. Prepare YAML file and place into **<custom_data_folder>**
- Make a YAML file by using **[yaml_file_template.yaml](https://github.com/alfa934/train_custom_yolo_model/blob/main/yaml_file_template.yaml)**

- Follow the instructions in the YAML file template

---
```
Your <custom_data_folder> structure should look like this:

<custom_data_folder> 
|
|-- <image_folder>
|   |-- <train_folder>
|   |-- <val_folder>
|
|-- <label_folder>
|   |-- <train_folder>
|   |-- <val_folder>
|
|--<yaml_file_template>
|
|---------------------
```

![custom_data_folder.png](https://github.com/alfa934/train_custom_yolo_model/blob/main/resource/custom_data_folder.png)

---
<br>

## 2. Google Colab Preparation
Follow instructions from **[Train_custom_yolo_model.ipynb](https://github.com/alfa934/train_custom_yolo_model/blob/main/Train_custom_yolo_model.ipynb)**

<br>

## 3. Train YOLO v8 model with up-to-date Ultralytics API in Google Colab
Change the model and epoch parameters for better result.

![train_model.png](https://github.com/alfa934/train_custom_yolo_model/blob/main/resource/train_model.png)

<br>

## 4. Deploy custom model to OpenCV (camera feed, image, video, etc...)
Results are usually saved to **_runs/detect/train_** <br>


Find in directory, the more you train, the more train files there will be (choose the latest one, for example **_train2_**).


> Choose **_best.pt_**, or other **_.pt_** file

Download the **_.pt_** file and save it LOCALLY on your laptop/pc.

![deploy_model.png](https://github.com/alfa934/train_custom_yolo_model/blob/main/resource/deploy_model.png)

Then use it with **[opencv_detect.py](https://github.com/alfa934/train_custom_yolo_model/blob/main/opencv_detect.py)**

<br>

## REFERENCES
1. https://www.youtube.com/watch?v=GRtgLlwxpc4
2. https://www.youtube.com/watch?v=FBavXyN18K8
3. https://www.youtube.com/watch?v=2TIhdai0f6M
4. https://www.youtube.com/watch?v=tFNJGim3FXw
5. https://www.youtube.com/watch?v=wM1wn1bZ3S4
