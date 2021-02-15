# ssh实现与服务器的文件传输

## scp

```
scp path/filename ubuntu(user_name)@114.117.0.252(IP):path     //单文件传输
#绝对路径 /path/filename
#相对路径 path/filename
#path可为空
#将两者顺序交换，则是从服务器上下载文件
#-r指令为整个目录上传下载
#服务器的默认地址是/home/ubuntu/
```

## sftp

```
sftp ubuntu@114.117.0.252   #登录
put path/filename path
get path/filename path
#绝对路径 /path/filename
#相对路径 path/filename
#path可为空
#将两者顺序交换，则是从服务器上下载文件
#-r指令为整个目录上传下载
#服务器的默认地址是/home/ubuntu/
```

