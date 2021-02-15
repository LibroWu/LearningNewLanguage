## shell脚本

* #### 标记

`#! /bin/bash` 告诉系统脚本需要用什么解释器来执行

* #### 运行

1、作为可执行文件

```
chmod +x path/filename.sh
path/filename.sh
```

2、作为解释器参数

```
/bin/sh test.sh
/bin/php test.php
bash test.sh
```

* #### 变量

1、赋值

​	显式赋值`variable_name=blahblah`

​	语句赋值

​		`for variable in 'ls /etc'`

​		`for variable in $(ls /etc)`

```
for skill in Ada Coffe Action Java; do
    echo "I am good at ${skill}Script"
done
```

2、使用

​	`$(variable)`

3、只读声明

​	`readonly variable_name`

4、删除变量

​	`unset variable_name`

* #### 字符串

1、单引号

​		原样输出，变量无效

​		单引号字串中不能出现单独一个的单引号（对单引号使用转义符后也不行），但可成对出现，作为字符串拼接使用。

2、双引号

​		可有变量和转义字符

3、获取长度

```
string="abcd"
echo ${#string} #输出 4
```

4、提取子字符串

```
string="runoob is a great site"
echo ${string:1:4} # 输出 unoo
string:start:end (0 based)
```

5、查找子字符串

```
string="runoob is a great site"
echo `expr index "$string" io`  # 输出 4
```

* #### 数组

```c++
array_name=(v0 v1 v2 v3)
//or
array_name[0]=v0
array_name[3]=v3
//all
array_name[@]
```

获取数组长度的方法与获取字符串长度的方法相同，例如：

```
# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度
lengthn=${#array_name[n]}
```

* #### 注释

单行`#` 

多行

```
:<<flag

flag
```

* #### input

##### 命令行参数

有点像匿名数组

类似c++的argv数组，第一个参数是被执行的文件路径

`$n`即可调用这些传入参数

`$#`是`argc`

**当n>=10时，需要使用${n}来获取参数**

未来可能有用

