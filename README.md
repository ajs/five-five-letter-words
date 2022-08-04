# Solution to Matt Parker's twenty-five unique letters

In [this video](https://youtu.be/_-AfhLQfb6w), Matt Parker of Stand-up Maths posed an interesting
problem: given a word list, compute the list of 5-word groups that consist
of 5-letter words and repeat no letters.

This script finds a solution on my machine in 6 minutes.

However, there is a difference between Matt's solution and mine.

He trims out anagram words (e.g. meat and team) but I trim out
anagram *solutions*, even *parts of solutions*!

There are arguments either way as to whether or not
this is the desired result, but I thought it was interesting,
and optimizing for time, it's a real win.

## Usage

```commandline
python3 five-words-search.py words.txt
```

The `words.txt` file is obtained from Matt's suggestion location:
[english-words](https://github.com/dwyl/english-words).

Sample output:

```
python3.8 five-words-search.py words.txt
5334 words...
chimb, expwy, fjord, klutz, vangs
chivw, expdt, furzy, jambs, klong
chivw, expdt, jumby, klong, zarfs
chivw, fjord, glaky, muntz, pbxes
dwarf, glyph, jocks, muntz, vibex
expdt, furzy, gconv, jambs, whilk
fjord, gucks, nymph, vibex, waltz
Final results: 7 solutions in 6.0min 6.410505771636963sec
```
