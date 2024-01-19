# Program to detect objects from CAMERA STREAM
# Library : Ultralytics, opencv
# Reference : https://www.freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8/

from ultralytics import YOLO
import cv2

# input path to model/weight (.pt file from Google Colab)
model = YOLO('path_to_model.pt')

cap = cv2.VideoCapture(0)


while True:

    ret, frame = cap.read()

    if not ret:
        break

    # predict stuff in the image
    results = model.predict(frame)

    for result in results:

        for box in result.boxes:

            class_id = result.names[box.cls[0].item()]
            cords = box.xyxy[0].tolist()
            cords = [round(x) for x in cords]
            conf = round(box.conf[0].item(), 2)
            
            cv2.rectangle(frame, 
                          (cords[0], cords[1]), 
                          (cords[2], cords[3]), 
                          (0, 255, 0), 
                          2)
            
            label = f"{class_id}, {conf}"
            cv2.putText(frame, 
                        label, 
                        (cords[0], cords[1] - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, 
                        (0, 255, 0), 
                        2)
        

    cv2.imshow('YOLO Object Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
