import cv2

# 打开摄像头
cap = cv2.VideoCapture(1)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 定义视频编码器和输出视频的名称
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用mp4v编码器
out = cv2.VideoWriter('potato_2.mp4', fourcc, 20.0, (640, 480))

while True:
    # 读取一帧
    ret, frame = cap.read()

    # 如果正确读取帧，ret为True
    if not ret:
        print("无法读取帧")
        break

    # 显示帧
    cv2.imshow('frame', frame)

    # 将帧写入视频文件
    out.write(frame)

    # 按 'q' 键退出循环
    if cv2.waitKey(1) == ord('q'):
        break

# 释放摄像头和视频写入对象
cap.release()
out.release()

# 关闭所有OpenCV窗口
cv2.destroyAllWindows()