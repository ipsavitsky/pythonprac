import textdistance as td
from multiprocessing import Pool, TimeoutError


def dist(s1: str, s2: str, type_str: str) -> int:
    match type_str:
        case 'L':
            ret = td.levenshtein(s1, s2)
        case 'D':
            ret = td.damerau_levenshtein(s1, s2)
        case _:
            ret = -1
    return ret

s1 = input()
s2 = input()
len_type = input()

pool = Pool(processes=1)
promised_result = pool.apply_async(dist, (s1, s2, len_type))
try:
    res = promised_result.get(timeout=1)
except TimeoutError:
    res = -1

