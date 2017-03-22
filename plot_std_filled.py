def plot_std_filled(data, std, data_color='cyan', std_color='blue', std_alpha=1.0) :
  fig = plt.figure()
  ax=fig.gca()
  data_minus_std = data - std 
  data_plus_std  =  data + std 
  ax.fill_between(range(len(data)), data_minus_std, data_plus_std, color=std_color, alpha=std_alpha)
  ax.plot(data)
