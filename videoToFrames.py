# Importing all necessary libraries
import cv2
import os

# Set path to folder containing MP4 files
video_folder_path = "C:/Users/manav/Desktop/New folder"

# Loop over all MP4 files in folder
for video_file_name in os.listdir(video_folder_path):
    print(video_file_name)
    if video_file_name.endswith('.mp4'):
        # Read the video from file
        video_file_path = os.path.join(video_folder_path, video_file_name)
        cam = cv2.VideoCapture(video_file_path)

        # Create subdirectory for saving frames
        video_file_basename = os.path.splitext(video_file_name)[0]
        frames_folder_path = os.path.join(video_folder_path, video_file_basename)
        if not os.path.exists(frames_folder_path):
            os.makedirs(frames_folder_path)

        # Extract frames from video
        currentframe = 0
        fps = cam.get(cv2.CAP_PROP_FPS)
        frame_interval = int(round(fps / 10))
        while True:
            # Reading from frame
            ret, frame = cam.read()
            if ret:
                # Save frame every 10 frames
                if currentframe % frame_interval == 0:
                    frame_file_name = 'frame' + str(currentframe) + '.jpg'
                    frame_file_path = os.path.join(frames_folder_path, frame_file_name)
                    print('Extracting frame: ' + frame_file_path)
                    cv2.imwrite(frame_file_path, frame)
                currentframe += 1
            else:
                break

        # Release all space and windows once done
        cam.release()
        cv2.destroyAllWindows()