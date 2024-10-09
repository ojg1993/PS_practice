class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)

        if length < 2:
            return length

        i = j = 0

        while i < length:
            cnt = 1
            while i+1 < length and chars[i] == chars[i+1]:
                cnt += 1
                i += 1
            chars[j] = chars[i]
            j += 1
            if cnt > 1:
                for val in str(cnt):
                    chars[j] = val
                    j += 1
            i += 1
        return j
