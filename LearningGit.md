# LearningGit

## 学习存档

11/19https://www.liaoxuefeng.com/wiki/896043488029600/896954074659008

11/20https://www.liaoxuefeng.com/wiki/896043488029600/900002180232448

## 安装

#### 设置

```git
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```

`git config`命令的`--global`参数：表示你这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。

## 版本库 repository

#### 创建

选择合适的地方，创建空目录

###### \#\# 表示文件名

##### 初始化

```
$ git init
```

##### add

``` 
$ git add ##
```

##### commit

``` 
$ git commit -m "***"
```

`git commit`命令执行成功后会告诉你，`1 file changed`：1个文件被改动（我们新添加的readme.txt文件）；`2 insertions`：插入了两行内容（readme.txt有两行内容）。

##### status

``` git
$ git status
```

我在learngit文件夹下创建了一个learn.txt修改了内容后，进行`$ git status`操作

```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   learn.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        sub_1/

no changes added to commit (use "git add" and/or "git commit -a")

```

##### diff

```
$ git diff ##
```

关于git diff

https://www.cnblogs.com/qianqiannian/p/6010219.html

##### log

```
$ git log
$ git log --pretty=oneline
```

由近及远输出提交日志，添加`--pretty=oneline`参数使输出信息更为简洁

主要信息包括： SHA1获得的哈希值，HEAD所在位置，commit及可被忽略的信息author date

##### reset

```
$ git reset --hard HEAD^
$ git reset --hard HEAD~100
```

HEAD指针回退

```
$ git reset --hard ***
```

***表示commit id （哈希值），通过这个commit id 进行回退

##### reflog

```
$ git reflog
```

显示reset的日志

#### 删除

##### 	未add

##### restore

```
$ git restore ##
```

##### 		checkout

```git
$ git checkout -- ##
```

回到上一次add或commit后的版本

##### 	去stage化

##### 		restore

```
$ git restore --staged ##
```

##### 		reset

```
$ git reset HEAD ##
```

##### 	未push

​		head的回退

## GitHub

在GitHub上创建仓库后

```
$ git remote add origin git@github.com:LibroWu/MatrixOOP.git
```

重定向

```
$ git remote set-url origin git@github.com: ##
```

第一次提交

```
$ git push -u origin master
```

提交

```
$ git push origin master
```

#### pull

```
$ git pull git@github.com:Finnyear/ICPC-Management-System master
```



## 文件管理

##### 创建文件夹

```
$ mkdir learngit
```

在当前目录下创建名为learngit的文件夹

##### 进入文件夹

```
$ cd learngit
```

进入子文件夹learngit

##### 显示地址

```
$ pwd
```

显示当前所在的文件夹地址

##### 显示文件夹内容 

```
$ ls
$ ls -ah
$ ls ##
```

显示当前文件夹下内容（-ah 命令显示隐藏内容）

中间可加相对路径，如 sub/sub_sub

```
ls==dir?
```

##### cat显示内容

```
$ cat ###
```

##### rm remove

```
$ rm ##
```

```
$ git rm ##
```

