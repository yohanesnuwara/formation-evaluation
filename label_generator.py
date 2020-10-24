def label_generator(df_well, df_tops, column_depth, label_name):
  """
  Generate Formation (or other) Labels to Well Dataframe
  (useful for machine learning and EDA purpose)

  Input:

  df_well is your well dataframe (that originally doesn't have the intended label)
  df_tops is your label dataframe (this dataframe should ONLY have 2 columns)
    1st column is the label name (e.g. formation top names)
    2nd column is the depth of each label name

  column_depth is the name of depth column on your df_well dataframe
  label_name is the name of label that you want to produce (e.g. FM. LABEL)

  Output:

  df_well is your dataframe that now has the labels (e.g. FM. LABEL)
  """
  import numpy as np
  import pandas as pd

  # generate list of formation depths and top names
  fm_tops = df_tops.iloc[:,0]  
  fm_depths = df_tops.iloc[:,1] 

  # create FM. LABEL column to well dataframe
  # initiate with NaNs
  df_well[label_name] = np.full(len(df_well), np.nan)  

  indexes = []
  topnames = []
  for j in range(len(fm_depths)):
    # search index at which the DEPTH in the well df equals to OR
    # larger than the DEPTH of each pick in the pick df
    if (df_well[column_depth].iloc[-1] > fm_depths[j]):
      index = df_well.index[(df_well[column_depth] >= fm_depths[j])][0]
      top = fm_tops[j]
      indexes.append(index)
      topnames.append(top)

  # replace the NaN in the LABEL column of well df
  # at the assigned TOP NAME indexes
  df_well[label_name].loc[indexes] = topnames

  # Finally, using pandas "ffill" to fill all the rows 
  # with the TOP NAMES
  df_well = df_well.fillna(method='ffill')  

  return df_well 
