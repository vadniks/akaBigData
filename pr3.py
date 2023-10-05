
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sts


class P3:
    data: pd.DataFrame
    data2: pd.DataFrame
    data3: pd.DataFrame

    @staticmethod
    def t1():
        P3.data = pd.read_csv('insurance.csv')

    @staticmethod
    def t2():
        print('t2:')
        print(P3.data.head())
        print()
        print(P3.data.describe())
        print('--------------------------------------------------')

    @staticmethod
    def t3():
        fig, ax = plt.subplots(1, 4, figsize=(15, 4))
        ax[0].hist(P3.data.age, edgecolor='black', color='green', bins=15, label='bins=15')
        ax[0].title.set_text('Age')
        ax[0].legend()
        ax[1].hist(P3.data.bmi, edgecolor='black', color='green', bins=15, label='bins=15')
        ax[1].title.set_text('BMI')
        ax[1].legend()
        ax[2].hist(P3.data.charges, edgecolor='black', color='green', bins=15, label='bins=15')
        ax[2].title.set_text('Charges')
        ax[2].legend()
        ax[3].hist(P3.data.children, edgecolor='black', color='green', bins=15, label='bins=15')
        ax[3].title.set_text('Children')
        ax[3].legend()

    @staticmethod
    def t4():
        bmi = P3.data['bmi']
        charges = P3.data['charges']

        mean_bmi = bmi.mean()
        median_bmi = bmi.median()
        mode_bmi = bmi.mode().values[0]

        mean_charges = charges.mean()
        median_charges = charges.median()
        mode_charges = charges.mode().values[0]

        print('t4:')
        print('Mean BMI = %f' % mean_bmi)
        print('Mode BMI: ', mode_bmi)
        print('Median BMI = %f' % median_bmi)
        print(' ')
        print('Mean Charges = %f' % mean_charges)
        print('Mode Charges: ', mode_charges)
        print('Median Charges = %f' % median_charges)
        print()

        # noinspection PyArgumentList
        def measure_of_dispersion(which):
            std = P3.data[which].std()
            rang = P3.data[which].max() - P3.data[which].min()
            q1 = np.percentile(P3.data[which], 25, interpolation='midpoint')
            q3 = np.percentile(P3.data[which], 75, interpolation='midpoint')
            iqr1 = q3 - q1
            iqr2 = sts.iqr(P3.data[which], interpolation='midpoint')

            print(f'Standard Deviation of {which}: ', std)
            print(f'Range of {which}: ', rang)
            print(f'Quarter range of {which} using numpy: ', iqr1)
            print(f'Quarter range of {which} with scipy: ', iqr2)

        measure_of_dispersion('charges')
        print()
        measure_of_dispersion('bmi')
        print('--------------------------------------------------')

        fig, ax = plt.subplots(1, 2, figsize=(15, 4))
        ax[0].hist(P3.data.bmi, edgecolor='black', color='green', bins=15, label='bins=15')
        ax[1].hist(P3.data.charges, edgecolor='black', color='green', bins=15, label='bins=15')

        ax[0].axvline(mean_bmi, color='r', linestyle='--', label='Mean')
        ax[0].axvline(median_bmi, color='g', linestyle='-', label='Median')
        ax[0].axvline(mode_bmi, color='b', linestyle='-', label='Mode')
        ax[0].set_title('BMI')
        ax[0].legend()

        ax[1].axvline(mean_charges, color='r', linestyle='--', label='Mean')
        ax[1].axvline(median_charges, color='g', linestyle='-', label='Median')
        ax[1].axvline(mode_charges, color='b', linestyle='-', label='Mode')
        ax[1].set_title('Charges')
        ax[1].legend()

    @staticmethod
    def t5():
        plt.figure(figsize=(8, 8))
        plt.boxplot(
            [P3.data['bmi'], P3.data['charges'], P3.data['age'], P3.data['children']],
            labels=['bmi', 'charges', 'age', 'children'],
            vert=False
        )
        plt.xticks(np.arange(0, 105, 5))
        plt.grid()
        plt.show()

        fig, ax = plt.subplots(1, 4, figsize=(15, 4))
        ax[0].boxplot(P3.data.age, vert=False)
        ax[0].set_title('Age')
        ax[0].grid()
        ax[1].boxplot(P3.data.bmi, vert=False)
        ax[1].set_title('BMI')
        ax[1].grid()
        ax[2].boxplot(P3.data.charges, vert=False)
        ax[2].set_title('Charges')
        ax[2].grid()
        ax[3].boxplot(P3.data.children, vert=False)
        ax[3].set_title('Children')
        ax[3].grid()

    @staticmethod
    def t6():
        import seaborn as sns

        samples = [1, 10, 50, 100, 150, 200]
        np.random.seed(123)
        set_of_means = []
        for i in samples:
            x = [np.mean(P3.data['charges'].sample(i)) for _ in range(300)]
            set_of_means.append(x)
        sns.distplot(set_of_means)

        k = 0
        fig, ax = plt.subplots(3, 2, figsize=(10, 11))
        for i in range(0, 3):
            for j in range(0, 2):
                ax[i, j].hist(set_of_means[k], 10, density=True, edgecolor='black', color='green')
                ax[i, j].set_title(label=('n = ', samples[k]))
                k += 1
        plt.show()

        def mean_std(ii, n):
            df = pd.DataFrame(set_of_means[ii], columns=[f'n={n}'])
            print('Mean of ', df.mean().to_string(), ' ', 'Std of ', df.std().to_string())

        print('t6:')
        mean_std(0, 1)
        mean_std(1, 10)
        mean_std(2, 50)
        mean_std(3, 100)
        mean_std(4, 150)
        mean_std(5, 200)

        std = P3.data['charges'].std()
        rang = P3.data['charges'].max() - P3.data['charges'].min()
        # noinspection PyArgumentList
        q1 = np.percentile(P3.data['charges'], 25, interpolation='midpoint')
        # noinspection PyArgumentList
        q3 = np.percentile(P3.data['charges'], 75, interpolation='midpoint')
        iqr1 = q3 - q1
        iqr2 = sts.iqr(P3.data['charges'], interpolation='midpoint')

        print()
        print('Standard Deviation: ', std)
        print('Range: ', rang)
        print('Quarter range using numpy: ', iqr1)
        print('Quarter range with scipy: ', iqr2)
        print('--------------------------------------------------')

    @staticmethod
    def t7():
        print('t7:')

        print('90% confidence interval for Charges: ', sts.norm.interval(
            confidence=0.90,
            loc=np.mean(P3.data['charges']),
            scale=sts.sem(P3.data['charges'])
        ))

        print('95% confidence interval for Charges: ', sts.norm.interval(
            confidence=0.95,
            loc=np.mean(P3.data['charges']),
            scale=sts.sem(P3.data['charges'])
        ))

        print('90% confidence interval for BMI: ', sts.norm.interval(
            confidence=0.90,
            loc=np.mean(P3.data['bmi']),
            scale=sts.sem(P3.data['bmi'])
        ))

        print('95% confidence interval for BMI: ', sts.norm.interval(
            confidence=0.95,
            loc=np.mean(P3.data['bmi']),
            scale=sts.sem(P3.data['bmi'])
        ))

        print('--------------------------------------------------')

    @staticmethod
    def t8():
        import pylab

        sts.probplot(P3.data['charges'], dist='norm', plot=pylab)
        pylab.ylabel('charges')
        pylab.xlabel('normals')
        pylab.title('QQ for Charges')
        pylab.show()

        sts.probplot(P3.data['bmi'], dist='norm', plot=pylab)
        pylab.ylabel('bmi')
        pylab.xlabel('normals')
        pylab.title('QQ for BMI')
        pylab.show()

        print('t8:')
        print(sts.kstest(P3.data['bmi'], 'norm', sts.norm.fit(P3.data['bmi'])))
        print(sts.kstest(P3.data['charges'], 'norm', sts.norm.fit(P3.data['charges'])))
        print('--------------------------------------------------')

    @staticmethod
    def t9():
        P3.data2 = pd.read_csv('ECDCCases.csv')
        print('t9:')
        print(P3.data2)
        print()
        P3.data2.info()
        print('--------------------------------------------------')

    @staticmethod
    def t10():
        print('t10:')

        def check_na():
            for column in P3.data2.columns:
                na = np.mean(P3.data2[column].isna() * 100)
                print(f' {column} : {round(na, 1)}%')
        check_na()
        print()

        P3.data2 = P3.data2.drop(['Cumulative_number_for_14_days_of_COVID-19_cases_per_100000', 'geoId'], axis=1)
        P3.data2['countryterritoryCode'].fillna('Other', inplace=True)
        P3.data2['popData2019'].fillna(P3.data2['popData2019'].median(), inplace=True)
        print(P3.data2)
        print()

        check_na()
        print('--------------------------------------------------')

    @staticmethod
    def t11():
        print('t11:')
        print(P3.data2.describe())
        print()

        plt.figure(figsize=(5, 4))
        plt.boxplot(
            [
                P3.data2['day'], P3.data2['month'], P3.data2['year'],
                P3.data2['cases'], P3.data2['deaths'], P3.data2['popData2019']
            ],
            labels=['day', 'month', 'year', 'cases', 'deaths', 'popData2019'],
            vert=False
        )
        plt.grid()
        plt.show()

        data2_outliers = P3.data2.select_dtypes(exclude=['object'])
        for column in data2_outliers:
            plt.figure(figsize=(5, 4))
            data2_outliers.boxplot([column])

        deaths_above_3000 = P3.data2['deaths'] >= 3000
        print(deaths_above_3000)
        print()
        print(f'There are {sum(deaths_above_3000 == True)} days where deaths >= 3000')
        print()
        print(P3.data2[deaths_above_3000])
        print('--------------------------------------------------')

    @staticmethod
    def t12():
        print('t12:')
        print(P3.data2[P3.data2.duplicated()])
        print()

        P3.data3 = P3.data2.drop_duplicates()
        print(P3.data3)
        print()
        print(P3.data3[P3.data3.duplicated()])
        print('--------------------------------------------------')

    @staticmethod
    def t13():
        from statsmodels.stats.weightstats import ttest_ind

        P3.data3 = pd.read_csv('bmi.csv')
        print('t13:')
        print(P3.data3.head())
        print()

        data3_northwest = P3.data3.loc[P3.data3['region'] == 'northwest']
        print(data3_northwest)
        print()

        data3_southwest = P3.data3.loc[P3.data3['region'] == 'southwest']
        print(data3_southwest)
        print()

        print('The variance of both data groups:', np.var(data3_northwest['bmi']), np.var(data3_southwest['bmi']), '\n')
        print(sts.ttest_ind(a=data3_northwest['bmi'], b=data3_southwest['bmi'], equal_var=True), '\n')
        print(ttest_ind(data3_northwest['bmi'], data3_southwest['bmi']), '\n')

        print(sts.shapiro(data3_northwest['bmi']), '\n', sts.shapiro(data3_southwest['bmi']), '\n')

        print(sts.bartlett(data3_northwest['bmi'], data3_southwest['bmi']))
        print('--------------------------------------------------')

    @staticmethod
    def t14():
        data4 = pd.DataFrame([[1, 97], [2, 98], [3, 109], [4, 95], [5, 97], [6, 104]], columns=['N', 'Observed'])
        data4['Expected'] = 100

        print('t14:')
        print(data4, '\n')
        print(sts.chisquare(data4['Observed'], data4['Expected']))
        print('--------------------------------------------------')

    @staticmethod
    def t15():
        data = pd.DataFrame({
            'Married': [89, 17, 11, 43, 22, 1],
            'Civil marriage': [80, 22, 20, 35, 6, 4],
            'Isn\'t in relationships': [35, 44, 35, 6, 8, 22]
        })

        data.index = [
            'Full working day',
            'Part-time employment',
            'Temporary doesn\'t work',
            'On the household',
            'Retired',
            'Studying'
        ]

        print('t15:')
        print(data.head())
        print()
        _, p_value, _, _ = sts.chi2_contingency(data)
        print(p_value)
        print('--------------------------------------------------')


if __name__ == '__main__':
    import warnings
    warnings.filterwarnings('ignore')

    P3.t1()
    P3.t2()
    P3.t3()
    P3.t4()
    P3.t5()
    P3.t6()
    P3.t7()
    P3.t8()
    P3.t9()
    P3.t10()
    P3.t11()
    P3.t12()
    P3.t13()
    P3.t14()
    P3.t15()
