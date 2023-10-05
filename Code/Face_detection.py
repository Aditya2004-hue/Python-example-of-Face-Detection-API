import requests
import json
import cv2
import numpy as np
import os

# Load the image
image_path = "path of image"
output_dir = "path to save the output image"
image = cv2.imread(image_path)

# Convert the image to base64 string
_, image_data = cv2.imencode('.jpg', image) 
image_base64 = image_data.tobytes()

# Sending request to server
url = "server url"  
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data = image_data.tobytes())
print(response)
#Save the result
def save_image(image, image_path,output_dir):
    print("Saving output image to dir {}".format(output_dir))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filename = "result_{}".format(image_path.split('/')[-1])
    filepath = os.path.join(output_dir, filename)
    cv2.imwrite(filepath, image)

#displaying image
def display_image(image):
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)


if response.status_code == 200: 
    response_data = response.json()
    print(response.json()) 
    faces = response_data["result"]["faces"]
    print(faces)

    # drawing text and boundary
    for face in faces: 
         
         confidence = face["confidence"]
         box = face["boundingBox"]

         #Extracting bounding box coordinates
         top = int(box["top"])
         left = int(box["left"])
         width = int(box["width"])
         height = int(box["height"])
         cv2.rectangle(image, (left, top), (left + width, top + height), (0, 255, 0), 2)     
        
         face_type = "Face"
         text = f"{face_type} {confidence:.2f}"
         cv2.putText(image, text, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)         
         
         # Draw landmarks
         landmarks = face["landmarks"]
         for landmark in landmarks:
            x = int(landmark["x"])
            y = int(landmark["y"])
            type = (landmark["type"])
            cv2.circle(image, (x, y), 2, (255, 0, 0), -1)
            cv2.putText(image, text,type, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        # display image
            display_image(image)
        # save output
            save_image(image, image_path,output_dir)

         

else:
    print("Error: Request to the API server failed ", response.status_code)
