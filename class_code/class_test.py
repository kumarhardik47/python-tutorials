class Sample(object):
    '''This class defines various methods related to the sample'''
    a = 0

    def drawSample(samplesize,List):
        sample=random.sample(List,samplesize)
        return sample

Choices=range(100)
print Sample.drawSample(5,Choices)

print hasattr(Sample,a)
