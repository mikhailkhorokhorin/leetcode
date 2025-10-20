class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {" ": " "}
        letters = "abcdefghijklmnopqrstuvwxyz"

        i = 0
        for char in key:
            if char not in mapping:
                mapping[char] = letters[i]
                i += 1

        return "".join([mapping[char] for char in message])
