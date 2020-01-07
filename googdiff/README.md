
# googdiff: command-line diff tool, a wrapper of Google's diff-match-patch module.

See [the API doc of Google's diff-match-patch
module](https://github.com/google/diff-match-patch).

## Use googdiff when git diff something:

```
git difftool -y --extcmd=googdiff.py
```
