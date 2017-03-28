def autocorrRMSD(y) : 

    yunbiased = y-np.mean(y)
    ynorm = np.sum(yunbiased**2)
    acor = np.correlate(yunbiased, yunbiased, "same")/ynorm
    # use only second half
    acor = acor[len(acor)/2:]
    # fit exponential
    def func(x, a, c):
        return a*np.exp(-c*x)
        
    popt, pcov = curve_fit(func, np.arange(len(acor)), acor, p0=(1, 10))

    xx = np.linspace(0, len(acor), 1000)
    yy = func(xx, *popt)
    return xx, yy, acor
