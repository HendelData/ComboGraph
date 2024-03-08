import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# READ IN DATA
creditscores = pd.read_csv('creditscores.csv')

# SET CUSTOM PARAMETERS TO CHANGE AXIS COLOR AND SIZE AND COLOR OF TICK MARKS
custom_params = {'axes.edgecolor': 'gainsboro',
                 'xtick.color': 'gainsboro', 'xtick.major.size': '2',
                 'ytick.color': 'gainsboro', 'ytick.major.size': '2'}
sns.set_theme(style="ticks", rc=custom_params)

# CREATE A JOINTPLOT OF THE DATA
sns.jointplot(data=creditscores, x='Eq', y='Exp', s=0.75,
              marginal_kws={'color': 'maroon', 'ec': 'maroon'},
              joint_kws={'color': 'darkblue'})

# AXIS LABELS
plt.ylabel("EXPERIAN \nSCORE", rotation=0, y=1, fontsize=7, color='gray')
plt.xlabel("EQUIFAX \nSCORE", rotation=0, x=1, fontsize=7, color='gray')
plt.yticks(fontsize=7, color='gray')
plt.xticks(fontsize=7, color='gray')
plt.tick_params(color='gainsboro')

plt.show()
