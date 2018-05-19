# -*- coding: cp1252 -*-
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
col_names = ["user_id", "item_id", "rating", "timestamp"]
data = pd.read_table('u.data', names=col_names)
data = data.drop('timestamp', 1)
data.info()
plt.hist(data['rating'])
plt.show()
Number_Ratings = len(data)
Number_Movies = len(np.unique(data['item_id']))
Number_Users = len(np.unique(data['user_id']))
