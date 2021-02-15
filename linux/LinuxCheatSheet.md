## LinuxCheatSheet

### 文件操作

* #### 目录跃迁

```
cd /absolute path
cd relative path
cd /~/~username   进入个人主目录
pwd 	显示工作路径
```

* #### 目录显示

```
ls	查看目录下文件
ls -F	会显示文件类别
ls -l	显示文件的详细资料
ls -a	隐藏文件也将被显示
ls -lh  显示权限
ls *[0-9]* 带有数字的文件，其实是正则表达式
tree	树形显示
```

* #### 创除移搜

隐藏文件夹`.` 表示当前目录
隐藏文件夹`..` 表示上一级目录
```
mkdir path1/dir1 path2/dir2 ...     //创建目录
mkdir -p path			//会按照path创建path中没有的所有目录

rm -f path/filename			//删除文件
dirrm path/dirname
rm -rf path1/dir1 path2/dir2 ...	//删除整个目录

mv paths/names patht/namet

cp paths/filenames patht/filenamet //path_target空缺则是当前目录
cp path/* path		//复制所有文件到path目录下
cp -a path/filename		//当前目录下
cp -a path1 path2		//赋值一个目录
````

* #### 权限

```linux
文件的权限 - 使用 "+" 设置权限，使用 "-" 用于取消 
ls -lh 显示权限 
ls /tmp | pr -T5 -W$COLUMNS 将终端划分成5栏显示 
chmod ugo+rwx directory1 设置目录的所有人(u)、群组(g)以及其他人(o)以读（r ）、写(w)和执行(x)的权限 
chmod go-rwx directory1 删除群组(g)与其他人(o)对目录的读写执行权限 
chown user1 file1 改变一个文件的所有人属性 
chown -R user1 directory1 改变一个目录的所有人属性并同时改变改目录下所有文件的属性 
chgrp group1 file1 改变文件的群组 
chown user1:group1 file1 改变一个文件的所有人和群组属性 
find / -perm -u+s 罗列一个系统中所有使用了SUID控制的文件 
chmod u+s /bin/file1 设置一个二进制文件的 SUID 位 - 运行该文件的用户也被赋予和所有者同样的权限 
chmod u-s /bin/file1 禁用一个二进制文件的 SUID位 
chmod g+s /home/public 设置一个目录的SGID 位 - 类似SUID ，不过这是针对目录的 
chmod g-s /home/public 禁用一个目录的 SGID 位 
chmod o+t /home/public 设置一个文件的 STIKY 位 - 只允许合法所有人删除文件 
chmod o-t /home/public 禁用一个目录的 STIKY 位 
```

