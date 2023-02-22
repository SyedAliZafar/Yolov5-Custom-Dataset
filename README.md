# Yolov5-Custom-Dataset
* Train Yolo Network

\\code
python train.py --img 640 --batch 16 --epochs 3 --data dataset\custom.yaml --weights weights\yolov5s.pt  
* Run Yolo after traininig your weigths
{

python detect.py --source path\to\images\your_image.jpg --weights runs\train\expX(your_trained_weights)\weights\best.pt --conf 0.5 

}


