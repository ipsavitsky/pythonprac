import os
from glob import glob
import subprocess

all_needed_test_execution_lines = list()

for dir in glob(os.path.join('./', "*", "")):
    os.chdir(dir)
    for inner_dir in glob(os.path.join('./', "*", "")):
        os.chdir(inner_dir)
        print(f'executing local tests in {dir[:-1]}{inner_dir[1:]}')
        all_needed_test_execution_lines.append(f'python3 checkerNN.py {dir[:-1]}{inner_dir[1:]}')
        # os.system(f'python3 checkerNN.py {dir[1:-1]}{inner_dir[1:]}')
        with open('URLS', 'r') as f:
            for repo in f:
                print(f'executing {repo[:-1]} on {dir[:-1]}{inner_dir[1:]}')
                all_needed_test_execution_lines.append(f'python3 checkerNN.py {dir[:-1]}{inner_dir[1:]} {repo[:-1]}')
                # os.system(f'python3 checkerNN.py {dir[1:-1]}{inner_dir[1:]} {repo[:-1]}')
        os.chdir('../')
    os.chdir('../')

for line in all_needed_test_execution_lines:
    print('#'*80)
    print(line)
    try:
        result = subprocess.check_output(line, shell=True ,stderr=subprocess.STDOUT)
    except:
        print('an error occured\n')
    else:
        print(result.decode())