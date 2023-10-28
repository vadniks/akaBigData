
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class P4:

    @staticmethod
    def t1():
        streets = np.array([80, 98, 75, 91, 78])
        garages = np.array([100, 82, 105, 89, 102])

        # 1.1
        print('t1:')
        print(np.corrcoef(streets, garages))
        print(np.corrcoef(streets, garages)[0, 1])
        print('--------------------------------------------------')

        # 1.2
        plt.grid(True)
        plt.title('scatter plot')
        plt.xlabel('Number of cars on the street')
        plt.ylabel('Number of cars inside the garage')
        plt.scatter(streets, garages, marker='o', color='crimson')

    @staticmethod
    def t2():
        from sklearn import preprocessing
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import mean_squared_error

        print('t2:')

        data = pd.read_csv('penguins_size.csv')
        print(data, '\n')

        cat_columns = data.select_dtypes(['object']).columns
        # noinspection PyShadowingNames
        data[cat_columns] = data[cat_columns].apply(lambda x: pd.factorize(x)[0])
        print(data, '\n')

        x = data.drop(['species'], axis=1)
        y = data['species']
        x.replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
        y.replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
        data = data.dropna()

        x = data.values
        scaled_data = pd.DataFrame(preprocessing.MinMaxScaler().fit_transform(x), columns=data.columns)
        scaled_x = data.drop(['species'], axis=1)
        scaled_y = data['species']
        scaled_x.replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
        scaled_y.replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
        print(scaled_data, '\n')

        scaled_data.dropna()
        print(scaled_data, '\n')

        # 2.1
        print(np.corrcoef(scaled_data['species'], scaled_data['body_mass_g']), '\n')
        cr = scaled_data['species'].corr(scaled_data['body_mass_g'])
        print(cr, '\n')

        df = pd.DataFrame(scaled_data, columns=[
            'species island',
            'culmen_length_mm',
            'culmen_depth_mm',
            'flipper_length_mm',
            'body_mass_g',
            'sex'
        ])
        df.corr()
        print(df.corr().round(3), '\n')

        corr = df.corr()
        corr.style.background_gradient(cmap='coolwarm') # display in colab.research.google.com

        # 2.2
        x = scaled_data[['body_mass_g']]
        y = scaled_data['flipper_length_mm']
        x = np.array(x, type(float))
        y = np.array(y, type(float))
        model1 = LinearRegression()
        model1.fit(x, y)
        print(model1.coef_, model1.intercept_, '\n')

        model_a = model1.coef_[0]
        model_b = model1.intercept_
        model_line = model_a * x + model_b
        print(mean_squared_error(model_line, y), '\n')
        print('--------------------------------------------------')

        # 2.3
        plt.figure(figsize=(10, 6))
        plt.plot(x, model_line, linewidth=2, color='r', label=f'linear_model = {model_a:.2f}x + {model_b:.2f}')
        plt.scatter(x, y, alpha=0.7)
        plt.grid()
        plt.xlabel('feature')
        plt.ylabel('target')
        plt.legend(prop={'size': 16})
        plt.show()

    @staticmethod
    def t3():
        import scipy.stats as stats
        import statsmodels.api as sm
        from statsmodels.formula.api import ols
        # noinspection PyProtectedMember
        from statsmodels.stats.multicomp import pairwise_tukeyhsd

        print('t3:')

        data = pd.read_csv('insurance.csv')
        print(data, '\n')
        data.info()
        print('\n')

        for column in data.columns:
            na = np.mean(data[column].isna() * 100)
            print(f' {column} : {round(na, 1)}%')
        print('\n')

        region_bmi = pd.DataFrame({'region': data['region'], 'bmi': data['bmi']})
        groups = region_bmi.groupby('region').groups

        northeast = data['bmi'][groups['northeast']]
        northwest = data['bmi'][groups['northwest']]
        southeast = data['bmi'][groups['southeast']]
        southwest = data['bmi'][groups['southwest']]

        # 3.1
        print(stats.f_oneway(northeast, northwest, southeast, southwest), '\n')

        # 3.2
        model_lm = ols('bmi ~ region', data=region_bmi).fit()
        anova_result = sm.stats.anova_lm(model_lm, typ=2)
        print(anova_result, '\n')

        # 3.3
        regions = ['northeast', 'northwest', 'southeast', 'southwest']
        region_pairs = []

        for i in range(4):
            for j in range(i + 1, 4):
                region_pairs.append((regions[i], regions[j]))

        for i, j, in region_pairs:
            print(i, j)
            print(stats.ttest_ind(data['bmi'][groups[i]], data['bmi'][groups[j]]))
        print('\n')

        # 3.4
        print(data['bmi'].mean())
        print(data['bmi'].median())
        print('\n')

        # noinspection SpellCheckingInspection
        tukey = pairwise_tukeyhsd(endog=data['bmi'], groups=data['region'], alpha=0.05)
        tukey.plot_simultaneous()
        plt.vlines(x=30.66, ymin=-0.5, ymax=4.5, color="red")
        print(tukey.summary(), '\n')

        # optional
        cat_columns = data.select_dtypes(['object']).columns
        data[cat_columns] = data[cat_columns].apply(lambda x: pd.factorize(x)[0])
        print(data, '\n')

        # 3.5
        model = ols('bmi ~ C(region) + C(sex) + C(region) : C(sex)', data=data).fit()
        print(sm.stats.anova_lm(model, type=2), '\n\n')

        # 3.6
        data['combination'] = data['region'] + data['sex']
        # noinspection SpellCheckingInspection
        tukey = pairwise_tukeyhsd(endog=data['bmi'], groups=data['combination'], alpha=0.05)
        tukey.plot_simultaneous()
        plt.vlines(x=30.66, ymin=-1, ymax=8, color='red')
        print(tukey.summary(), '\n')


if __name__ == '__main__':
    import warnings
    warnings.filterwarnings('ignore')

    P4.t1()
    P4.t2()
    P4.t3()
