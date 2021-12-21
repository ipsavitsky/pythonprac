import os
from glob import glob
from random import sample

with open("repo_urls", 'r') as f:
    urls = f.readlines()

for dir in glob(os.path.join('./', "*", "")):
    os.chdir(dir)
    for inner_dir in glob(os.path.join('./', "*", "")):
        os.chdir(inner_dir)
        test_repos = sample(urls, 3)
        with open('URLS', 'w') as f:
            for repo in test_repos:
                f.write(repo[:-1] + '/tree/main' + dir[1:-1] + inner_dir[1:] + 'tests\n')
        os.chdir('../')
    os.chdir('../')