# LearningGit

## 学习存档

11/19https://www.liaoxuefeng.com/wiki/896043488029600/896954074659008

11/20https://www.liaoxuefeng.com/wiki/896043488029600/900002180232448

01/14 finish

## 安装

#### 设置

```git
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```

`git config`命令的`--global`参数：表示你这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。

#### SSH

第1步：创建SSH Key。在用户主目录下，看看有没有.ssh目录，如果有，再看看这个目录下有没有`id_rsa`和`id_rsa.pub`这两个文件，如果已经有了，可直接跳到下一步。如果没有，打开Shell（Windows下打开Git Bash），创建SSH Key：

```
$ ssh-keygen -t rsa -C "youremail@example.com"
```

你需要把邮件地址换成你自己的邮件地址，然后一路回车，使用默认值即可，由于这个Key也不是用于军事目的，所以也无需设置密码。

如果一切顺利的话，可以在用户主目录里找到`.ssh`目录，里面有`id_rsa`和`id_rsa.pub`两个文件，这两个就是SSH Key的秘钥对，`id_rsa`是私钥，不能泄露出去，`id_rsa.pub`是公钥，可以放心地告诉任何人。

第2步：登陆GitHub，打开“Account settings”，“SSH Keys”页面：

然后，点“Add SSH Key”，填上任意Title，在Key文本框里粘贴`id_rsa.pub`文件的内容：

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
$ git log --graph --pretty=oneline --abbrev-commit
```

由近及远输出提交日志，添加`--pretty=oneline`参数使输出信息更为简洁

主要信息包括： SHA1获得的哈希值，HEAD所在位置，commit及可被忽略的信息author date

`--graph`显示分支的合并情况

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

##### 查看远程库信息

```
$ git remote
$ git remote -v  //详细信息
```

##### 删除远程库

```
git remote rm origin
```

## 多分支

##### 创建分支

```
$ git branch ##
```

##### 分支切换

```
$ git checkout ##
```

##### 上述两个操作合并

```
$ git checkout -b ##
$ git checkout -b dev origin/dev  //创建新分支，与远程库中的分支相关联
```

##### 显示当前分支

```
$ git branch
```

##### 设置远程关联分支

```
$ git branch --set-upstream-to=origin/dev dev
```

##### 分支合并

```
$ git merge ##
$ git merge --no-ff -m "" ##   //禁用Fast forward，保留分支历史
```

##### 删除分支

```
$ git branch -d ##
$ git branch -D <name>  //强行删除未合并的分支
```

#### swich

##### 切换到新分支

```
$ git switch -c ##
```

##### 切换到已有分支

```
$ git switch ##
```

#### stash

存档当前工作区，进行debug工作

```
$ git stash
```

显示当前stash中的内容

```
$ git stash list
```

从stash中恢复

```
$ git stash apply <版本号>
```

从stash中删除

```
$ git stash drop <版本号>
```

恢复+删除

```
$ git stash pop
```

#### cherry-pick

复制一个特定的提交到当前分支（用来修多个分支的bug）

```
$ git cherry-pick <hash of a commit>
```

### 冲突

手动解决。 远程分支发生冲突，先pull，本地手动解决后push

#### rebase

把分叉的提交历史“整理”成一条直线，看上去更直观。缺点是本地的分叉提交已经被修改过了。

```
$ git rebase
```

## Tag

打tag（打在最近的commit上

```
$ git tag ##
$ git tag ## <commit id>
```

查看tag

```
$ git tag
```

显示tag的信息

```
$ git show <tagname>
```

带说明的tag

```
$ git tag -a <tagname> -m "" <commit id>
```

删除标签

```
$ git tag -d <tagname>
```

以上的tag都是本地的

将本地tag推送到远程

```
$ git push origin <tagname>
$ git push origin --tags   //all tags
//本地删除tag后删除远程的tag
$ git push origin :refs/tags/<tagname>
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

## 自定义git

显示颜色

```
$ git config --global color.ui true
```

#### .gitignore

https://github.com/github/gitignore

强行添加被ignore的文件

```
$ git add -f ##
```

提交某个文件不成功，查找是否是ignore的锅：

```
$ git check-ignore -v ##
```

```
!##     //##将不会被ignore
*.in    // ignore以.in为后缀的文件，通配字符*
```

#### alias

定义命令的别名

```
$ git config --global alias.## ###
//例如
$ git config --global alias.st status

git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

显示配置文件

```
$ cat .git/config 
```

#### 搭建git服务器

https://www.liaoxuefeng.com/wiki/896043488029600/899998870925664