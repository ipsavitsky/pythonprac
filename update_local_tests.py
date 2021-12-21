import os
from glob import glob


for dir in glob(os.path.join('./', "*", "")):
    os.chdir(dir)
    for inner_dir in glob(os.path.join('./', "*", "")):
        os.chdir(f'{inner_dir}')
        for input_file in glob("./tests/*.in"):
            print(f'executing python3 prog.py < {input_file} > {input_file[:-3]}.out at {os.getcwd()}')
            os.system(f'python3 prog.py < {input_file} > {input_file[:-3]}.out')
        os.chdir('../')
    os.chdir('../')