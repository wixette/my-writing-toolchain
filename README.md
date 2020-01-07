# 我的中文写作工具链

## 工具驱动的中文写作

在社交 APP 里，我有个签名是“用 Emacs 写小说”。很多人问我，你怎么用 Emacs 写小说？

写代码是我的工作，中文写作则是我的爱好。代码之外，我写作或发表过技术文章、技术图书、科普图书、科幻小说、散文、诗歌等等。我的写作水平并不高明，但从写代码继承过来的习惯还是让我在技术上有别于主要用稿纸或 Word 写作的人。所谓“用 Emacs 写小说”只是个笼统的说法，其实我是在用一系列写代码时常用的软件工具来完成整个中文写作流程。

原因很简单，这样做效率更高！

记得八九十年代的作家常说“换笔”，那时“换笔”指的是把真的纸笔替换成可以打字的电脑。今天如果有人想“换”更厉害的笔，那我会推荐这套高效率的中文写作工具链——当然，前提是你要懂点简单的编程知识，或者会摆弄些电脑上的命令行工具。

## Markdown 格式

我很少用 Word 或 WPS 写作。更多时候（包括写这篇文章在内）是在一个最简单的文本编辑器里写 [Markdown 格式](https://daringfireball.net/projects/markdown/)的纯文本。少数情况下，我会先用 Markdown 格式打草稿，然后再打开 Word 等办公软件完成图表等高级任务。

和使用 Office 等大体量的办公软件相比，使用 Markdown 格式写作的好处有很多：

1. Markdown 随时随地都可以写，在电脑记事本里写，在手机 APP 里写，在印象笔记里写，在微信里写，在 iPad 上写，在 Github 等网页工具上写，在编程工具里写，在终端里写，在树莓派这样的廉价电脑里写……要是换成办公软件？真不是任何地方都能免费、快速打开 Word 来用的。
1. 用 Markdown 格式写出来的东西，可以方便地用版本管理系统如 Git 管理起来，或者丢进 Github，以便迅速同步到家里、办公室里、移动中的各种写作设备上。要是用 Git 管理体量巨大的 Word 文件，就有的是头疼之处了。
1. 用 Markdown 格式写出来的东西，可以方便地比较两个版本甚至多个版本间的差别。想想我们用 Word 比较两个文档版本差别时是有多费劲。
1. 用 Markdown 超快，超简单。没有像 Word 一样繁琐的格式、样式设定来分散精力，就可以把更多的有效时间放在内容创作上。
1. 用 Markdown 很酷，自我感觉很好。

![Markdown 示例](https://raw.githubusercontent.com/wixette/my-writing-toolchain/master/images/markdown_format.png)

不熟悉 Markdown 的，推荐阅读知乎问题[“怎样引导新手使用 Markdown？”下的高票回答](https://www.zhihu.com/question/20409634)。

## 中文段落的两种写作方法

使用 Markdown 格式写作中文内容，自然段落有两种写作方式，一种是每段一行，中间不加换行/回车符，编辑器可以开启“自动折行”功能。另一种方式是段内换行，每行只写差不多固定数目的文字，中间加上换行/回车符。无论中间换行不换行，Markdown 的段与段之间都使用单独的空行隔开。比如下面这样每行大约 35 汉字（或 70 英文字符）的写法：

```
此开卷第一回也。作者自云：曾历过一番梦幻之后，故将真事隐去，而借通灵说
此《石头记》一书也，故曰“甄士隐”云云。但书中所记何事何人?自己又云：“今
风尘碌碌，一事无成，忽念及当日所有之女子：一一细考较去，觉其行止见识皆
出我之上。我堂堂须眉诚不若彼裙钗，我实愧则有馀，悔又无益，大无可如何之
日也。当此日，欲将已往所赖天恩祖德，锦衣纨之时，饫甘餍肥之日，背父兄
教育之恩，负师友规训之德，以致今日一技无成、半生潦倒之罪，编述一集，以
告天下；知我之负罪固多，然闺阁中历历有人，万不可因我之不肖，自护己短，
一并使其泯灭也。所以蓬牖茅椽，绳床瓦灶，并不足妨我襟怀；况那晨风夕月，
阶柳庭花，更觉得润人笔墨。我虽不学无文，又何妨用假语村言敷演出来?亦可
使闺阁昭传。复可破一时之闷，醒同人之目，不亦宜乎？”故曰“贾雨村”云云。
更于篇中间用“梦”“幻”等字，却是此书本旨，兼寓提醒阅者之意。
```

两种写法没有优劣之分。我个人偏爱每段之中换行的写法，这样整个 Markdown 里的中文段落整齐划一，在各个编辑器、各个平台、各种尺寸屏幕上都能正常显示。很多编辑器都支持边写作边自动换行并对齐每行字数，比如我在 Emacs 边写边按 M-q (fill-paragraph)，就可以自动将段落分行且各行填满固定字数。

### Markdown 中文段内换行在输出时会多一个空格的问题

使用上面说的中文段内换行的写作方式，在将 Markdown 输出成 HTML、PDF、Word 等文件时，会存在一个恼人的问题：输出后的文件在将多行显示为一个段落时，会在行与行之间自动插入一个空格。其实这是 HTML 处理多行连续文本的一个历史问题，完全是针对英文的使用习惯设计的，因为英文上一行结尾的单词和下一行开头的单词，需要用一个空格来分开。

在 Github 上写 REAMDE.md 时，如果每段的中文分行来写，Github 一样会将这样的中文段落渲染成中间有空格的样子。这是今天 Github 上很多中文描述文件长得不太好看的原因之一。所以，这一篇 README.md，因为要在 Github 上展示，我也只好放弃了我钟爱的段间分行样式。

那么，段间分行的中文文本，该如何正确输出到 HTML、PDF、Word 等格式呢？我目前使用两个方案：

#### 解决方案 1

我曾在 Markdown 作者最早发布的 Perl 脚本工具 [Markdown.pl 1.0.1](https://daringfireball.net/projects/downloads/Markdown_1.0.1.zip) 的基础上，做了一个代码改动，使得 Markdown 解析器在遇到第一行尾和下一行首是中日韩全角字符的时候，自动删除两行之间的换行，这样就将同一段落的中文内容完美、不加空格地连接在一起了。同时，我也考虑了第一行尾或下一行首同时是英文半角字符的情况，这种情况下，换行（或最终渲染出来的空格）还是需要保留的。

我对 Markdown.pl 1.0.1 加以修改以支持中日韩全角字符的代码发布在 [markdown-cjk](https://github.com/wixette/my-writing-toolchain/tree/master/markdown_cjk)，其中也包括二者之间差异的 diff 文件。

喜欢原生 Markdown.pl 的同学可以使用这个工具来处理分行的中文段落。

#### 解决方案 2

今天流行的 Markdown 工具里，有少数几种通过插件的形式，可以正确（或近乎正确）地处理中日韩全角字符分行时的情况。其中我比较喜欢用的是 [pandoc](https://pandoc.org/)。使用 pandoc 时，可以通过一个名叫 `east_asian_line_breaks` 的插件来处理中文分行段落。

在 pandoc 中打开中日韩分行插件并输出 HTML 格式的命令写法是：

```
pandoc -f markdown_strict+east_asian_line_breaks input.md
```

大多数情况下，推荐使用 pandoc。但 pandoc 在处理行尾、行首有英文半角字符时的规则，可能和有些人的期望不符，这时可以尝试上面提到的 markdown-cjk。

## 编辑器

任何一个用着顺手，能编辑纯文本的编辑器都可以胜任 Markdown 格式的写作。Windows、MacOS、Linux 等操作系统上的记事本，网页里的编辑框，各种在线文档类的笔记工具、写作平台、微信小程序，手机上的记事本，都能圆满完成写作工作。当然，对程序员来说最理想的还是那些平常用来写程序的工具软件。

传统程序员有两大“宗教”——VIM 和 Emacs。我是 Emacs 党，但从不说 VIM 的坏话。所以，用 VIM 写作还是用 Emacs 写作，完全看心情。最近我还比较喜欢超轻量级的 nano，做些短平快的事情特别合适。Windows 上的 Notepad++ 也很棒。其他诸如 VS Code、Eclipse、Xcode 之类，都显得略重了些，不过也足以胜任写作任务。

各种代码编辑器都能针对 Markdown 中的不同类型内容，用不同颜色或字体显示。我在 Emacs 里会缺省安装并打开 [markdown-mode](https://jblevins.org/projects/markdown-mode/)。

其他还有一些小技巧，比如我在 Emacs 里会为中文写作的 Markdown 文本或其他纯文本设置较大的字号，而为 C++、JavaScript、Python 等代码编辑设置较小的字号，两者之间相差两到三档。这大概是因为写作文字时更希望关注某些聚焦的内容，而写代码时更希望一眼看到更多的信息量吧。

我在 Emacs 里做的与中文写作有关的设置，可以参见我的 [Emacs 启动文件](https://github.com/wixette/my-writing-toolchain/blob/master/emacs/my-emacs-init-file.el)。

## Git 版本管理

虽然 Word 提供了强大的版本修订功能，但用的人很少。据说在用 Word 写作的人里，90% 以上是用文件名来管理不同版本的，如下图：

![Word 版本管理](https://raw.githubusercontent.com/wixette/my-writing-toolchain/master/images/word_versions.png)

这不是版本管理，而是版本灾难。

所以，我坚持用 Git 来管理我的每一次写作、每一次修改。在 Git 的版本管理系统中，对同一个内容所做的所有修改，是一目了然的。

![Git 版本管理](https://raw.githubusercontent.com/wixette/my-writing-toolchain/master/images/git_versions.png)

我们为每一个版本所做的增、删、改，都清楚地记录在案，随时可以调阅、复原。甚至可以使用分支同时写作不同构思的内容（比如为一篇小说同时写作大团圆结局和“死光光”结局），然后在需要时，选用不同的构思。

需要 Git 入门的，推荐知乎问题[GitHub 入门方法有哪些？](https://www.zhihu.com/question/29929269)下的高票答案。

用了 Git，当然要接着用 Github——所谓的[全球最大同性交友网站](https://zhuanlan.zhihu.com/p/35618222)。以前 Github 是为开源社区服务的，所有免费进驻的个人项目都要开放给大家浏览或下载，这件事对于在创作时非常注意保密的内容创作者来说是不友好的。好在 Github 已经允许我们管理私有项目。当时传出这个好消息时，我第一时间就把我的所有个人写作内容移到了 Github 的私有项目里。

感谢 Github，宣传一下 Github 的吉祥物 [Octodex](https://octodex.github.com/)：

![Octodex](https://octodex.github.com/images/original.png)

## Diff 版本差异比较以及 googdiff 小工具

管理不同版本时，查看两个或多个版本之间的差异是程序员最熟悉的任务之一。但查看两份代码的差异，和查看两个版本中文文章间的差异，还是挺不一样的两件事。代码的基本单元是“行”和“符号”，而中文文章的基本单元是“段”“句”“词”“字”。比较两个版本的代码时，大多数时候都是一行对一行的比较。而比较两个版本中文文章时，一段对一段的比较显得跨度太大，很难理清楚其中的差异。比如，对下面这个版本修改，Git 缺省的 diff 工具只能笼统显示两段是不同的，无法更进一步显示两段之间哪里不同：

![git diff](https://raw.githubusercontent.com/wixette/my-writing-toolchain/master/images/git_diff.png)

Github 网页版使用的 diff 工具稍好一些，可以在段内不换行的中文里找出一些具体的差异位置，但这些差异仍然没有具体到能体现最小区别的字词级别，例如两个版本第一句话中本来只有“示例”和“测试”的区别，但 Github 用深红、深绿标注的差异部分却扩大到了“示例的中文文本”和“测试的中文文本”。至于分行的中文段落，Github diff 就更是无法区分其中的差异位置了。见下图：

![github diff](https://raw.githubusercontent.com/wixette/my-writing-toolchain/master/images/github_diff.png)

Git 和 Github 的 diff 工具在粒度上是无法满足中文写作的要求的。有不少好的 diff 工具可以在更细的粒度上对文本内容进行比较。其中有一些是收费的商业产品。免费的工具里，我自己就简单使用 Google 开源的 diff-match-patch 代码库，并在这个代码库的基础上包装了一个 Python 命令行小工具，叫 [googdiff](https://github.com/wixette/my-writing-toolchain/tree/master/googdiff)。

这个工具可以单独使用，也可以嵌入 Git 命令行使用。要安装这个工具，可以使用 pip：

```
pip3 install googdiff
```

安装后，可以用下面的命令行比较两个本地文件，googdiff 缺省会打开浏览器来展示比较结果：

```
googdiff a.txt b.txt
```

也可以将 googdiff 与 git 集成使用，即，用 googdiff 来展示 git diff 的结果，像这样：

```

```

## 输出与发布

将 Markdown 格式文本转换成 HTML、PDF、Word 等格式的工具很多，我个人还是比较喜欢用[pandoc](https://pandoc.org/)。例如，用 pandoc 将本文转换成 HTML：

```
pandoc README.md -o readme.html
```

用 pandoc 将本文转换成 Word 文档：

```
pandoc README.md -t docx -o readme.docx
```

有了 HTML 或 Word 文档，后续就可以在网页设计软件或者办公软件里，对我们写好的文稿进行加工，添加更丰富的图表信息了。

pandoc 的使用方式很简单，参见 [Getting started with pandoc](https://pandoc.org/getting-started.html) 或者知乎上的 [pandoc 话题](https://www.zhihu.com/topic/19862254/hot)

祝大家写作愉快 :-)
