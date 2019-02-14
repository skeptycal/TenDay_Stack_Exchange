

import pandas

df = pandas.read_csv('hrdata.csv')
print(df)

inputfile = "/Volumes/Data/skeptycal/Documents/current/_data_science/_stack_exchange/categories.csv"
cats = []

df = pandas.read_csv('hrdata.csv')
print(df)
   


# As supplementary, if you are reading a vvvvery large file, and you don't want read all of the content into memory at once, you might consider using a buffer, then return each word by yield:

'''
def read_words(inputfile):
    with open(inputfile, 'r') as f:
        while True:
            buf = f.read(10240)
            if not buf:
                break

            # make sure we end on a space (word boundary)
            while not str.isspace(buf[-1]):
                ch = f.read(1)
                if not ch:
                    break
                buf += ch

            words = buf.split()
            for word in words:
                yield word
        yield '' #handle the scene that the file is empty

if __name__ == "__main__":
    for word in read_words('./very_large_file.txt'):
        process(word)
'''
