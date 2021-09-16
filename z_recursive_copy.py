import os
import shutil
from datetime import datetime

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

def file_move():
    target_path = r"H:\finished"
    files = os.listdir(target_path)
    files_dir = [f for f in files if os.path.isdir(os.path.join(target_path, f))]
    # print(files_dir)

    for cd in files_dir:
        for f in find_all_files(cd):
            if os.path.isfile(f):
                #('/path/to/script', '.py')
                #path, ext = os.path.splitext(f)
                # ('script', '.py')
                path, ext = os.path.splitext(os.path.basename(f))
                target_name = target_path + "\\" + path + ext
                # コピー場所に同じ名前のファイルが存在したら名前を変更して移動
                f_name = f
                if os.path.exists(target_name):
                    path, ext = os.path.splitext(f)
                    now = datetime.now()
                    now_ts = now.timestamp()
                    f_name = path + "_" + str(now_ts) + ext
                    os.rename(f, f_name)
                print("Move Source file {}".format(f_name))
                shutil.move(f_name, target_path)

if __name__ == '__main__':
    file_move()