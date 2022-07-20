from dataclasses import dataclass
class Solution:
    def numMatchingSubseq(self, s, words):
        count, buckets = 0, defaultdict(list)
        for w in words: buckets[w[0]].append(Word(w))

        for c in s:
            prev, buckets[c] = buckets[c], []
            for word in prev:
                word.i += 1
                count += word.i == len(word.s)
                if word.i < len(word.s):
                    buckets[word.s[word.i]].append(word)

        return count

@dataclass
class Word:
    s: str
    i: int = 0
