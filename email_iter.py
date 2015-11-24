import os

class email_iter:
    #mail_dir is the path to the mail text files
    def __init__(self, mail_dir):
        self.i         = 0
        self.mail_dir  = mail_dir
        self.filenames = []
        self.dirpath   = ""
        for dirpath, dirnames, filenames in os.walk(self.mail_dir):
            self.dirpath   = dirpath + ("" if dirpath[-1] == "/" else "/")
            self.filenames = filenames

    def __iter__(self):
        return self

    def next(self):
        if self.i < len(self.filenames):
            self.i += 1
            filepath  = self.dirpath + self.filenames[self.i-1]
            f         = open(filepath, 'r')
            file_text = f.read()
            f.close()
            return file_text
        else:
            raise StopIteration()
