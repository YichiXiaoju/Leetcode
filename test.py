s = "AABABBA"
k = 1

def characterReplacement(s, k):
    count = {}
    left = 0
    max_length = 0
    max_freq = 0

    for right in range(len(s)):
        if s[right] in count:
            count[s[right]] += 1
        else:
            count[s[right]] = 1

        max_freq = max(max_freq, count[s[right]])

        while right - left + 1 - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

result = characterReplacement(s, k)