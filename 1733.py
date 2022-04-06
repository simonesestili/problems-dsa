class Solution:
    def minimumTeachings(self, n, langs, ships):
        m, langs = len(langs), list(map(set, langs))

        unable = set()
        for u, v in ships:
            if langs[u-1] & langs[v-1]: continue
            unable.add(u); unable.add(v)

        if not unable: return 0

        counts = defaultdict(int)
        for person in unable:
            for lang in langs[person-1]:
                counts[lang] += 1

        return len(unable) - max(counts.values())
