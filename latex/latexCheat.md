## 头文件及基础结构

#### 宏包

* `\documentclass{article}`

源文件类型，其他有IEEE/mcmthesis/ctexart/SJTUThesis

可定义格式`\documentclass[a4paper,12pt]{article}`设置为A4，12pt的格式

* `\usepackage{...}`加载宏包

一些常用宏包

​	`color`  设置颜色 背景颜色 `\colorbox{red}`  字体颜色`\color{blue}`

​	`UTF8` : `\usepackage{UTF8}{ctex}`

​	`ctex`

​	`times` 设置为 times new roman 字体

​	`amssyymb`一些符号的显示

```undefined
\usepackage{xeCJK} % 中文支持
\usepackage{amsmath, amsthm}
\usepackage{listings,xcolor}  %插入代码
\usepackage{geometry} % 设置页边距
\usepackage{fontspec}
\usepackage{graphicx}
\usepackage{fancyhdr} % 自定义页眉页脚
```

#### 环境设置

##### 字体、纸张

```latex
\setsansfont{Consolas} % 设置英文字体
\setmonofont[Mapping={}]{Consolas} % 英文引号之类的正常显示，相当于设置英文字体
\geometry{left=1cm,right=1cm,top=2cm,bottom=0.5cm} % 页边距
\setlength{\columnsep}{30pt}  %两栏之间的间距大小
% \setlength\columnseprule{0.4pt} % 分割线
```

##### 页眉页脚设置

```latex
% 页眉、页脚设置
\pagestyle{fancy}
% \lhead{CUMTB}
\lhead{\CJKfamily{hei} 将作用域中文字体的格式为"黑体"。}
\chead{}
% \rhead{Page \thepage}
\rhead{\CJKfamily{hei} 第 \thepage 页}
\lfoot{} 
\cfoot{}
\rfoot{}
\renewcommand{\headrulewidth}{0.4pt} 
\renewcommand{\footrulewidth}{0.4pt}
%代码中只保留了页眉的左、右部分，舍弃了页脚（\lfoot,\cfoot,\rfoot）和页眉中间部分（\chead），如有需要可以自行添加。
%\thepage 显示当前页数。
%\renewcommand 是命令重定义指令，有点类似于C语言中的#define，这里是设置页眉实线（\headrulewidth）和页脚实线（\footrulewidth）的宽度。
```

##### 代码格式

```latex
% 代码格式设置 \listings宏包
\lstset{
    language    = c++,
    numbers     = left,
    numberstyle = \tiny,
    breaklines  = true,
    captionpos  = b,
    tabsize     = 4,
    frame       = shadowbox,
    columns     = fullflexible,
    commentstyle = \color[RGB]{0,128,0},
    keywordstyle = \color[RGB]{0,0,255},
    basicstyle   = \small\ttfamily,
    stringstyle  = \color[RGB]{148,0,209}\ttfamily,
    rulesepcolor = \color{red!20!green!20!blue!20},
    showstringspaces = false,
}
```

##### 基本格式

文件结构的基本模式https://www.jianshu.com/p/15b235f291fa

```latex
\documentclass[option]{class}  %文档类声明
\usepackage[option]{package}  %序言
\begin{document}  %正文
...
\end{document}
```

