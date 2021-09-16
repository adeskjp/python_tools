# -*- coding: utf-8 -*-
#
# Copyright 2021
# Created by Haruhiko Kawaguchi
#

""" z_rename.py
    rename file name
"""

import os
import argparse


def main():
    """main
    main function
    Args:
        arg1    : 置換対象文字列
        arg2    : 置換文字列
    Returns:
        None    : None
    """
    parser = argparse.ArgumentParser(description='Twitter image and movie Down Loader')
    parser.add_argument('arg1', type=str, help='Replacement Target')
    parser.add_argument('arg2', type=str, help='Replacement')
    args = parser.parse_args()
    t = args.arg1
    r = args.arg2
    print('Replacement Target : ',t)
    print('Replacement : ',r)
    print('\n')

    file_list = os.listdir('./')
    print(file_list)
    
    os.system('PAUSE')

    for f in file_list:
        aa = f.replace(t, r)
        # ファイル名の変更 
        os.rename(f, aa)

if __name__ == '__main__':
    # print("Start if __name__ == '__main__'")
    main()