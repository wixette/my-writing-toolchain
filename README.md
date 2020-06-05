# 我的中文写作工具链

## 工具驱动的中文写作

在社交 APP 里，我有个签名是“用 Emacs 写小说”。很多人问我，用 Emacs 怎么写小说？

写代码是我的工作，中文写作是我的爱好。代码之外，我写作或发表过一些技术文章、技术图书、科普图书、科幻小说、散文、诗歌等。我的写作水平并不高明，但从写代码继承过来的习惯还是让我在技术上有别于主要用稿纸或 Word 写作的人。所谓“用 Emacs 写小说”只是个笼统的说法，其实我是在用一系列写代码时常用的软件工具来完成整个中文写作流程。

原因很简单，这样做效率更高。

记得八九十年代的作家常说“换笔”，那时“换笔”指的是把真的纸笔替换成可以打字的电脑。今天如果有人想“换”更厉害的笔，那我会推荐这套高效率的中文写作工具链——当然，前提是你要懂点简单的编程知识，或者会摆弄些电脑上的命令行工具。

## Markdown 格式

我很少用 Word 或 WPS 写作。更多时候（包括写这篇文章在内）是在一个最简单的文本编辑器里写 [Markdown](https://daringfireball.net/projects/markdown/) 格式的纯文本。少数情况下，我会先用 Markdown 格式打草稿，然后再打开 Word 等办公软件完成图表等高级任务。

和使用 Office 等大体量的办公软件相比，使用 Markdown 格式写作的好处有很多：

1. Markdown 随时随地都可以写，在电脑记事本里写，在手机 APP 里写，在印象笔记里写，在微信里写，在 iPad 上写，在 Github 等网页工具上写，在编程工具里写，在终端里写，在树莓派这样的廉价电脑里写……要是换成办公软件？真不是任何地方都能免费、快速打开 Word 来用的。
1. 用 Markdown 格式写出来的东西，可以方便地用版本管理系统如 Git 管理起来，或者丢进 Github，以便迅速同步到家里、办公室里、移动中的各种写作设备上。要是用 Git 管理体量巨大的 Word 文件，那让人头疼的地方可太多了。
1. 用 Markdown 格式写出来的东西，可以方便地比较两个版本甚至多个版本间的差别。——想想我们用 Word 比较两个文档版本差别时是有多费劲。
1. 用 Markdown 超快，超简单，更聚焦于内容本身。Markdown 写文本时可以只关注标题、列表、超链接、着重强调的词句或段落等少数与格式相关的事情。反之，在 Word 里我就经常会被繁琐的格式、样式设置分散精力。
1. 用 Markdown 很酷，写作时的自我感觉很好。

<img src="https://raw.githubusercontent.com/wixette/my-writing-toolchain/master/images/markdown_format.png" width="600">

不熟悉 Markdown 的，推荐阅读知乎问题[“怎样引导新手使用 Markdown？”](https://www.zhihu.com/question/20409634)下的高票回答。

## 中文段落的两种写作方法

使用 Markdown 格式写作中文内容，自然段落有两种写作方式，一种是每段一行，中间不加换行/回车符，编辑器可以开启“自动折行”功能。另一种方式是段内换行，每行只写差不多固定数目的文字，中间加上换行/回车符。无论中间换行不换行，Markdown 的段与段之间都使用单独的空行隔开。比如下面这样每行大约 35 汉字（或 70 英文字符）的写法：

```
栖芒是对的。我真的见过栖芒，而且是在十年以前。

和栖芒握手时，我的大脑仿佛瞬间浸入了一泓清水，无数潜藏在记忆暗区的场景
清晰地浮现在眼前。曾经被遗忘的记忆碎片，接二连三地回到大脑中负责长期记
忆的区域。当然，也有另一种可能，就是自己骤然进入了一个可以循时间脉络回
到记忆深处的平行宇宙。

我想起了许多原本不该想起的细节。
```

两种写法没有优劣之分。我个人偏爱每段之中换行的写法，这样整个 Markdown 里的中文段落整齐划一，在各个编辑器、各个平台、各种尺寸屏幕上都能正常显示。这种写法也便于快速定位每个具体字词在编辑器里的行号、列号。现在很多编辑器都支持边写作边自动换行，并按照每行的固定字数来自动排列内容。比如我在 Emacs 边写边按 M-q (fill-paragraph)，就可以自动将段落分行且各行填满固定字数。

### Markdown 中文段内换行在输出时会多一个空格的问题

使用上面说的中文段内换行的写作方式，在将 Markdown 输出成 HTML、PDF、Word 等文件时，会存在一个恼人的问题：输出后的文件在将多行显示为一个段落时，会在行与行之间自动插入一个空格。其实这是 HTML 处理多行连续文本的一个历史问题，完全是针对英文习惯设计的，因为英文上一行结尾的单词和下一行开头的单词，需要用一个空格来分开。

在 Github 上写 REAMDE.md 时，如果每段的中文分行来写，Github 一样会将这样的中文段落渲染成中间有空格的样子。这是今天 Github 上很多中文描述文件长得不太好看的原因之一。所以，这一篇 README.md 因为要在 Github 上展示，我也被迫放弃了我钟爱的段间分行样式。

那么，段间分行的中文 Markdown 文本，该如何正确输出到 HTML、PDF、Word 等格式呢？我目前使用两个方案：

#### 方案 1

我曾在 Markdown 作者最早发布的 Perl 脚本工具 [Markdown.pl 1.0.1](https://daringfireball.net/projects/downloads/Markdown_1.0.1.zip) 的基础上，做了一个代码改动，使得 Markdown 解析器在遇到第一行尾和下一行首都是中日韩全角字符的时候，自动删除两行之间的换行，这样就将同一段落的中文内容不加空格地连接在一起了。同时，我也考虑了第一行尾或下一行首同时是英文半角字符的情况，这种情况下，换行（或最终渲染出来的空格）还是需要保留的。

我对 Markdown.pl 1.0.1 加以修改以支持中日韩全角字符的代码发布在 [markdown-cjk](https://github.com/wixette/my-writing-toolchain/tree/master/markdown_cjk)，其中也包括二者之间差异的 diff 文件。

喜欢原生 Markdown.pl 的同学可以用这个工具来处理分行的中文段落。

#### 方案 2

今天流行的 Markdown 工具里，有少数几种通过插件的形式，可以正确（或近乎正确）地处理中日韩全角字符分行时的情况。其中我比较喜欢用的是 [pandoc](https://pandoc.org/)。使用 pandoc 时，可以通过一个名叫 `east_asian_line_breaks` 的插件来处理中文分行段落。

在 pandoc 中打开中日韩分行插件并输出 HTML 格式的命令写法是：

```
pandoc -f markdown+east_asian_line_breaks input.md
```

或：

```
pandoc -f markdown_strict+east_asian_line_breaks input.md
```

大多数情况下，推荐使用 pandoc。但 pandoc 在处理行尾、行首有英文半角字符时的规则，可能和有些人的期望不符，这时可以尝试上面提到的 [markdown-cjk](https://github.com/wixette/my-writing-toolchain/tree/master/markdown_cjk)。

## 文本编辑器

任何一个用着顺手，能编辑纯文本的编辑器都可以胜任 Markdown 格式的写作。Windows、MacOS、Linux 等操作系统上的记事本，网页里的编辑框，各种在线文档类的笔记工具、写作平台、微信小程序，手机上的记事本、备忘录，都能圆满完成写作工作。

当然，对程序员来说最理想的还是那些平常用来写程序的工具软件。传统程序员有两大派别——Vim 党和 Emacs 党。我是 Emacs 党，但从不说 Vim 的坏话。所以，用 Vim 写作还是用 Emacs 写作，完全看大家的心情就好。最近我还比较喜欢超轻量级的 nano，做些短平快的事情特别合适。Windows 上的 Notepad++ 也很棒。其他诸如 VS Code、Eclipse、Xcode 之类，都显得略重了些，不过也足以胜任写作任务。

各种代码编辑器都能针对 Markdown 中的不同样式，用不同颜色或字体显示。比如我在 Emacs 里会缺省安装并打开 [markdown-mode](https://jblevins.org/projects/markdown-mode/)。

其他还有一些小技巧。我在 Emacs 里会为中文写作的 Markdown 文本或其他纯文本设置较大的字号，而为 C++、JavaScript、Python 等代码编辑设置较小的字号，两者之间相差两到三档。这大概是因为写作文字时更希望聚焦核心内容，而写代码时更希望一眼看到更多信息吧。

我在 Emacs 里做的与中文写作有关的设置，可以参见我的 [Emacs 启动文件](https://github.com/wixette/my-writing-toolchain/blob/master/emacs/my-emacs-init-file.el)。

## Git 版本管理

虽然 Word 提供了强大的版本修订功能，但用的人很少。据说在用 Word 写作的人里，95% 以上是用文件名来管理不同版本的，如下图：

<img src="https://raw.githubusercontent.com/wixette/my-writing-toolchain/master/images/word_versions.png" width="400">

这不是版本管理，而是版本灾难。

所以，我坚持用 Git 来管理我的每一次写作、每一次修改。在 Git 的版本管理系统中，对同一个内容所做的所有修改，是一目了然的。

<img src="https://raw.githubusercontent.com/wixette/my-writing-toolchain/master/images/git_versions.png" width="400">

我们为每一个版本所做的增、删、改，都清楚地记录在案，随时可以调阅、复原。甚至可以使用 Git 分支来同时写作不同构思的内容——比如为一篇小说同时写作大团圆结局和“死光光”结局，然后在需要时，选用不同的结局。

需要 Git 入门的，推荐知乎问题[GitHub 入门方法有哪些？](https://www.zhihu.com/question/29929269)下的高票答案。

用了 Git，当然要接着用 Github——所谓的[全球最大同性交友网站](https://zhuanlan.zhihu.com/p/35618222)。以前 Github 是为开源社区服务的，所有免费进驻的个人项目都要开放给大家浏览或下载，这件事对于在创作时非常注意保密的内容创作者来说是不可接受的，我以前就被迫运营自己的 Git 服务器。好在今天的 Github 已经允许我们管理私有项目，不需要每个项目都公开。Git 宣布这个好消息时，我第一时间就把所有个人写作内容移到了 Github 的私有项目。使用 Github 的另一个好处是，所有写作内容都随时和云端同步，你从任何地方的任何一台设备上，都可以继续你的写作过程，不用带着 U 盘满世界跑，也不必担心丢电脑。

感谢 Github，也顺便宣传一下 Github 的吉祥物 [Octodex](https://octodex.github.com/)：

<img src="https://octodex.github.com/images/original.png" width="300">

## 版本差异比较

管理不同版本时，查看两个或多个版本之间的差异是程序员最熟悉的任务之一。但查看两份代码的差异，和查看两个版本中文文章间的差异，还是挺不一样的两件事：

* 代码的基本单元是“行”和“符号”，而中文文章的基本单元是“段”“句”“词”“字”。
* 比较两个版本的代码时，大多数时候都是一行对一行的比较。而比较两个版本中文文章时，一段对一段或一行对一行的比较就显得跨度太大了，很难理清楚其中的差异。

比如，对下面这个版本改动，Git 缺省的 diff 工具只能笼统显示两段是不同的，无法更进一步显示两段之间哪里不同：

<img src="https://raw.githubusercontent.com/wixette/my-writing-toolchain/master/images/git_diff.png" width="600">

Github 网页版使用的 diff 工具稍好一些，可以在段内不换行的中文里找出一些具体的差异位置，但这些差异仍然没有具体到能体现最小区别的字词级别，例如两个版本第一句话中本来只有“示例”和“测试”的区别，但 Github 用深红、深绿标注的差异部分却扩大到了“示例的中文文本”和“测试的中文文本”。至于分行的中文段落，Github diff 就更无法区分其中的差异位置了。见下图：

<img src="https://raw.githubusercontent.com/wixette/my-writing-toolchain/master/images/github_diff.png" width=800>

Git 和 Github 的 diff 工具在粒度上是无法满足中文写作的要求的。有不少好的 diff 工具可以在更细的粒度上对文本内容进行比较。其中有一些是收费的商业产品。免费的工具里，我自己简单使用 Google 开源的 [diff-match-patch](https://github.com/google/diff-match-patch) 代码库，并在其基础上包装了一个 Python 命令行小工具，叫 [googdiff](https://github.com/wixette/googdiff)。

我发布的这个小工具可以单独使用，也可以嵌入 Git 命令行使用。要安装这个工具，可以：

```
pip3 install googdiff
```

安装后，可以用下面的命令行比较两个本地文件，googdiff 既可以在命令行终端比较结果：

```
googdiff samples/diff_example_english_pair_01.txt samples/diff_example_english_pair_02.txt
```

也可以打开浏览器来展示比较结果：

```
googdiff -b samples/diff_example_english_pair_01.txt samples/diff_example_english_pair_02.txt
```

也可以将 googdiff 与 git 集成使用，即，用 googdiff 来展示 git diff 的结果，像这样：

```
git difftool -y --extcmd=googdiff

```

或者显示两个 tag 之间某文件的版本变化：

```
git difftool -y --extcmd=googdiff after before -- samples/diff_example_chinese.txt
```

googdiff 的比较结果与上面 Git 或 Github 的 diff 工具相比，就细化了很多，可以将每一处细小的改动用红色或绿色显示出来，如下图：

<img src="https://raw.githubusercontent.com/wixette/my-writing-toolchain/master/images/googdiff1.png" width="600">

无论是完整的中文段落，还是分行写的中文段落，googdiff 都会尽量精确地展示其中的差异：

<img src="https://raw.githubusercontent.com/wixette/my-writing-toolchain/master/images/googdiff2.png" width="600">

## 输出与发布

将 Markdown 格式文本转换成 HTML、PDF、Word 等格式的工具很多，我个人还是比较喜欢用 [pandoc](https://pandoc.org/)。

pandoc 的使用方式很简单，参见 [Getting started with pandoc](https://pandoc.org/getting-started.html) 或者知乎上的 [pandoc 话题](https://www.zhihu.com/topic/19862254/hot)。

例如，用 pandoc 将本文转换成 HTML：

```
pandoc README.md -o readme.html
```

用 pandoc 将本文转换成 Word 文档：

```
pandoc README.md -t docx -o readme.docx
```

有了 HTML 或 Word 文档，后续就可以在网页设计软件、办公软件或排版软件里，对我们写好的文稿进行加工、补全、排版和发布了。

## 最后两句话

以上工具选择其实只是我的个人喜好。高效工作方式有很多，萝卜白菜各有所爱。

有好用的工具，自然有高效率和好心情。祝大家写作愉快 :-)
