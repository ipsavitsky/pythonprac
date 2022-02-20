from dataclasses import dataclass, field
import zlib
from glob import iglob
from os.path import basename, dirname

SHIFT = "  "


@dataclass
class BranchInfo:
    last_commit: str

@dataclass
class CommitInfo():
    tree: str
    parent: str
    text: str


@dataclass
class TreeInfo():
    refs: list[tuple[str, str]] = field(default_factory=list)


commits = dict()
trees = dict()

for store in iglob("../../.git/objects/??/*"):
    Id = basename(dirname(store)) + basename(store)

    with open(store, "rb") as f:
        obj = zlib.decompress(f.read())
        header, _, body = obj.partition(b'\x00')
        kind, size = header.split()

    if kind == b'tree':
        tail = body
        tree_info = TreeInfo()
        while tail:
            treeobj, _, tail = tail.partition(b'\x00')
            tmode, tname = treeobj.split()
            num, tail = tail[:20], tail[20:]
            tree_info.refs.append((tname.decode(), num.hex()))
        trees[Id] = tree_info
    elif kind == b'commit':
        out = body.decode().split()
        commits[Id] = CommitInfo(out[1], out[3], ' '.join(out[4:]))

branches = dict()

for head in iglob('../../.git/refs/heads/*'):
    with open(head, 'r') as f:
        branches[basename(head)] = BranchInfo(f.read().strip())

def walk_tree(subtree: str, layer: int) -> None:
    layer += 1
    tree_info = trees[subtree]
    for ref in tree_info.refs:
        print('  ' * layer + ref[0])
        if ref[1] in trees:
            walk_tree(ref[1], layer)
        

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 1:
        for branch in branches.keys():
            print(branch)
    elif len(argv) == 2:
        branch_name = argv[-1]
        commit_hash = branches[branch_name].last_commit
        commit_info = commits[commit_hash]
        walk_tree(commit_info.tree, 0)
