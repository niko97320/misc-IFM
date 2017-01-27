def runningMeanFast(x, N=500): # where x is the aray of data and N the bin width

    x1 = np.pad(x,N,mode='reflect')
    output =np.convolve(x1, np.ones((N,))/N)[(N-1):]
    return output[N:-N]
