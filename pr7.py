
import pandas as pd
from sklearn.metrics import f1_score
import time


def display(_):
    pass


class P7:
    data: pd.DataFrame
    x_train = None
    x_test = None
    y_train = None
    y_test = None

    @staticmethod
    def t1():
        from sklearn.model_selection import train_test_split

        P7.data = pd.read_csv('penguins_size.csv')
        print(P7.data)

        P7.data = P7.data.dropna()

        cat_columns = P7.data.select_dtypes(['object']).columns
        # noinspection PyShadowingNames
        P7.data[cat_columns] = P7.data[cat_columns].apply(lambda x: pd.factorize(x)[0])
        print(P7.data)

        x = P7.data.drop(['species'], axis=1)
        y = P7.data['species']

        P7.x_train, P7.x_test, P7.y_train, P7.y_test \
            = train_test_split(x, y, test_size=.2, shuffle=True, random_state=59)

        print(
            '\n',
            'Size of Predictor Train set', P7.x_train.shape, '\n',
            'Size of Predictor Test set', P7.x_test.shape, '\n',
            'Size of Target Train set', P7.y_train.shape, '\n',
            'Size of Target Test set', P7.y_test.shape
        )

    @staticmethod
    def t2():
        from sklearn.model_selection import GridSearchCV
        from sklearn.ensemble import RandomForestClassifier

        # regular tree

        start_time = time.time()
        random_forest = RandomForestClassifier(max_depth=15, min_samples_split=10).fit(P7.x_train, P7.y_train)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f'Elapsed time: {elapsed_time} seconds')

        # noinspection PyUnresolvedReferences
        train_predictions = random_forest.predict(P7.x_train)
        print('F1 metric for training set', f1_score(train_predictions, P7.y_train, average='macro'))

        # noinspection PyUnresolvedReferences
        test_predictions = random_forest.predict(P7.x_test)
        print('F1 metric for test set', f1_score(test_predictions, P7.y_test, average='macro'))

        # bagging (aka tuning for trees)

        random_forest = RandomForestClassifier()

        params_grid = {
            'max_depth': [12, 18],
            'min_samples_leaf': [3, 10],
            'min_samples_split': [6, 12],
        }

        start_time = time.time()

        grid_search_random_forest = GridSearchCV(
            estimator=random_forest, param_grid=params_grid, scoring='f1_macro', cv=5
        )
        grid_search_random_forest.fit(P7.x_train, P7.y_train)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'\nElapsed time: {elapsed_time} seconds')

        best_model = grid_search_random_forest.best_estimator_
        train_predictions = best_model.predict(P7.x_train)
        print('F1 metric for training set', f1_score(train_predictions, P7.y_train, average='macro'))

        test_predictions = best_model.predict(P7.x_test)
        print('F1 metric for test set', f1_score(test_predictions, P7.y_test, average='macro'))

    @staticmethod
    def t3():
        import catboost as cb

        start_time = time.time()
        model_boost = cb.CatBoostClassifier(iterations=3000, task_type='CPU', devices='0')
        # 'GPU' works only on GPUs with CUDA cores - can be solved with running within Google Colab

        model_boost.fit(P7.x_train, P7.y_train)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f'\nElapsed time: {elapsed_time} seconds')

        train_predictions_boosted = model_boost.predict(P7.x_train, task_type='CPU')
        print('Boosted F1 metric for train set', f1_score(train_predictions_boosted, P7.y_train, average='macro'))

        test_predictions_boosted = model_boost.predict(P7.x_test, task_type='CPU')
        print('Boosted F1 metric for test set', f1_score(test_predictions_boosted, P7.y_test, average='macro'))


if __name__ == '__main__':
    P7.t1()
    P7.t2()
    P7.t3()
