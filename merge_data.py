def merge_data_interpolation(df_data, df_new, xdata, ydata, xnew, kind="cubic"):
  """ 
  Merging two data by interpolation 
  
  INPUT:

  df_data: Data source for interpolation 
  df_new: Data where its values are to be interpolated
  xdata: The x column name in df_data. This value MUST exist in BOTH dataframes 
    above. Usually it is the DEPTH. 
  ydata: The y column name in df_data. This value will be the TARGET for interp.
    Could be more than one (LIST)
  xnew: The x column name in df_new
  
  THEORY:

  f(x1, x2, x3, ..., xi) = y1, y2, y3, ..., yi
  f is the interpolation function. f is applied to a new x value to produce new y
  f(xn) = yn 

  OUTPUT:

  df: It is the df_new, but now contains the newly interpolated y values
  """
  import scipy
  
  xd = df_data[xdata].values
  yd = df_data[ydata].values
  xn = df_new[xnew].values

  # Interpolation
  for i in range(len(ydata)):
    yd_ = yd[:,i]
    f = scipy.interpolate.interp1d(xd, yd_, kind=kind, fill_value="extrapolate")
    yn = f(xn)
    # yn = np.interp(xn, xd, yd_)
    df_new[ydata[i]] = yn # add new column to df_new
  
  df_new[df_new[xnew] > max(xd)] = np.nan

  return df_new
