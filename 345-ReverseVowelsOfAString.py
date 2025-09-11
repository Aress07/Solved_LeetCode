class Solution:
    def reverseVowels(self, s: str) -> str:
        voyelles = 'aeiouAEIOU'
        k, j = 0, len(s) - 1
        s_t = list(s)
        length = len(s_t)

        while k < j:
            if s_t[k] in voyelles:
                if s_t[j] in voyelles:
                    s_t[k], s_t[j] = s_t[j], s_t[k]
                    k += 1
                j -= 1
            else:
                k += 1

        return "".join(s_t)
