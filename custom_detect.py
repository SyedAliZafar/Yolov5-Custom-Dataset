import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Images
dir = 'https://github.com/ultralytics/yolov5/raw/master/data/images/'
imgs = [dir + f for f in ('zidane.jpg', 'bus.jpg')]  # batched list of images

# Inference
results = model(imgs)

# Results
results.print()  
results.save()  # or .show()

# Data
print(results.xyxy[0])  # print img1 predictions (pixels)