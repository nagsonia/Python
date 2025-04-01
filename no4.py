import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    df = pd.read_csv("medical_examination.csv")
    df['overweight'] = ((df['weight'] / (df['height'] / 100) ** 2) > 25).astype(int)
    df[['cholesterol', 'gluc']] = (df[['cholesterol', 'gluc']] > 1).astype(int)
    return df

def draw_cat_plot():
    df = load_data()
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat).fig
    return fig

def draw_heat_map():
    df = load_data()
    df = df[(df['ap_lo'] <= df['ap_hi']) & df['height'].between(df['height'].quantile(0.025), df['height'].quantile(0.975)) & df['weight'].between(df['weight'].quantile(0.025), df['weight'].quantile(0.975))]
    mask = np.triu(np.ones_like(df.corr(), dtype=bool))
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, fmt='.1f', mask=mask, cmap='coolwarm', square=True, linewidths=0.5, cbar_kws={'shrink': 0.5})
    return fig