![img](https://upload-images.jianshu.io/upload_images/9874038-bc0d949a4e2528f6.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/887/format/webp)

## 标题、摘要、层次、目录

#### 标题

```undefined
\title{标题}  %“标题”处写上文章标题
\author{作者}  %“作者”处写上文章作者
\today  %编译生成文章时的日期
\date{\today}
\maketitle
```

##### 自定义标题

例子：

通过重定义`maketitle` 函数，调整标题结构，加入新元素

```
\makeatletter

\def\@maketitle{%
  \vskip 2em%
  \begin{center}%
  \let \footnote \thanks
\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{shanghaijiaotongdaxue.png}
    \caption*{\LARGE SHANGHAI JIAO TONG UNIVERSITY}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.2\textwidth]{round.png}
    \label{fig:my_label}
\end{figure}
    {\LARGE \@title \par}%
    \vskip 1.5em%
    {\large
      \lineskip .5em%
      \begin{tabular}[t]{c}%
        \@author
      \end{tabular}\par}%
    \vskip 1em%
A Paper Submitted to Associate Professor Wei Yaoyu for the Course\\
Academic Communication in English: Writing and Presentation
    \vskip 1em%
    {\large \@date}%
  \end{center}%
  \par
  \vskip 1.5em}
\makeatother
```

#### 摘要

```csharp
\begin{abstract}
...
\end{abstract}
```

#### 层次

```latex
\chapter{...}  %article 中无chapter
\section{...}  
\subsection{...}
\subsubsection{...}
\chapter*{...} %取消层次标号（目录和正文同时取消）
\section*{...}


\setcounter{secnumdepth}{0} %设置层次深度
\setcounter{secnumdepth}{2}
```

#### 目录

```latex
\tableofcontents
\setcounter{tocdepth}{2}  %设置深度为2
\renewcommand{\contentsname}{目录} %将生成的"Content"改写成中文的"目录"。
```

## 列表

```latex
\documentclass{article}
\begin{document}
\begin{itemize}  %点
  \item First
  \item Second
  \item Third
\end{itemize}

\begin{enumerate} %number
  \item First
  \item Second
  \item Third
\end{enumerate}

\begin{description} %First...
  \item{First} aaa
  \item{Second} bbb
  \item{Third} ccc
\end{description}
\end{document}
```

## 插入图片

```latex
%单图
\begin{figure}[H]
    \centering
    \includegraphics[width=0.2\textwidth]{round.png}
    \label{fig:my_label}
    %\caption*{Pic.3}
\end{figure}

%多图
\begin{figure}[H] 
\centering  
\subfigure[{\normalsize1.1 General view of original image}]{
\label{Fig.sub.1}
\includegraphics[width=0.45\textwidth]{P1.png}}
\subfigure[{\normalsize1.2 General view of transferred image}]{
\label{Fig.sub.2}
\includegraphics[width=0.45\textwidth]{P2.png}}
\label{Fig.main}
\end{figure}
```

## 插入代码

```latex
\begin{lstlisting}
#include <iostream>
using namespace std;
int main(){
  cout<<"Hello,world!"<<endl;
  return 0;
}
\end{lstlisting}
```

	##  math及符号

#### 常用表达

```latex
\begin{dispalymath} \end{displaymath}
\begin{equation} \end{equation}
\[E=mc^2\]

^ _{} %上下标

\sqrt \sqrt[n] \surd %平方根 surd来手动调整大小

\overline \underline %在表达式上下方画出水平线

\overbrace \underbrace  %大括号
$\underbrace{a+b+\cdots+z}_{26}$

\vec \overrightarrow \overleftarrow %向量

\frac{分子}{分母}

\sum \prod \int%求和 连乘 积分
\sum_{i=1}^{n}
\int_{0}^{\frac{\pi}{2}}
\prod_\epsilon

\qquad %空格
```

![math](D:\workspace\libro_workspace\LearningNewLanguage\latex\math.png)

------

![math2](D:\workspace\libro_workspace\LearningNewLanguage\latex\math2.png)

-------

![math4](D:\workspace\libro_workspace\LearningNewLanguage\latex\math4.png)

------

![math5](D:\workspace\libro_workspace\LearningNewLanguage\latex\math5.png)

------------------

![math6](D:\workspace\libro_workspace\LearningNewLanguage\latex\math6.png)

----------------------

![math7](D:\workspace\libro_workspace\LearningNewLanguage\latex\math7.png)

---------------

#### 常用数学符号

```python
MATH_SYMBOLS = {
  'aleph', 'alpha', 'beta', 'beth', 'chi', 'daleth',
  'delta', 'digamma', 'epsilon', 'eta', 'gamma', 'gimel',
  'iota', 'kappa', 'lambda', 'mu', 'nu', 'omega', 'omega',
  'phi', 'pi', 'psi', 'rho', 'sigma', 'tau', 'theta',
  'upsilon', 'varepsilon', 'varkappa', 'varphi', 'varpi', 'varrho',
  'varsigma', 'vartheta', 'xi', 'zeta', 'Delta', 'Gamma',
  'Lambda', 'Omega', 'Phi', 'Pi', 'Sigma', 'Theta',
  'Upsilon', 'Xi',
}

BUILTIN_CALLEES = {
  'abs': (r'\left|{', r'}\right|'),
  'math.acos': (r'\arccos{\left({', r'}\right)}'),
  'math.acosh': (r'\mathrm{arccosh}{\left({', r'}\right)}'),
  'math.asin': (r'\arcsin{\left({', r'}\right)}'),
  'math.asinh': (r'\mathrm{arcsinh}{\left({', r'}\right)}'),
  'math.atan': (r'\arctan{\left({', r'}\right)}'),
  'math.atanh': (r'\mathrm{arctanh}{\left({', r'}\right)}'),
  'math.ceil': (r'\left\lceil{', r'}\right\rceil'),
  'math.cos': (r'\cos{\left({', r'}\right)}'),
  'math.cosh': (r'\cosh{\left({', r'}\right)}'),
  'math.exp': (r'\exp{\left({', r'}\right)}'),
  'math.fabs': (r'\left|{', r'}\right|'),
  'math.factorial': (r'\left({', r'}\right)!'),
  'math.floor': (r'\left\lfloor{', r'}\right\rfloor'),
  'math.fsum': (r'\sum\left({', r'}\right)'),
  'math.gamma': (r'\Gamma\left({', r'}\right)'),
  'math.log': (r'\log{\left({', r'}\right)}'),
  'math.log10': (r'\log_{10}{\left({', r'}\right)}'),
  'math.log2': (r'\log_{2}{\left({', r'}\right)}'),
  'math.prod': (r'\prod \left({', r'}\right)'),
  'math.sin': (r'\sin{\left({', r'}\right)}'),
  'math.sinh': (r'\sinh{\left({', r'}\right)}'),
  'math.sqrt': (r'\sqrt{', '}'),
  'math.tan': (r'\tan{\left({', r'}\right)}'),
  'math.tanh': (r'\tanh{\left({', r'}\right)}'),
  'sum': (r'\sum \left({', r'}\right)'),
}
```

#### 常用其他符号

![img](https://upload-images.jianshu.io/upload_images/9874038-ceef1cccb06ffb34.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/874/format/webp)

## 引用

#### 参考文件类型设置

```latex
\bibliographystyle{plain}
%unsrt – 基本上跟 plain 类型一样，除了参考文献的条目的编号是按照引用的顺序，而不是按照作者的字母顺序.
%alpha – 类似于 plain 类型，当参考文献的条目的编号基于作者名字和出版年份的顺序.
%abbrv – 缩写格式 .
```



#### 不适用BibTex

```latex
\renewcommand\refname{Reference} %重定义引用列表的名字
\begin{thebibliography}{99}  
\addcontentsline{toc}{section}{Reference} 
\bibitem{ref1}Harmsen, J.J. and Pearlman, W.A. (2003) Steganalysis of Additive-Noise Modelable Information Hiding. SPIE Proceedings, 5020, 131-142. https://doi.org/10.1117/12.476813
\bibitem{ref2}Ker, A.D. (2005) Steganalysis of LSB Matching in Grayscale Images. IEEE Signal Processing Letters, 12, 441-444. https://doi.org/10.1109/LSP.2005.847889
\bibitem{ref3}Pevn`y, T., Filler, T. and Bas, P. (2010) Using High-Dimensional Image Models to Perform Highly Undetectable Steganography. Springer, Berlin.
\bibitem{ref4}Holub, V. and Fridrich, J. (2012) Designing Steganographic Distortion Using Directional Filters. IEEE International Workshop on Information Forensics and Security (WIFS), 2, 234-239. https://doi.org/10.1109/WIFS.2012.6412655
\bibitem{ref5}Sedighi, V., Cogranne, R. and Fridrich, J. (2016) Content-Adaptive Steganography by Minimizing Statistical Detectability. IEEE Transactions on Information Forensics and Security, 11, 221-234. https://doi.org/10.1109/TIFS.2015.2486744
\bibitem{ref6}Killshadow. 隐写术(一)--简介. https://www.killshadow.xyz/2019/05/29/\%E9\%9A\%90\%E5\%86\%99\%E6\%9C\%AF(\%E4\%B8\%80)--\%E7\%AE\%80\%E4\%BB\%8B/
\end{thebibliography}

\bibliography{thebibliography} %列出引用列表
%正文中引用参考文献
\cite{ref1}
\cite{ref1, ref5}
```

#### 使用BibTex

```latex
@article{name1,
author = {作者, 多个作者用 and 连接},
title = {标题},
journal = {期刊名},
volume = {卷20},
number = {页码},
year = {年份},
abstract = {摘要, 这个主要是引用的时候自己参考的, 这一行不是必须的}
}
@book{name2,
author ="作者",
year="年份2008",
title="书名",
publisher ="出版社名称"
}
%列表
\bibliography{bibfile}
```



## 微小命令

##### 日期相关

```latex
\year
\month
\day
\today
\renewcommand{\today}{\number\year 年 \number\month 月 \number\day 日}
```

##### 页码相关

```latex
\pagenumbering{Roman}
roman Roman arabic

\thispagestyle{empty}  %当前页无页码
\setcounter{page}{1}   %从当前页开始计算页数
\thepage               %显示当前page
```



