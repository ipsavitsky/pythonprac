import textdistance as td

def dist(s1: str, s2: str) -> int:
    return td.levenshtein(s1, s2)

s1 = input()
s2 = input()
