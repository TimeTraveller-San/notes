# Argument list too long
- For a kaggle competition, I downloaded and extracted some data.
- I wanted to remove that data (some of it, png files only)
- I did the usual stuff: `rm train_128/*png`
- I didn't get the usual result
- I got this: `bash: /usr/bin/rm: Argument list too long`
- Naturally, I googled the issue

Turns out, there's a size limitation to the number of command line arguments I can pass.
Thank you stackoverflow for the [solution](https://stackoverflow.com/questions/11289551/argument-list-too-long-error-for-rm-cp-mv-commands)

# Fix
here's what I did:

```
for f in train_128/*png; do rm "$f"; done
```

This was slow, very slow.

The files are gone though, next time I am trying:

```
find . -maxdepth 1 -name 'train_128/*png' -delete
``
