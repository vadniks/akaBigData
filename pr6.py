
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import matplotlib.pyplot as plt


class P6:
    data: pd.DataFrame

    @staticmethod
    def t1():
        P6.data = pd.read_csv("penguins_size.csv")
        print(P6.data)
        P6.data = P6.data.dropna()

        cat_columns = P6.data.select_dtypes(['object']).columns
        P6.data[cat_columns] = P6.data[cat_columns].apply(lambda x: pd.factorize(x)[0])
        print(P6.data)

    @staticmethod
    def t2():
        from sklearn.cluster import KMeans
        from sklearn.metrics import silhouette_score

        models = []
        score1 = []
        score2 = []
        for i in range(2, 10):
            model = KMeans(n_clusters=i, random_state=123, init='k-means++').fit(P6.data)
            models.append(model)
            # noinspection PyUnresolvedReferences
            score1.append(model.inertia_)
            # noinspection PyUnresolvedReferences
            score2.append(silhouette_score(P6.data, model.labels_))

        # elbow rule
        plt.grid()
        plt.plot(np.arange(2, 10), score1, marker='o')
        plt.show()

        # silhouette coefficient
        plt.grid()
        plt.plot(np.arange(2, 10), score2, marker='o')
        plt.show()

        # actual clusterization
        model1 = KMeans(n_clusters=2, random_state=123, init='k-means++')
        model1.fit(P6.data)
        print(model1.cluster_centers_)

        labels = model1.labels_
        P6.data['cluster'] = labels
        print(P6.data.cluster.value_counts())

        # noinspection PyTypeChecker
        fig = go.Figure(data=[go.Scatter3d(
            x=P6.data.culmen_length_mm,
            y=P6.data.flipper_length_mm,
            z=P6.data.body_mass_g,
            mode='markers',
            marker_color=P6.data.cluster,
            marker_size=4
        )])
        fig.show()

    @staticmethod
    def t3():
        from sklearn.cluster import AgglomerativeClustering

        model2 = AgglomerativeClustering(2, compute_distances=True)
        clustering = model2.fit(P6.data)
        # noinspection PyUnresolvedReferences
        P6.data.cluster = clustering.labels_

        # noinspection PyTypeChecker
        fig = go.Figure(data=[go.Scatter3d(
            x=P6.data.culmen_length_mm,
            y=P6.data.flipper_length_mm,
            z=P6.data.body_mass_g,
            mode='markers',
            marker_color=P6.data.cluster,
            marker_size=4
        )])
        fig.show()

    @staticmethod
    def t4():
        from sklearn.cluster import DBSCAN

        model3 = DBSCAN(eps=11, min_samples=5).fit(P6.data)
        # noinspection PyUnresolvedReferences
        P6.data.cluster = model3.labels_

        # noinspection PyTypeChecker
        fig = go.Figure(data=[go.Scatter3d(
            x=P6.data.species,
            y=P6.data.flipper_length_mm,
            z=P6.data.body_mass_g,
            mode='markers',
            marker_color=P6.data.cluster,
            marker_size=4
        )])
        fig.show()

    @staticmethod
    def t5():
        from sklearn.manifold import TSNE
        from sklearn.preprocessing import StandardScaler
        import seaborn as sns

        label = P6.data.species

        dropped = P6.data.drop('species', axis=1)

        scaled_dropped = StandardScaler().fit_transform(dropped)
        first_1000 = scaled_dropped[0:1000, :]
        first_labels_1000 = label[0:1000]

        model_1 = TSNE(n_components=2, perplexity=5, random_state=123)
        tsne_features = model_1.fit_transform(first_1000)
        tsne_data = np.vstack((tsne_features.T, first_labels_1000)).T
        # noinspection PyTypeChecker
        tsne_df = pd.DataFrame(data=tsne_data, columns=('X', 'Y', 'class_type'))

        sns.scatterplot(data=tsne_df, x='X', y='Y', hue='class_type', palette='bright')
        plt.title('Perplexity 5')
        plt.show()


if __name__ == '__main__':
    import warnings
    warnings.filterwarnings('ignore')

    P6.t1()
    P6.t2()
    P6.t3()
    P6.t4()
