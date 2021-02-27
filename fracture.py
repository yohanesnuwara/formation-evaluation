def stereonet(strikes, dips):
  """
  Function to Plot Stereonet of Fracture Data (with polar heatmap)
  """
  import numpy as np
  import matplotlib.pyplot as plt
  import mplstereonet 

  # Visualize stereonets (Schmidt projection)
  fig = plt.figure(figsize=(10,10))

  ax = fig.add_subplot(111, projection='stereonet')
  ax.pole(strikes, dips, '.', color="black", markersize=10)
  ax.plane(strikes, dips, '-', color="blue", linewidth=1)
  ax.density_contourf(strikes, dips, measurement='poles', cmap='Reds')
  ax.grid()  

def rose(strikes):
  """
  Function to Plot Rose Diagram of Fracture Data

  NOTE: Source code originally by Bruno Ruas de Pinho
        Website: http://geologyandpython.com/structural_geology.html
        Function is made by author to interface user to that source code
  """
  import numpy as np
  import matplotlib.pyplot as plt
  import mplstereonet

  # calculate the number of strikes every 10 degree
  bin_edges = np.arange(-5, 366, 10)
  number_of_strikes, bin_edges = np.histogram(strikes, bin_edges)

  # Sum the last value with the first value
  number_of_strikes[0] += number_of_strikes[-1]

  # Sum the first half 0-180° with the second half 180-360° to achieve the "mirrored behavior" of Rose Diagrams
  half = np.sum(np.split(number_of_strikes[:-1], 2), 0)
  two_halves = np.concatenate([half, half])

  fig = plt.figure(figsize=(10,10))
  ax = fig.add_subplot(projection='polar')

  ax.bar(np.deg2rad(np.arange(0, 360, 10)), two_halves, 
        width=np.deg2rad(10), bottom=0.0, color='green', edgecolor='k')
  ax.set_theta_zero_location('N')
  ax.set_theta_direction(-1)
  ax.set_thetagrids(np.arange(0, 360, 10), labels=np.arange(0, 360, 10))
  ax.set_rgrids(np.arange(1, two_halves.max() + 1, 2), angle=0, weight= 'black')
  ax.set_title('Rose Diagram', y=1.10, fontsize=15)

  fig.show()  
