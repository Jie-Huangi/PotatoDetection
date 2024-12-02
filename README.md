# PotatoDetection
 bud eye detection

软件开发环境:python3.9
系统界面开发：pyqt5

项目文件说明
见目录中的【目录文件说明.png】图片。

环境配置步骤【共两步】：
【注意：软件存放路径最好不要有中文。】

## 【第一步：安装python3.9】
方法一【推荐】：
先安装ananconda软件，官网地址：https://www.anaconda.com/download
安装完成后，在conda命令窗口，使用命令"conda create -n py39 python=3.9"创建3.9的虚拟环境
然后激活虚拟环境“conda activate py39”,然后再进行第二步依赖库的安装。
方法二：
直接在python官网下载pyhon3.9的exe文件，安装即可。

## 【第二步：安装软件所需的依赖库】
（注意：输入命令前，命令行需先进入项目目录的路径下，不然会提示找不到文件）
方法一：【推荐】
直接运行installPackages.py一键安装第三方库的脚本。命令为：python installPackages.py
方法二: 运行下方命令
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

## 【第三步：运行程序】
按照以上两步环境配置完成后，直接运行MainProgram.py文件即可打开程序。
命令为：python MainProgram.py


## 【第四步：模型训练】
将文件【datasets/PotatoData/data.yaml】中train,val数据集的绝对路径改为自己项目数据集的绝对路径
train: E:\PotatoDetection\datasets\PotatoData\train
val: E:\PotatoDetection\datasets\PotatoData\val
命令为：python train.py

然后运行train.py文件即可开始进行模型训练,训练结果会默认保存在runs/detect目录中。
其中runs/train是我已经训练好的结果文件，含模型与所有过程内容。
训练好的模型在runs/train/weights目录下，last.pt表示最后一轮结果的训练模型，best.pt表示训练中最好结果的训练模型。一般我们使用best.pt就行。

