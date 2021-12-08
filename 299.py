class Solution:
    def getHint(self, secret, guess):
        n = len(guess)
        secret, guess = list(secret), list(guess)
        bulls = cows = 0
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
                secret[i] = guess[i] = ''

        rem = Counter(secret)
        for c in guess:
            if not c: continue
            if rem[c]:
                cows += 1
                rem[c] -= 1

        return f'{bulls}A{cows}B'
