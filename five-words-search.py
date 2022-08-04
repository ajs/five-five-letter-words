import dataclasses
import sys
import random
import time
from typing import List, Set


def valid_word(word):
    """Strip out words that aren't 5-char lower case, etc."""

    word = word.strip()
    if len(word) != 5:
        return False
    if not (word.isalpha() and word.islower()):
        return False
    if len(set(word)) != 5:
        return False
    if not set(word) & set("aeiouy"):
        return False
    return True


def unique_letter_words(words):
    """Strip out words that are anagrams of others"""

    letter_key = set()
    for word in words:
        letters = "".join(sorted(set(word)))
        if letters not in letter_key:
            letter_key.add(letters)
            yield word


@dataclasses.dataclass
class FinderContext:
    maxlen: int = 0  # Longest solution so far
    solutions: List[List[str]] = dataclasses.field(default_factory=lambda: [])  # Actual solutions
    letter_set_tracker: Set[str] = dataclasses.field(default_factory=lambda: set())  # Partial solution letters seen


def finder(result, words, setlist, context: FinderContext, pos=0, resultset=None):
    """Take a current result and a word list, starting from pos and find new endings"""

    if not resultset:
        resultset = set()
    i = pos
    wordlist_len = len(words)
    first_word = not resultset

    while i < wordlist_len:
        word = words[i]
        next_i = i + 1
        if first_word or resultset.isdisjoint(word):
            # if first_word:
            #    print(f" Working: {word}...")
            new_result = result + [word]
            solution_len = len(result) + 1
            if solution_len >= context.maxlen:
                if solution_len > context.maxlen:
                    context.maxlen = len(result) + 1
                    context.solutions = []
                context.solutions.append(new_result)
                if len(result) >= 4:
                    print(", ".join(new_result))
            if wordlist_len > next_i:
                next_set = resultset | setlist[word]
                next_set_letters = "".join(sorted(next_set))
                if next_set_letters not in context.letter_set_tracker:
                    context.letter_set_tracker.add(next_set_letters)
                    finder(new_result, words, setlist, context, next_i, resultset | setlist[word])
        i = next_i


wordfile = sys.argv[1]
with open(wordfile, "r") as wordfile_fh:
    words = (word.strip() for word in (w for w in wordfile_fh.readlines()) if valid_word(word))

words = list(unique_letter_words(words))
setlist = {word: set(word) for word in words}
# random.shuffle(words)

print(f"{len(words)} words...")

context = FinderContext()

start_time = time.time()
finder([], words, setlist, context)
end_time = time.time()

time_lapsed = end_time - start_time
if time_lapsed >= 60:
    time_lapsed = f"{time_lapsed // 60}min {time_lapsed % 60}sec"
else:
    time_lapsed = f"{time_lapsed}sec"

print(f"Final results: {len(context.solutions)} solutions in {time_lapsed}")
