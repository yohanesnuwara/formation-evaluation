def regrid(df, column_depth, column_feature, depth_regrid):
  """
  Regrid log data to coarsen or to produce blocky log by averaging
  """
  import numpy as np
  import pandas as pd

  # Make endpoints (lower and upper depth)
  endpoint0, endpoint1 = depth_regrid[:-1], depth_regrid[1:]
  midpoint = 0.5 * (depth_regrid[:-1] + depth_regrid[1:])

  x_avg = []
  for i in range(len(endpoint0)):
    # Select dataframe at depths between endpoints
    df_ = df[(df[column_depth]>=endpoint0[i]) & (df[column_depth]<=endpoint1[i])]
    
    # Take average
    x = df_[column_feature].values
    x_avg_ = np.mean(x)
    x_avg.append(x_avg_)
  
  # Make new dataframe
  df_regrid = pd.DataFrame({column_depth+"_regrid": midpoint, column_feature+"_regrid": x_avg})

  return df_regrid
