Mackdown 语法

# 这是一级标题
## 这是二级标题
### 这是三级标题
#### 这是四级标题
##### 这是五级标题
###### 这是六级标题

**这是加粗的文字**
*这是倾斜的文字*`
***这是斜体加粗的文字***
~~这是加删除线的文字~~


>这是引用的内容
>>这是引用的内容
>>
>>>>>>>>>这是引用的内容

---
----
***
****
*****

![图片alt](图片地址 ''图片title'')

图片alt就是显示在图片下面的文字，相当于对图片内容的解释。
图片title是图片的标题，当鼠标移到图片上时显示的内容。title可加可不加

![blockchain](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/
u=702257389,1274025419&fm=27&gp=0.jpg "区块链")

上传本地图片直接点击导航栏的图片标志，选择图片即可

markdown格式追求的是简单、多平台统一。那么图片的存储就是一个问题，需要用图床，提供统一的外链，这样就不用在不同的平台去处理图片的问题了。才能做到书写一次，各处使用。

超链接
[超链接名](超链接地址 "超链接title")
title可加可不加
[简书](http://jianshu.com)
[百度](http://baidu.com)
注：Markdown本身语法不支持链接在新页面中打开，貌似简书做了处理，是可以的。别的平台可能就不行了，如果想要在新页面中打开的话可以用html语言的a标签代替。
<a href="超链接地址" target="_blank">超链接名</a>
示例
<a href="https://www.jianshu.com/u/1f5ac0cf6a8b" target="_blank">简书</a>

## 列表
无序列表

- 内容
* 内容
+ 内容

有序列表
1. a
2. b
3. c

列表嵌套
上一级和下一级之间敲三个空格即可

* 一级
   1. 二级
   2. 二级
   3. 二级
+ 一级级
   * 二级
   * 二级
   * 二级

表格//注意与表格相隔一行

| 表头 | 表头 | 表头 |
| ---: | ---: | ---: |
| 内容 | 内容 | 内容 |
| 内容 | 内容 | 内容 |

第二行分割表头和内容。
- 有一个就行，为了对齐，多加了几个
文字默认居左
-两边加：表示文字居中
-右边加：表示文字居右
注：原生的语法两边都要用 | 包起来。此处省略

代码
`#include`
```
  代码...
  代码...
  代码...
```
流程图
```flow
st=>start: 开始
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
&```
```