class Binner:
    def __init__(self, binwidth, binmax):
        self.binwidth, selfbinmax = binwidth, binmax
        nbins = int(binmax / float(binwidth) + 1)
        self.bins = [0] * nbins

    def add(self, value):
        bin = value / self.binwidth
        self.bins[bin] += 1

binner = Binner(5, 20)
for i in range(0,20):
    binner.add(i)
binner.bins