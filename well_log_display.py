def well_log_display(df, column_depth, column_list, 
                     column_semilog=None, min_depth=None, max_depth=None, 
                     column_min=None, column_max=None, colors=None, 
                     fm_tops=None, fm_depths=None, 
                     tight_layout=1, title_size=10):
  """
  Display log side-by-side style
  Input:
  df is your dataframe
  specify min_depth and max_depth as the upper and lower depth limit
  column_depth is the column name of your depth
  column_list is the LIST of column names that you will display

  column_semilog is specific for resistivity column; if your resistivities are 
    in column 3, specify as: column_semilog=2. Default is None, so if you don't 
    specify, the resistivity will be plotted in normal axis instead
    
  column_min is list of minimum values for the x-axes.
  column_max is list of maximum values for the x-axes.
  
  colors is the list of colors specified for each log names. Default is None,
    so if don't specify, the colors will be Matplotlib default (blue)
  fm_tops and fm_depths are the list of formation top names and depths.
    Default is None, so no tops are shown. Specify both lists, if you want
    to show the tops
  """
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd
  import random

  if column_semilog==None:
    # column semilog not defined, RT will be plotted in normal axis
    logs = column_list

    # create the subplots; ncols equals the number of logs
    fig, ax = plt.subplots(nrows=1, ncols=len(logs), figsize=(20,10))

    # looping each log to display in the subplots
    if colors==None:
      # color is None (default)
      for i in range(len(logs)):
        # normal axis plot
        ax[i].plot(df[logs[i]], df[column_depth])
        ax[i].set_title(logs[i], size=title_size)
        ax[i].minorticks_on()
        ax[i].grid(which='major', linestyle='-', linewidth='0.5', color='lime')
        ax[i].grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        if column_min!=None and column_max!=None:
          # x-axis limits defined
          ax[i].set_xlim(column_min[i], column_max[i])
        if min_depth!=None and max_depth!=None:
          # y-axis limit defined
          ax[i].set_ylim(min_depth, max_depth)          
        ax[i].invert_yaxis()    

    else:
      # colors are defined (as list)
      for i in range(len(logs)):
        # normal axis plot
        ax[i].plot(df[logs[i]], df[column_depth], color=colors[i])
        ax[i].set_title(logs[i], size=title_size)
        ax[i].minorticks_on()
        ax[i].grid(which='major', linestyle='-', linewidth='0.5', color='lime')
        ax[i].grid(which='minor', linestyle=':', linewidth='0.5', color='black')        
        if column_min!=None and column_max!=None:
          # x-axis limits defined
          ax[i].set_xlim(column_min[i], column_max[i])       
        if min_depth!=None and max_depth!=None:
          # y-axis limit defined
          ax[i].set_ylim(min_depth, max_depth)           
        ax[i].invert_yaxis()    


  else:
    # column semilog is defined, RT will be plotted in semilog axis
    logs = column_list

    # create the subplots; ncols equals the number of logs
    fig, ax = plt.subplots(nrows=1, ncols=len(logs), figsize=(20,10))

    # looping each log to display in the subplots
    if colors==None:
      # color is None (default)
      for i in range(len(logs)):
        if i == column_semilog:
          # for resistivity, semilog plot
          ax[i].semilogx(df[logs[i]], df[column_depth])
        else:
          # for non-resistivity, normal plot
          ax[i].plot(df[logs[i]], df[column_depth])
        
        ax[i].set_title(logs[i], size=title_size)
        ax[i].minorticks_on()
        ax[i].grid(which='major', linestyle='-', linewidth='0.5', color='lime')
        ax[i].grid(which='minor', linestyle=':', linewidth='0.5', color='black')        
        if column_min!=None and column_max!=None:
          # x-axis limits defined
          ax[i].set_xlim(column_min[i], column_max[i])        
        if min_depth!=None and max_depth!=None:
          # y-axis limit defined
          ax[i].set_ylim(min_depth, max_depth)          
        ax[i].invert_yaxis()    

    else:
      # colors are defined (as list)
      for i in range(len(logs)):
        if i == column_semilog:
          # for resistivity, semilog plot
          ax[i].semilogx(df[logs[i]], df[column_depth], color=colors[i])     
        else:
          # for non-resistivity, normal plot
          ax[i].plot(df[logs[i]], df[column_depth], color=colors[i])
        
        ax[i].set_title(logs[i], size=title_size)
        ax[i].minorticks_on()
        ax[i].grid(which='major', linestyle='-', linewidth='0.5', color='lime')
        ax[i].grid(which='minor', linestyle=':', linewidth='0.5', color='black')  
        if column_min!=None and column_max!=None:
          # x-axis limits defined
          ax[i].set_xlim(column_min[i], column_max[i])   
        if min_depth!=None and max_depth!=None:
          # y-axis limit defined
          ax[i].set_ylim(min_depth, max_depth)
        ax[i].invert_yaxis() 

  if fm_tops!=None and fm_depths!=None:
    # Formation tops and depths are specified, they will be shown

    # produce colors
    rgb = []
    for j in range(len(fm_tops)):
      _ = (random.random(), random.random(), random.random())
      rgb.append(_)

    for i in range(len(logs)):
      for j in range(len(fm_tops)):
        # rgb = (random.random(), random.random(), random.random())
        ax[i].axhline(y=fm_depths[j], linestyle=":", c=rgb[j], label=fm_tops[j])  
        # y = fm_depths[j] / (max_depth - min_depth)    
        # ax[i].text(0.5, y, fm_tops[j], fontsize=5, va='center', ha='center', backgroundcolor='w')

  # plt.legend()
  # plt.legend(loc='upper center', bbox_to_anchor=(-3, -0.05),
  #            fancybox=True, shadow=True, ncol=5)  
  
  plt.tight_layout(tight_layout)
  plt.show()  

