__author__ = 'wallisj'

def wavelet_load(wavelet_path):
    openfile = open(wavelet_path, 'r')
    readfile = openfile.read()
    alllines = readfile.strip().split("\n")

    class columns:
        def __init__(self, t, a):
            self.t = t
            self.a = a

    data = []

    for row in alllines:
            array = row.strip().split('\t')
            data.append(columns(array[0], array[1]))

    t = ([thing.t for thing in data])
    a = ([thing.a for thing in data])

    #wavelet = zip(t,a)

    return t,a



