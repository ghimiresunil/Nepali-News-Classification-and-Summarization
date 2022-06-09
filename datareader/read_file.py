import time
import sys
import string

sys.path.append('./')

import config as cfg

def read_file(file_path):
    start = time.process_time()
    print("Reading the file .......")
    f = open(file_path, encoding="utf-8", buffering=10000)
    lines = f.read().strip().split()
    return lines

print(read_file(cfg.stop_words))