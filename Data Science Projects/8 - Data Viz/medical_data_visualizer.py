import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
df.set_index("id", inplace=True)

# Add 'overweight' column
df['overweight'] = (df['weight']/ (df['height']/100**2))
df['overweight'] = df['overweight'].apply(lambda x : 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['gluc'] = df['gluc'].apply(lambda x : 0 if x ==1 else 1)
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = 'cardio', value_vars=["cholesterol", 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
    df_cat = df_cat.rename(columns={'value': 'total'})  

    # Draw the catplot with 'sns.catplot()'

    fig = sns.catplot(x='variable',y=None,hue='value',col='cardio',data=df_cat,kind='count')
    fig.set_ylabels('total')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    figOut = fig.fig
    return figOut


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
    df['height'] >= (df['height'].quantile(0.025)) &
    df['height'] >= (df['height'].quantile(0.975)) &
    df['weight'] >= (df['weight'].quantile(0.025)) &
    df['weight'] >= (df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True,fmt='0.1f',vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
