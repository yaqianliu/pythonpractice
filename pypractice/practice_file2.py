# Use words.txt as the file name
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd # pandas
import matplotlib.pyplot as plt # module for plotting
from statsmodels.nonparametric.api import lowess
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import statsmodels.formula.api as smf
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
import sklearn.decomposition
import sklearn.cluster
from matplotlib import gridspec
import seaborn as sns
import datetime

#set default plot characterstics and colors
from matplotlib import rcParams

#dark_colors = [(0.10588235294117647, 0.6196078431372549, 0.4666666666666667),
dark_colors = ["#99D699", "#B2B2B2",
                (0.8509803921568627, 0.37254901960784315, 0.00784313725490196),
                (0.4588235294117647, 0.4392156862745098, 0.7019607843137254),
                (0.9058823529411765, 0.1607843137254902, 0.5411764705882353),
                (0.4, 0.6509803921568628, 0.11764705882352941),
                (0.9019607843137255, 0.6705882352941176, 0.00784313725490196),
                (0.6509803921568628, 0.4627450980392157, 0.11372549019607843),
                (0.4, 0.4, 0.4)]

rcParams['figure.figsize'] = (12, 9)
rcParams['figure.dpi'] = 150
rcParams['axes.color_cycle'] = dark_colors
rcParams['lines.linewidth'] = 2
rcParams['axes.facecolor'] = "white"
rcParams['axes.titlesize'] = 20
rcParams['axes.labelsize'] = 17.5
rcParams['xtick.labelsize'] = 15
rcParams['ytick.labelsize'] = 15
rcParams['legend.fontsize'] = 17.5
rcParams['patch.edgecolor'] = 'none'
rcParams['grid.color']="white"
rcParams['grid.linestyle']="-"
rcParams['grid.linewidth'] = 1
rcParams['grid.alpha']=1
rcParams['text.color'] = "444444"
rcParams['axes.labelcolor'] = "444444"
rcParams['ytick.color'] = "444444"
rcParams['xtick.color'] = "444444"

%matplotlib inline
a = 3
print ('a')
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
