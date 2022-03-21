from sys import argv
from textdistance import damerau_levenshtein
import difflib
import ast

def create_pill(node, depth = 0):
    'recursively creates a pill that contains every node first letter and `depth` of a node'
    resulting_pill = ''
    resulting_pill += type(node).__name__[0] + str(depth) + '.'*len(node._fields)
    # print(f'visiting node {type(node).__name__} at depth {depth} with attributes {node._fields}')
    for child in ast.iter_child_nodes(node):
        resulting_pill += create_pill(child, depth + 1)
    return resulting_pill


txt1 = open(argv[1], 'r').read()
txt2 = open(argv[2], 'r').read()
pill1 = create_pill(ast.parse(txt1))
pill2 = create_pill(ast.parse(txt1))
if damerau_levenshtein.normalized_distance(pill1, pill2) <= 0.1:
    print('possible plagiarism')
    diff = difflib.HtmlDiff(tabsize=8, wrapcolumn=None, linejunk=None)
    stripped_text1 = ast.unparse(ast.parse(txt1))
    stripped_text2 = ast.unparse(ast.parse(txt2))
    diff_html = diff.make_file(stripped_text1.split('\n'), stripped_text2.split('\n'), argv[1], argv[2])
    with open('plagiarism.html', 'w') as html:
        html.write(diff_html)
    

