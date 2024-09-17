from ultralytics import YOLO 

# model = YOLO('yolov8x')
model = YOLO('models/best.pt')

results = model.predict('input_videos/08fd33_4.mp4',save=True)
# results = model.predict('input_videos/08fd33_4.mp4',save=True, stream=True) 
# inference results will accumulate in RAM unless `stream=True` is passed,
# causing potential out-of-memory errors for large sources or long-running streams and videos.

print(results[0])
print('=====================================')
for box in results[0].boxes:
    print(box)