# def well_log_display(df, column_depth, column_list, 
#                      column_semilog=None, min_depth=None, max_depth=None, 
#                      column_min=None, column_max=None, colors=None, 
#                      fm_tops=None, fm_depths=None, 
#                      tight_layout=1, title_size=10):
#   """
#   Display log side-by-side style

#   Input:

#   df is your dataframe
#   specify min_depth and max_depth as the upper and lower depth limit
#   column_depth is the column name of your depth
#   column_list is the LIST of column names that you will display

#   column_semilog is specific for resistivity column; if your resistivity is
#     in column 3, specify as: column_semilog=2. Default is None, so if 
#     you don't specify, the resistivity will be plotted in normal axis instead
    
#   column_min is list of minimum values for the x-axes.
#   column_max is list of maximum values for the x-axes.
  
#   colors is the list of colors specified for each log names. Default is None,
#     so if don't specify, the colors will be Matplotlib default (blue)

#   fm_tops and fm_depths are the list of formation top names and depths.
#     Default is None, so no tops are shown. Specify both lists, if you want
#     to show the tops
#   """
#   import numpy as np
#   import matplotlib.pyplot as plt
#   import pandas as pd
#   import random

#   if column_semilog==None:
#     # column semilog not defined, RT will be plotted in normal axis
#     logs = column_list

#     # create the subplots; ncols equals the number of logs
#     fig, ax = plt.subplots(nrows=1, ncols=len(logs), figsize=(20,10))

#     # looping each log to display in the subplots
#     if colors==None:
#       # color is None (default)
#       for i in range(len(logs)):
#         # normal axis plot
#         ax[i].plot(df[logs[i]], df[column_depth])
#         ax[i].set_title(logs[i], size=title_size)
#         ax[i].minorticks_on()
#         ax[i].grid(which='major', linestyle='-', linewidth='0.5', color='lime')
#         ax[i].grid(which='minor', linestyle=':', linewidth='0.5', color='black')
#         if column_min!=None and column_max!=None:
#           # x-axis limits defined
#           ax[i].set_xlim(column_min[i], column_max[i])
#         if min_depth!=None and max_depth!=None:
#           # y-axis limit defined
#           ax[i].set_ylim(min_depth, max_depth)          
#         ax[i].invert_yaxis()    

