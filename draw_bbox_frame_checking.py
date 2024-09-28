import cv2
import numpy as np

# Define the polygon points
polygon_points = np.array([[110, 1035], 
                           [260, 275], 
                           [1055, 253], 
                           [1955, 897]], np.int32)

# Load the video
video_path = 'C:\\Users\\chirag_rana\\Documents\\GitHub\\football-analysis\\input_videos\\08fd33_4.mp4'  # Replace with your video path
cap = cv2.VideoCapture(video_path)

# Check if video is successfully loaded
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object to save the output
output_path = 'C:\\Users\\chirag_rana\\Documents\\GitHub\\football-analysis\\output_videos\\box_check.mp4'  # Output video path
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

while True:
    # Read the next frame from the video
    ret, frame = cap.read()

    if not ret:
        print("End of video or failed to read frame.")
        break

    # Draw the polygon on the current frame
    cv2.polylines(frame, [polygon_points], isClosed=True, color=(255, 0, 0), thickness=1)

    # Write the frame into the output video
    out.write(frame)

# Release video capture and writer objects
cap.release()
out.release()

print(f"Video with polygon saved as {output_path}")
