import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importing the data using the read_csv method
df = pd.read_csv("medical_examination.csv")

# 2. Adding overweight column
df['overweight'] = np.where((df['weight'] / np.square(df['height']/100))> 25, 1,0)

# 3. Normalize the data so that 0 always represents a good condition and 1 always represents a bad condition. For the 'cholesterol' and 'gluc' values: if the value is 1, change it to 0; if the value is greater than 1, change it to 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0 , 1)
df['gluc'] = np.where(df['gluc'] == 1, 0 , 1)

# 4. Drawing the categorical plot
def draw_cat_plot():
    # 5. Create a DataFrame for a categorical plot using `pd.melt`, incorporating only the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=['active', 'alco', "cholesterol" , 'gluc', 'overweight', 'smoke'])


    # 6. Grouping and reformating the data to split it by 'cardio'. Show the counts of each feature.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7. Drawing the catplot with 'sns.catplot()'
    plot = sns.catplot(x= "variable", y = "total", kind ="bar" ,hue = "value", data = df_cat, col= "cardio")
    plot.set_axis_labels("variable", "total")


    # 8. Getting the figure for the output
    fig = plot.fig


    # 9. Returning the figure
    fig.savefig('catplot.png')
    return fig


# 10. Drawing the Heat Map
def draw_heat_map():
    # 11. Cleaning the data
    df_heat = df[
         (df['ap_lo'] <= df['ap_hi']) & 
         (df['height'] >= df['height'].quantile(0.025)) & 
         (df['height'] <= df['height'].quantile(0.975)) &
         (df['weight'] >= df['weight'].quantile(0.025)) & 
         (df['weight'] <= df['weight'].quantile(0.975))]

    # 12. Calculating the correlation matrix
    corr = df_heat.corr()

    # 13. Generating a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype= bool))



    # 14. Setting up the matplotlib figure
    fig, ax = plt.subplots(figsize = (12,12))

    # 15. Drawing the Heat Map with the help of 'sns.heatmap()'
    sns.heatmap(corr, vmin=0, vmax= 0.25, fmt='.1f', linewidth = 1, annot = True, square = True, mask=mask, cbar_kws = {'shrink':.82})

    # 16. Returning the figure
    fig.savefig('heatmap.png')
    return fig

# Test functions
draw_heat_map()
draw_cat_plot()