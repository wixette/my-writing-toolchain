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

## 编辑器

任何一个用着顺手，能编辑纯文本的编辑器都可以胜任 Markdown 格式的写作。Windows、MacOS、Linux 等操作系统上的记事本，网页里的编辑框，各种在线文档类的笔记工具、写作平台、微信小程序，手机上的记事本，都能圆满完成写作工作。当然，对程序员来说最理想的还是那些平常用来写程序的工具软件。

传统程序员有两大“宗教”——VIM 和 Emacs。我是 Emacs 党，但从不说 VIM 的坏话。所以，用 VIM 写作还是用 Emacs 写作，完全看心情。最近我还比较喜欢超轻量级的 nano，做些短平快的事情特别合适。Windows 上的 Notepad++ 也很棒。其他诸如 VS Code、Eclipse、Xcode 之类，都显得略重了些，不过也足以胜任写作任务。

各种代码编辑器都能针对 Markdown 中的不同类型内容，用不同颜色或字体显示。我在 Emacs 里会缺省安装并打开 [markdown-mode](https://jblevins.org/projects/markdown-mode/)。

其他还有一些小技巧，比如我在 Emacs 里会为中文写作的 Markdown 文本或其他纯文本设置较大的字号，而为 C++、JavaScript、Python 等代码编辑设置较小的字号，两者之间相差两到三档。这大概是因为写作文字时更希望关注某些聚焦的内容，而写代码时更希望一眼看到更多的信息量吧。

我在 Emacs 里做的与中文写作有关的设置，可以参见我的 [Emacs 启动文件](https://github.com/wixette/my-writing-toolchain/blob/master/emacs/my-emacs-init-file.el)。

## Git 版本管理

## Diff 版本比较

## 中文 Markdown 的换行问题

markdown-cjk

pandoc east asian extension

## 发布

pandoc

办公软件