| $*   | 以一个单字符串显示所有向脚本传递的参数。 如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。 |
| ---- | ------------------------------------------------------------ |
| $$   | 脚本运行的当前进程ID号                                       |
| $!   | 后台运行的最后一个进程的ID号                                 |
| $@   | 与$*相同，但是使用时加引号，并在引号中返回每个参数。 如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。 |
| $-   | 显示Shell使用的当前选项，与[set命令](https://www.runoob.com/linux/linux-comm-set.html)功能相同。 |
| $?   | 显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。 |

##### read

```
read var
```

从标准输入中读取一行存入var中

* #### 运算

`expr`

```
`expr 2 + 2`
```

注意空格，表达式和运算符之间要有空格

条件表达式要放在`[]`中

##### 布尔运算符

0为true

| 运算符 | 说明                                                | 举例                                     |
| :----- | :-------------------------------------------------- | :--------------------------------------- |
| !      | 非运算，表达式为 true 则返回 false，否则返回 true。 | [ ! false ] 返回 true。                  |
| -o     | 或运算，有一个表达式为 true 则返回 true。           | [ $a -lt 20 -o $b -gt 100 ] 返回 true。  |
| -a     | 与运算，两个表达式都为 true 才返回 true。           | [ $a -lt 20 -a $b -gt 100 ] 返回 false。 |

##### 关系运算符

数值

| 运算符 | 说明                                                  | 举例                       |
| :----- | :---------------------------------------------------- | :------------------------- |
| -eq    | 检测两个数是否相等，相等返回 true。                   | [ $a -eq $b ] 返回 false。 |
| -ne    | 检测两个数是否不相等，不相等返回 true。               | [ $a -ne $b ] 返回 true。  |
| -gt    | 检测左边的数是否大于右边的，如果是，则返回 true。     | [ $a -gt $b ] 返回 false。 |
| -lt    | 检测左边的数是否小于右边的，如果是，则返回 true。     | [ $a -lt $b ] 返回 true。  |
| -ge    | 检测左边的数是否大于等于右边的，如果是，则返回 true。 | [ $a -ge $b ] 返回 false。 |
| -le    | 检测左边的数是否小于等于右边的，如果是，则返回 true。 | [ $a -le $b ] 返回 true。  |

字符串

| -z   | 检测字符串长度是否为0，为0返回 true。        | [ -z $a ] 返回 false。  |
| ---- | -------------------------------------------- | ----------------------- |
| -n   | 检测字符串长度是否不为 0，不为 0 返回 true。 | [ -n "$a" ] 返回 true。 |
| $    | 检测字符串是否为空，不为空返回 true。        | [ $a ] 返回 true。      |

文本

| -b file | 检测文件是否是块设备文件，如果是，则返回 true。              | [ -b $file ] 返回 false。 |
| ------- | ------------------------------------------------------------ | ------------------------- |
| -c file | 检测文件是否是字符设备文件，如果是，则返回 true。            | [ -c $file ] 返回 false。 |
| -d file | 检测文件是否是目录，如果是，则返回 true。                    | [ -d $file ] 返回 false。 |
| -f file | 检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。 | [ -f $file ] 返回 true。  |
| -g file | 检测文件是否设置了 SGID 位，如果是，则返回 true。            | [ -g $file ] 返回 false。 |
| -k file | 检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。  | [ -k $file ] 返回 false。 |
| -p file | 检测文件是否是有名管道，如果是，则返回 true。                | [ -p $file ] 返回 false。 |
| -u file | 检测文件是否设置了 SUID 位，如果是，则返回 true。            | [ -u $file ] 返回 false。 |
| -r file | 检测文件是否可读，如果是，则返回 true。                      | [ -r $file ] 返回 true。  |
| -w file | 检测文件是否可写，如果是，则返回 true。                      | [ -w $file ] 返回 true。  |
| -x file | 检测文件是否可执行，如果是，则返回 true。                    | [ -x $file ] 返回 true。  |
| -s file | 检测文件是否为空（文件大小是否大于0），不为空返回 true。     | [ -s $file ] 返回 true。  |
| -e file | 检测文件（包括目录）是否存在，如果是，则返回 true。          | [ -e $file ] 返回 true。  |
|-S|判断某文件是否socket||
|-L|检查文件是否存在并且是一个符号链接|

* #### echo

自动换行，`\c`不换行

```
echo -e "" 开启转义
echo -n "" 不换行
```
* #### printf

```
printf  format-string  [arguments...]
```

**%s %c %d %f** 都是格式替代符，**％s** 输出一个字符串，**％d** 整型输出，**％c** 输出一个字符，**％f** 输出实数，以小数形式输出。

%- *len* s 

%- *a.b* f

* ##### 分支循环

`if …… then …… elif …… then …… else …… fi `

```
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done
```

```
while condition
do
    command
done
```

```
until condition
do
    command
done
```

```shell
case 值 in
模式1)
    command1
    command2
    ...
    commandN
    ;;
模式2）
    command1
    command2
    ...
    commandN
    ;;
esac

#eg
while :
do
    echo -n "输入 1 到 5 之间的数字: "
    read aNum
    case $aNum in
        1|2|3|4|5) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 1 到 5 之间的!"
            continue
            echo "游戏结束"
        ;;
    esac
done
```

* #### 函数

函数是脚本中的脚本，可以用类似命令行的方式传入参数

```shell
fun(){
    echo "Hello"
    return $(($aNum+$anotherNum)) #可省略
}
```

* #### 重定向


| \> | 重定向stdout |
|----|----|
| \>\> | 重定向stdout并追加输出到文件末尾 |
| 2\> | 重定向stderr |

```
command << delimiter
    document
delimiter
```

##### /dev/null 文件

如果希望执行某个命令，但又不希望在屏幕上显示输出结果，那么可以将输出重定向到 /dev/null：

```
$ command > /dev/null
```

/dev/null 是一个特殊的文件，写入到它的内容都会被丢弃；如果尝试从该文件读取内容，那么什么也读不到。但是 /dev/null 文件非常有用，将命令的输出重定向到它，会起到"禁止输出"的效果。

如果希望屏蔽 stdout 和 stderr，可以这样写：

```
$ command > /dev/null 2>&1
```

* #### 使用外部脚本

```
. path
source path
```



* #### 其他

##### 通配符 *

于是乘法得用`\*`来表示

##### ;

`;`的效果与回车相同，可将多行命令压缩成一行