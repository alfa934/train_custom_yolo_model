# train_custom_yolo_model
A very detailed explanation on how to train your own YOLO v8 model

> **📌 Note: This tutorial uses YOLO v8, thus may subject to change for future versions**

<br>

## 1. Prepare Dataset and Files
#### A. Take photos (as much as possible) with variety in position and lighting
#### B. Rename photos for easy organisation
#### C. Label photos using Roboflow, Make Sense AI, etc...
#### D. Organise images and label into ONE folder
#### E. Prepare YAML file and place in folder

<br>

## 2. Google Colab Preparation
Follow instructions from **[Train_custom_yolo_model.ipynb](https://github.com/alfa934/train_custom_yolo_model/blob/main/Train_custom_yolo_model.ipynb)**


<br>

## 3. Train YOLO v8 model with up-to-date Ultralytics API in Google Colab
Change the model and epoch parameters for better result.

<br>

## 4. Deploy custom model to OpenCV (camera feed, image, video, etc...)
Results are usually saved to **_runs/detect/train_** <br>

Find in directory, the more you train, the more train files there will be (choose the latest one, for example **_train2_**).

> Choose **_best.pt_**, or other **_.pt_** file

Download the **_.pt_** file and save it LOCALLY on your laptop/pc.

<br>

## REFERENCES
1. https://www.youtube.com/watch?v=GRtgLlwxpc4
2. https://www.youtube.com/watch?v=FBavXyN18K8
3. https://www.youtube.com/watch?v=2TIhdai0f6M
4. https://www.youtube.com/watch?v=tFNJGim3FXw
5. https://www.youtube.com/watch?v=wM1wn1bZ3S4
