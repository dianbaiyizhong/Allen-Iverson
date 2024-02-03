# conda
### 创建环境
```shell
conda create -n  ai_test python=3.7
```

### 查看环境
```shell
conda env list
```

### 激活环境
```shel
conda activate ai_test
```

### 退出环境

```sh
deactivate
```









# pip

```sh
pip install fastapi -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

pip install paddleocr -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

pip install uvicorn -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

```



# python

### 执行python脚本

```python
python paddle-ocr-web.py
```

### 后台运行脚本

```sh
nohup python paddle-ocr-web.py &
# 查看后台进程
ps aux |grep python
# 杀
kill -9 pid
```







# cuda

### cuda下载

[CUDA Toolkit Archive | NVIDIA Developer](https://developer.nvidia.com/cuda-toolkit-archive)



### paddle地址

[开始使用_飞桨-源于产业实践的开源深度学习平台 (paddlepaddle.org.cn)](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/docker/linux-docker.html)





# docker

### 端口映射启动

```sh
nvidia-docker run -p 8000:8000 --name paddle -it -v /mnt:/mnt -v $PWD:/paddle registry.baidubce.com/paddlepaddle/paddle:2.6.0-gpu-cuda12.0-cudnn8.9-trt8.6 /bin/bash


nvidia-docker run --runtime=nvidia2 -p 8000:8000 --name paddle -it -v /mnt:/mnt -v $PWD:/paddle registry.baidubce.com/paddlepaddle/paddle:2.6.0-gpu-cuda11.2-cudnn8.2-trt8.0 /bin/bash
```
### 进入容器
```sh
docker exec -it paddle /bin/bash
```





# 更新apt 源
curl https://get.docker.com | sh 



distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list



sudo apt update
sudo apt-get install nvidia-docker2
service docker start

