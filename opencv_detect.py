# Program to detect objects from CAMERA STREAM
# Library : Ultralytics, opencv
# Reference : https://www.freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8/

from ultralytics import YOLO
import cv2

# input path to model/weight
model = YOLO('path_to_model.pt')

# camera config, resolution, etc
cap = cv2.VideoCapture(0)
# # this is default resolution,
# # may not change for your camera
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while True:

    ret, frame = cap.read()
    # flip horizontally
    frame = cv2.flip(frame, 1)

    if not ret:
        print("Unable to open media!")
        break


    # predict stuff in the image
    results = model.predict(frame)


    for result in results:

        for box in result.boxes:

            class_id = result.names[box.cls[0].item()]
            cords = box.xyxy[0].tolist()
            cords = [round(x) for x in cords]
            conf = round(box.conf[0].item(), 2)

            # The coordinate of bounding boxes            
            # x_min, y_min => cords[0], cords[1]
            # x_max, y_max => cords[2], cords[3]


            # centroid of object
            cx = int((cords[0]+cords[2])/2.0)
            cy = int((cords[1]+cords[3])/2.0)

            cv2.circle(frame, 
                       (cx,cy), 
                       2,
                       (0, 0, 255),  
                       cv2.FILLED)
            
            # bounding box of object
            cv2.rectangle(frame, 
                          (cords[0], cords[1]), 
                          (cords[2], cords[3]), 
                          (0, 255, 0), 
                          2)
            
            # display info (class, confidence, centroid)
            label = f"{class_id}, {conf}, ({cx},{cy})"
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
