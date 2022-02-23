#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
import re
import sys
from ipsedixit import Generator


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('not enough arguments')
    elif len(sys.argv) == 3:
        match sys.argv[2]:
            case 'caesar' | 'tacitus':
                gen = Generator(sys.argv[2])
            case file_name:
                with open(file_name, 'r') as ifile:
                    text = ifile.read()
                gen = Generator(text)
        print('\n\n'.join(gen.paragraphs(int(sys.argv[1]))))
    # sys.argv[1]
    # sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    # sys.exit(cli())
