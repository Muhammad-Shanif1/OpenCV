import cv2

camera=cv2.VideoCapture(0)
# we take width and height frome the camera
frame_width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec=cv2.VideoWriter_fourcc(*"XVID")     # read below for explaination
fps=20
recorder=cv2.VideoWriter("my_video.mp4",codec,fps,(frame_width,frame_height))
while True:
    success,image=camera.read()
    if not success:
        break
    recorder.write(image)
    # cv2.imshow("Live Recording",image)
    if (cv2.waitKey(1) & 0xFF)==ord('q'):
        break

camera.release()
recorder.release()
cv2.destroyAllWindows()

'''
✅ cv2.VideoWriter_fourcc()

This function takes four characters and converts them into an integer fourcc code (Four Character Code).

This code tells OpenCV which video codec (compression method) to use.

✅ "XVID"

This is the name of the codec you want to use.

"XVID" is a popular open-source codec that saves video in .avi or sometimes .mp4 format.

✅ * (Unpacking)

*"XVID" unpacks the string into individual characters:
'''

'''
What is a Codec?

A codec compresses and decompresses video data. Without it, video files would be huge.

Common codecs:

'XVID' — Good for .avi and .mp4

'MJPG' — Motion JPEG

'X264' — Used for .mp4 (may require extra setup)

'DIVX', 'MP4V', etc.
'''