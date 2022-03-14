from sys import argv
import ast

class RemoveNames(ast.NodeVisitor):
    def visit(self, node):
        print(f'visiting node {node}')

file1 = open(argv[1], 'r').read()
# file2 = open(argv[2], 'r').read()
file1 = ast.unparse(ast.parse(file1))
# file2 = ast.unparse(ast.parse(file2))

ast1 = ast.dump(ast.parse(file1), indent=4)
# ast2 = ast.dump(ast.parse(file2), indent=4)
RemoveNames().visit(ast1)

# print(ast2)
