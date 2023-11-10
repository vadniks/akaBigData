
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def display(_):
    pass  # jupyter notebook | google research colab


class P5:
    data: pd.DataFrame
    x_over: pd.DataFrame
    y_over: pd.Series
    x_train: pd.DataFrame
    x_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series
    y_predict: np.ndarray
    svm_predictors: np.ndarray
    knn_predictors: np.ndarray

    @staticmethod
    def t1():
        print('t1:')

        P5.data = pd.read_csv("penguins_size.csv")
        print(P5.data, '\n')

        P5.data = P5.data.dropna()
        print(P5.data, '\n')

        cat_columns = P5.data.select_dtypes(['object']).columns
        P5.data[cat_columns] = P5.data[cat_columns].apply(lambda x: pd.factorize(x)[0])
        print(P5.data, '\n')

        print('--------------------------------------------------')

    @staticmethod
    def t2():
        import seaborn as sns
        from imblearn.over_sampling import RandomOverSampler

        fig = plt.figure(figsize=(10, 3))

        fig.add_subplot(1, 2, 1)
        P5.data.species.value_counts(normalize=True).plot.pie()

        fig.add_subplot(1, 2, 2)
        sns.countplot(x=P5.data.species)

        plt.tight_layout()
        plt.show()

        #

        x = P5.data.drop(['species'], axis=1)
        y = P5.data.species

        over_sample = RandomOverSampler(sampling_strategy='all')
        P5.x_over, y_over = over_sample.fit_resample(x, y)

        P5.y_over = pd.Series(y_over)
        print('t2:\n', P5.y_over.value_counts())

        print('--------------------------------------------------')

    @staticmethod
    def t3():
        from sklearn import preprocessing
        from sklearn.model_selection import train_test_split

        print('t3:')

        x = P5.data.values
        min_max_scaler = preprocessing.MinMaxScaler()
        scaled_data = pd.DataFrame(min_max_scaler.fit_transform(x), columns=P5.data.columns)
        print(scaled_data, '\n')

        P5.x_train, P5.x_test, P5.y_train, P5.y_test = train_test_split(
            P5.x_over,
            P5.y_over,
            test_size=.2,
            shuffle=True,
            random_state=59
        )

        print(
            'Size of Predictor Train set', P5.x_train.shape, '\n',
            'Size of Predictor Test set', P5.x_test.shape, '\n',
            'Size of Target Train set', P5.y_train.shape, '\n',
            'Size of Target Test set', P5.y_test.shape
        )

        print('--------------------------------------------------')

    @staticmethod
    def t4():
        import plotly.express as px
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import confusion_matrix
        from sklearn.svm import SVC
        from sklearn.model_selection import GridSearchCV
        from sklearn.neighbors import KNeighborsClassifier

        print('t4:')

        # logistic regression

        model_log = LogisticRegression(random_state=59)
        model_log.fit(P5.x_train, P5.y_train)
        P5.y_predict = model_log.predict(P5.x_test)

        print('Prediction values: \n', P5.y_predict)
        print('Target values: \n', np.array(P5.y_test), '\n')

        plt.rcParams['figure.figsize'] = (10, 10)
        fig = px.imshow(confusion_matrix(P5.y_test, P5.y_predict), text_auto=True)
        display(fig.update_layout(xaxis_title='Target', yaxis_title='Prediction'))

        # print(classification_report(P5.y_test, y_predict), '\n') #

        print((1.00 * 30 + 0.92 * 13 + 1.00 * 24) / (30 + 13 + 24))
        print((1.00 + 0.92 + 1.00) / 3, '\n')

        # svm

        param_kernel = ('linear', 'rbf', 'poly', 'sigmoid')
        parameters = {'kernel': param_kernel}
        model_svc = SVC()
        grid_search_svm = GridSearchCV(estimator=model_svc, param_grid=parameters, cv=6)
        display(grid_search_svm.fit(P5.x_train, P5.y_train))

        best_model = grid_search_svm.best_estimator_
        print(best_model.kernel, '\n')

        P5.svm_predictors = best_model.predict(P5.x_test)
        # print(classification_report(svm_predictors, P5.y_test), '\n') #

        plt.rcParams['figure.figsize'] = (10, 10)
        fig = px.imshow(confusion_matrix(P5.y_test, P5.svm_predictors), text_auto=True)
        display(fig.update_layout(xaxis_title='Target', yaxis_title='Prediction'))

        # knn

        num_of_neighbors = np.arange(3, 10)
        model_knn = KNeighborsClassifier()
        params = {'n_neighbors': num_of_neighbors}
        grid_search = GridSearchCV(estimator=model_knn, param_grid=params, cv=6)

        grid_search.fit(P5.x_train, P5.y_train)
        print(grid_search.best_score_, '\n')
        display(grid_search.best_estimator_)

        P5.knn_predictors = grid_search.predict(P5.x_test)
        # print(classification_report(knn_predictors, P5.y_test), '\n') #

        plt.rcParams['figure.figsize'] = (10, 10)
        fig = px.imshow(confusion_matrix(P5.y_test, P5.knn_predictors), text_auto=True)
        display(fig.update_layout(xaxis_title='Target', yaxis_title='Prediction'))

        print('--------------------------------------------------')

    @staticmethod
    def t5():
        from sklearn.metrics import classification_report

        print('t5:')

        print(classification_report(P5.y_test, P5.y_predict), '\n')
        print(classification_report(P5.svm_predictors, P5.y_test), '\n')
        print(classification_report(P5.knn_predictors, P5.y_test), '\n')

        print('--------------------------------------------------')


if __name__ == '__main__':
    import warnings
    warnings.filterwarnings('ignore')

    P5.t1()
    P5.t2()
    P5.t3()
    P5.t4()
    P5.t5()
