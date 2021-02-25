def merge_data_interpolation(df_data, df_new, xdata, ydata, xnew, kind="cubic"):
  """ 
  Merging two data by interpolation 
  
  INPUT:

  df_data: Data source for interpolation 
  df_new: Data where its values are to be interpolated
  xdata: The x column name in df_data. This value MUST exist in BOTH dataframes 
    above. Usually it is the DEPTH. 
  ydata: The y column name in df_data. This value will be the TARGET for interp.
    Must be in LIST, for example: ["TVD"] or ["TVD", "GR", "RHOB"]
  xnew: The x column name in df_new
  
  THEORY:

  f(x1, x2, x3, ..., xi) = y1, y2, y3, ..., yi
  f is the interpolation function. f is applied to a new x value to produce new y
  f(xn) = yn 

  OUTPUT:

  df: It is the df_new, but now contains the newly interpolated y values
  """
  from scipy import interpolate
  import numpy as np
  import pandas as pd

  xd = df_data[xdata].values
  yd = df_data[ydata].values
  xn = df_new[xnew].values

  # Interpolation
  for i in range(len(ydata)):
    yd_ = yd[:,i]
    f = interpolate.interp1d(xd, yd_, kind=kind, fill_value="extrapolate")
    yn = f(xn)

    # Make copy of df_new (to suppress the caveat warning)
    dfnew = df_new.copy()
    dfnew[ydata[i]] = yn # add new column to df_new
  
  dfnew[dfnew[xnew] > max(xd)] = np.nan

  return dfnew
