import os

ROOT = os.path.dirname(os.path.abspath(__file__))
tempStorage = os.path.join(ROOT, "tempStorage")

"""<------------Directory Absolute Paths------------------------------>"""
RootDir = os.path.dirname(os.path.abspath(__file__))
InputDir = os.path.join(RootDir, "dataset")

"""<-------Raw Text files--------->"""
raw_text_files = os.path.join(InputDir, "raw_text/raw_text.txt")

"""<-------Stop Words files--------->"""
stop_words = os.path.join(InputDir, "stopwords/stopwords.txt")
