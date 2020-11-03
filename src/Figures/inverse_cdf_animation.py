import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm

class InverseCDFSampler:
    
    def __init__(self,pdf,cdf,xlim,epsilon=0.05):
        self.pdf = pdf
        self.cdf = cdf
        self.xlim = xlim
        self.cur_sample = None
        
    def advance_sample(self):
        if self.cur_sample is None:
            x,y = self.xlim[0],np.random.rand()
            self.cur_sample = (self.xlim[0],np.random.rand())
            self.sample_direction = "horizontal"
        else:
            if self.sample_direction == "horizontal":
                x = self.cur_sample[0] + self.epsilon
                if self.cdf(x) <= self.cur_sample[1]:
                    self.cur_sample = (self.pdf(self.cur_sample[1]),self.cur_sample[1])
                    self.sample_direction = "vertical"
                else:
                    self.cur_sample = (x,self.cur_sample[1])
            elif self.sample_direction == "vertical":
                y = self.cur_sample[1] - self.epsilon
                if y <= 0:
                    self.cur_sample = (self.cur_sample[0],0)
                    
                else:
                    self.cur_sample = (self.cur_sample[0],y)
                    
        return self.cur_sample
    
def pdf(x):
    return x
    
def cdf(y):
    return y

smplr = InverseCDFSampler(pdf,cdf,[0,1])
fig = plt.figure()
ax = plt.axes(xlim=smplr.xlim,ylim=[-.1,1.1])
ax.plot(np.linspace(smplr.xlim[0],smplr.xlim[1],0.05))
sample, = ax.plot([],[])
        
def init():
    global smplr,sample
    sample.set_data([],[])
    return sample
    
def animate(i)
    
        