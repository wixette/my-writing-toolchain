# Markdown 格式里中文软换行的处理问题

许多 Markdown 格式解析器、转换器无法处理分行的中文段落，因为它们会在连
接每一行时缺省将 line break 替换成一个空格。

如果前一行结尾和后一行开头都是 CJK 的全角字符，那么连接每一行时插入的
空格就是多余的。

但彻底忽略掉 line breaks 也是不合适的。如果前一行结尾或后一行开头是
English phrases 或其他半角字符，那么增加一个空格在大多数时候是必须的。

[pandoc](https://github.com/jgm/pandoc) 包含了一个名为
`east_asian_line_breaks` 的扩展来处理 CJK 与其他语言混合时出现的这个问题。
参见 [jdm's
commit](https://github.com/jgm/pandoc/commit/44120ea7165546152af88fd442c52ab0f201052e)

可以使用：

    pandoc -f markdown_strict+east_asian_line_breaks input.md -o outpu.html

来开启这个开关。