#     else:
#       # colors are defined (as list)
#       for i in range(len(logs)):
#         # normal axis plot
#         ax[i].plot(df[logs[i]], df[column_depth], color=colors[i])
#         ax[i].set_title(logs[i], size=title_size)
#         ax[i].minorticks_on()
#         ax[i].grid(which='major', linestyle='-', linewidth='0.5', color='lime')
#         ax[i].grid(which='minor', linestyle=':', linewidth='0.5', color='black')        
#         if column_min!=None and column_max!=None:
#           # x-axis limits defined
#           ax[i].set_xlim(column_min[i], column_max[i])       
#         if min_depth!=None and max_depth!=None:
#           # y-axis limit defined
#           ax[i].set_ylim(min_depth, max_depth)           
#         ax[i].invert_yaxis()    


#   else:
#     # column semilog is defined, RT will be plotted in semilog axis
#     logs = column_list

#     # create the subplots; ncols equals the number of logs
#     fig, ax = plt.subplots(nrows=1, ncols=len(logs), figsize=(20,10))

#     # looping each log to display in the subplots
#     if colors==None:
#       # color is None (default)
#       for i in range(len(logs)):
#         if i == 3:
#           # for resistivity, semilog plot
#           ax[i].semilogx(df[logs[i]], df[column_depth])
#         else:
#           # for non-resistivity, normal plot
#           ax[i].plot(df[logs[i]], df[column_depth])
        
#         ax[i].set_title(logs[i], size=title_size)
#         ax[i].minorticks_on()
#         ax[i].grid(which='major', linestyle='-', linewidth='0.5', color='lime')
#         ax[i].grid(which='minor', linestyle=':', linewidth='0.5', color='black')        
#         if column_min!=None and column_max!=None:
#           # x-axis limits defined
#           ax[i].set_xlim(column_min[i], column_max[i])        
#         if min_depth!=None and max_depth!=None:
#           # y-axis limit defined
#           ax[i].set_ylim(min_depth, max_depth)          
#         ax[i].invert_yaxis()    

#     else:
#       # colors are defined (as list)
#       for i in range(len(logs)):
#         if i == 3:
#           # for resistivity, semilog plot
#           ax[i].semilogx(df[logs[i]], df[column_depth], color=colors[i])     
#         else:
#           # for non-resistivity, normal plot
#           ax[i].plot(df[logs[i]], df[column_depth], color=colors[i])
        
#         ax[i].set_title(logs[i], size=title_size)
#         ax[i].minorticks_on()
#         ax[i].grid(which='major', linestyle='-', linewidth='0.5', color='lime')
#         ax[i].grid(which='minor', linestyle=':', linewidth='0.5', color='black')  
#         if column_min!=None and column_max!=None:
#           # x-axis limits defined
#           ax[i].set_xlim(column_min[i], column_max[i])   
#         if min_depth!=None and max_depth!=None:
#           # y-axis limit defined
#           ax[i].set_ylim(min_depth, max_depth)
#         ax[i].invert_yaxis() 

#   if fm_tops!=None and fm_depths!=None:
#     # Formation tops and depths are specified, they will be shown

#     # produce colors
#     rgb = []
#     for j in range(len(fm_tops)):
#       _ = (random.random(), random.random(), random.random())
#       rgb.append(_)

#     for i in range(len(logs)):
#       for j in range(len(fm_tops)):
#         # rgb = (random.random(), random.random(), random.random())
#         ax[i].axhline(y=fm_depths[j], linestyle=":", c=rgb[j], label=fm_tops[j])  
#         # y = fm_depths[j] / (max_depth - min_depth)    
#         # ax[i].text(0.5, y, fm_tops[j], fontsize=5, va='center', ha='center', backgroundcolor='w')

#   # plt.legend()
#   # plt.legend(loc='upper center', bbox_to_anchor=(-3, -0.05),
#   #            fancybox=True, shadow=True, ncol=5)  
  
#   plt.tight_layout(tight_layout)
#   plt.show()  
