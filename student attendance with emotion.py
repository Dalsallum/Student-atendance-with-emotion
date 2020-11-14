from facial_emotion_recognition import EmotionRecognition
'''
to download this library see this video if you are using python 3.8 : https://www.youtube.com/watch?v=xaDJ5xnc8dc
see the library page : https://pypi.org/project/facial-emotion-recognition/
pip install might work.

'''

from facenet_pytorch import MTCNN
import torch

'''
these two libraries are supposed to be used inside the library only, but it's imported here since it help with faces counter
'''

import numpy as np
import cv2 as cv


er = EmotionRecognition(device='gpu', gpu_id=0) 
gpu_id=0 # this is used for faces counting
device = torch.device(f'cuda:{str(gpu_id)}') # to use gpu if your device supports it, if not comment this line and change device below to 'cpu'
cam = cv.VideoCapture(r'C:\Users\komsi\Desktop\Misk - GeStream\AI project - face detection\Data for emotion\Studenlecture04.mov') # video to be tested, in case of using Web cam the argument will be 0
mtcnn = MTCNN(keep_all=True, device=device) # for face counting also, if your device not gpu supported make device = 'cpu' and comment line number 22
font = cv.FONT_HERSHEY_SIMPLEX # font for the stuednts attendance
total_students = 50 # default value that will be inputted by the user later


while True:
    

    success, frame = cam.read() # read frame by frame
    faces,_ = mtcnn.detect(frame) ## faces will be returned as numpy array, the number of elements is the number of faces, if there are no faces it will return none
    if type(faces) == np.ndarray: ## if a face or more was detected
        cv.putText(frame, 'present students = {number}'.format(number = len(faces)) , (10, 50), font, 1, (0, 255, 255), 1, cv.LINE_4)
        cv.putText(frame, 'absent students = {number}'.format(number = total_students - len(faces)) , (10, 30), font, 1, (0, 255, 255), 1, cv.LINE_4)
    
    

    frame = er.recognise_emotion(frame, return_type='BGR') # it will recognise the emotion and label them
    

    cv.imshow('frame',frame)
    key = cv.waitKey(1) 
    if key == 27: # Press ESC to exit the frame
        break
