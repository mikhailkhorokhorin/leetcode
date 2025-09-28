class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "4").replace("IX", "9").replace("XL", "*").replace("XC", "&").replace("CD", "?").replace(
                "CM", "!")
        return s.count("4") * 4 + s.count("9") * 9 + s.count("*") * 40 + s.count("&") * 90 + s.count(
                "?") * 400 + s.count("!") * 900 + s.count("I") + s.count("V") * 5 + s.count("X") * 10 + s.count(
                "L") * 50 + s.count("C") * 100 + s.count("D") * 500 + s.count("M") * 1000
