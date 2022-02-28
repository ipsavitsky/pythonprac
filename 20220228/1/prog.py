import textdistance as td

def dist(s1: str, s2: str, type_str: str) -> int:
    match type_str:
        case 'L':
            return td.levenshtein(s1, s2)
        case 'D':
            return td.damerau_levenshtein(s1, s2)
        case _:
            return -1

s1 = input()
s2 = input()
len_type = input()


res = dist(s1, s2, len_type)

