#coding:utf-8
from ultralytics import YOLO

# 加载预训练模型
model = YOLO("yolov8n.pt")
# Use the model
if __name__ == '__main__':
    # Use the model
    # datasets/PotatoData/data.yaml
    # datasets/TomatoData/data.yaml
    results = model.train(data='datasets/PotatoData/data.yaml', epochs=250, batch=1)  # 训练模型
    # 将模型转为onnx格式
    # success = model.export(format='onnx')



