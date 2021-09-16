# -*- coding: utf-8 -*-
#
# Copyright 2021
# Created by Haruhiko Kawaguchi
#

""" z_delname.py
    delete file name
"""

import os
import argparse


def main():
    """main
    main function
    Args:
        arg1    : 削除対象文字列
    Returns:
        None    : None
    """
    parser = argparse.ArgumentParser(description='Twitter image and movie Down Loader')
    parser.add_argument('arg1', type=str, help='Replacement Target')
    args = parser.parse_args()
    t = args.arg1

    print('Delete Target : ',t)
    print('\n')

    file_list = os.listdir('./')
    print(file_list)
    
    os.system('PAUSE')

    for f in file_list:
        aa = f.replace(t, '')
        # ファイル名の変更 
        os.rename(f, aa)

if __name__ == '__main__':
    # print("Start if __name__ == '__main__'")
    main()