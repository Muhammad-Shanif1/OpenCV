import cv2
import time

# Open webcam
camera = cv2.VideoCapture(0)

# Get frame size
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Setup video writer
codec = cv2.VideoWriter_fourcc(*"XVID")
fps = 20
recorder = cv2.VideoWriter("my_video_with_timer.mp4", codec, fps, (frame_width, frame_height))

# Start timer
start_time = time.time()

while True:
    success, image = camera.read()
    if not success:
        break

    # Get elapsed time
    elapsed_time = int(time.time() - start_time)
    timer_text = f"Recording: {elapsed_time}s"

    # Add timer text
    cv2.putText(image, timer_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2, cv2.LINE_AA)

    # Add watermark (e.g., bottom-right corner)
    watermark_text = "© YourName"
    text_size = cv2.getTextSize(watermark_text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
    x = frame_width - text_size[0] - 10
    y = frame_height - 10
    cv2.putText(image, watermark_text, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 255, 255), 2, cv2.LINE_AA)

    # Write and show frame
    recorder.write(image)
    cv2.imshow("Live Recording with Timer & Watermark", image)

    # Press 'q' to quit
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

# Cleanup
camera.release()
recorder.release()
cv2.destroyAllWindows()
