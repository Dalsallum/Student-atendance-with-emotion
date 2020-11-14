# Student-atendance-with-emotion
A Python code that can detect the faces of students and count the number of faces and display their emotion.
One of the strengths of this code that the face detection is accurate even when faces are turned left or right. or looking up or down.
an additional feature with the code that it can display the emotion of each student (not very accurately).

the code can be further improved by keeping track of the number of students and take the average as you go along since it sometimes might miss a face for a few seconds.
and the int(average) at the end of class is the number of students present.
I choose a random number to assume the number of students is 50 , this can be inputted to be any number.



In this code I used the facial_emotion_recognition library which can be tricky to install (on windows).
I provided useful links inside the code, but I will share them here as well.
to download this library, see this video if you are using python 3.8 : https://www.youtube.com/watch?v=xaDJ5xnc8dc
see the library page : https://pypi.org/project/facial-emotion-recognition/
Pip install could work , but the library is not well supported on windows.

I have altered and added many things from library itself so I can count the number of faces. which i mentioned inside the code.
