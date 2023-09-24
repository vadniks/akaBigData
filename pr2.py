
from typing import Any
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


class P2:
    data: pd.DataFrame
    data2: pd.DataFrame
    first_1000: Any
    first_labels_1000: Any

    @staticmethod
    def t1():
        P2.data = pd.read_csv('q1data.csv')

    @staticmethod
    def t2():
        print('t2:')
        P2.data.info()
        print('t2:\n', P2.data.head())
        print('\n')

        if P2.data.isnull().values.any():
            P2.data = P2.data.dropna()

    @staticmethod
    def t3():
        import plotly.graph_objs as go
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=P2.data.six_regions,
            y=P2.data.life_exp,
            marker=dict(
                color=list(range(len(P2.data.country))),
                coloraxis='coloraxis',
                line=dict(color='black', width=2)
            )
        ))

        fig.update_layout(
            title='Population in the Six Regions',
            title_x=0.5,
            title_font_size=20,
            xaxis_title='Six Regions',
            xaxis_title_font_size=16,
            xaxis_tickfont_size=14,
            yaxis_title='Population',
            yaxis_title_font_size=16,
            yaxis_tickfont_size=14,
            width=1400,
            height=700,
            margin=dict(l=0, r=0, t=30, b=0)
        )

        fig.update_xaxes(showline=True, tickangle=-45, linewidth=2, linecolor='black', gridcolor='ivory')
        fig.update_yaxes(showline=True, tickangle=-45, linewidth=2, linecolor='black', gridcolor='ivory')
        fig.show()

    @staticmethod
    def t4():
        import plotly.express as px

        colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
        fig = px.pie(P2.data, values='population', names='six_regions', title='Population of European continent')

        fig.update_traces(
            hoverinfo='label+percent',
            textinfo='value',
            textfont_size=20,
            marker=dict(colors=colors, line=dict(color='#000000', width=2))
        )

        fig.update_layout(title='Population and Countries', title_x=0.5)
        fig.show()

    @staticmethod
    def t5():
        def plot(x, y, title, x_label, y_label):
            plt.rc('axes', axisbelow=True)
            px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
            plt.subplots(figsize=(1920*px, 700*px))

            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.scatter(x, y, color='white', edgecolor='black', linewidth=2, zorder=2)

            plt.plot(x, y, color='red', zorder=1)
            plt.grid(linewidth=2, color='mistyrose')
            plt.show()

        plot(P2.data.income, P2.data.life_exp, 'Income vs Life Expectancy', 'Income', 'Life Expectancy')
        plot(P2.data.income, P2.data.population, 'Income vs Population', 'Income', 'Population')

    @staticmethod
    def t6():
        from sklearn.preprocessing import StandardScaler
        from sklearn.manifold import TSNE

        P2.data2 = pd.read_csv('mnist_train.csv')
        print('t6:', P2.data2.head())

        labels = P2.data2['label']
        labels_dropped = P2.data2.drop('label', axis=1)

        standard = StandardScaler().fit_transform(labels_dropped)
        start_time = time.time()

        P2.first_1000 = standard[0:1000, :]
        P2.first_labels_1000 = labels[0:1000]

        def plot(perplexity):
            model = TSNE(n_components=2, perplexity=perplexity, random_state=123)
            tsne_features = model.fit_transform(P2.first_1000)

            tsne_data = np.vstack((tsne_features.T, P2.first_labels_1000)).T
            tsne_df = pd.DataFrame(data=tsne_data, columns=['X', 'Y', 'class_type'])

            sns.scatterplot(data=tsne_df, x='X', y='Y', hue='class_type', palette='bright')
            plt.title(f'Perplexity {perplexity}')
            plt.show()

        plot(5)
        plot(25)
        plot(50)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f't6: Elapsed time: {elapsed_time} seconds')

    @staticmethod
    def t7():
        import umap

        start_time = time.time()

        def plot(n_neighbors, min_dist):
            embedding = umap.UMAP(
                n_neighbors=n_neighbors,
                min_dist=min_dist,
                random_state=123,
                metric='correlation'
            ).fit_transform(P2.first_1000)

            umap_data = np.vstack((embedding.T, P2.first_labels_1000)).T
            umap_df = pd.DataFrame(data=umap_data, columns=['X', 'Y', 'class_type'])

            plt.title(f'n_neighbors={n_neighbors}, min_dist={min_dist}')
            sns.scatterplot(data=umap_df, x='X', y='Y', hue='class_type', palette='bright')
            plt.show()

        plot(5, 0.1)
        plot(25, 0.5)
        plot(50, 1.0)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f't7: Elapsed time: {elapsed_time} seconds')


if __name__ == '__main__':
    import warnings
    warnings.filterwarnings('ignore')

    P2.t1()
    P2.t2()
    P2.t3()
    P2.t4()
    P2.t5()
    P2.t6()
    P2.t7()
