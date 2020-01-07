#!/usr/bin/env python3
"""Command-line diff tool, an wrapper of Google's diff-match-patch module.
"""

import argparse
import tempfile
import webbrowser

from diff_match_patch import diff_match_patch


DIFF_HTML_TMP = '''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
body{font-family:"Lucida Console",Monaco,"Courier New",Courier, monospace;
font-size:14px;padding:20px;}
h1{font-size:14px;border-bottom:#ccc solid 1px;margin-bottom:20px;}
pre{font-family:"Lucida Console",Monaco,"Courier New",Courier, monospace;
font-size:14px;line-height:22px;}
</style>
</head>
<body>
<h1>diff between "%(file1)s" and "%(file2)s"</h2>
<pre>%(text)s</pre>
</body>
</html>
'''


def main():
    parser = argparse.ArgumentParser(
        description='diff tool using Google\'s diff-match-patch')
    parser.add_argument('files', metavar='FILE', type=str, nargs=2)
    parser.add_argument('--timeout', type=float, default=0)
    parser.add_argument('--view_in_browser', type=bool, default=True)
    args = parser.parse_args()
    path1, path2 = args.files

    googdiff = diff_match_patch()
    googdiff.Diff_Timeout = args.timeout
    text1 = open(path1).read()
    text2 = open(path2).read()
    diff = googdiff.diff_main(text1, text2, False)
    googdiff.diff_cleanupSemantic(diff)

    diff_html_span = googdiff.diff_prettyHtml(diff)

    diff_out = DIFF_HTML_TMP % dict(text=diff_html_span,
                               file1=path1,
                               file2=path2)
    if args.view_in_browser:
        with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as temp_file:
            temp_file.write(diff_out)
        webbrowser.open('file://%s' % temp_file.name)
    else:
        print(diff_out)


if __name__ == '__main__':
    main()
