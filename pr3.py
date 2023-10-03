
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
        P3.data = pd.read_csv("insurance.csv")

    @staticmethod
    def t2():
        print(P3.data.head())
        print(P3.data.describe())

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
        mean_bmi = P3.data['bmi'].mean()
        median_bmi = P3.data['bmi'].median()
        mode_bmi = P3.data['bmi'].mode().values[0]

        mean_charges = P3.data['charges'].mean()
        median_charges = P3.data['charges'].median()
        mode_charges = P3.data['charges'].mode().values[0]

        print('Mean BMI = %f' % mean_bmi)
        print('Mode BMI: ', mode_bmi)
        print('Median BMI = %f' % median_bmi)
        print(' ')
        print('Mean Charges = %f' % mean_charges)
        print('Mode Charges: ', mode_charges)
        print('Median Charges = %f' % median_charges)

        #

        fig, ax = plt.subplots(1, 2, figsize=(15, 4))
        ax[0].hist(P3.data.bmi, edgecolor='black', color='green', bins=15, label='bins=15')

        ax[1].hist(P3.data.charges, edgecolor='black', color='green', bins=15, label='bins=15')

        ax[0].axvline(mean_bmi, color='r', linestyle='--', label="Mean")
        ax[0].axvline(median_bmi, color='g', linestyle='-', label="Median")
        ax[0].axvline(mode_bmi, color='b', linestyle='-', label="Mode")
        ax[0].set_title('BMI')
        ax[0].legend()

        ax[1].axvline(mean_charges, color='r', linestyle='--', label="Mean")
        ax[1].axvline(median_charges, color='g', linestyle='-', label="Median")
        ax[1].axvline(mode_charges, color='b', linestyle='-', label="Mode")
        ax[1].set_title('Charges')
        ax[1].legend()

    @staticmethod
    def t5():
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

        samples = [50, 100, 150, 200, 250, 300]
        set_of_means = []
        for i in samples:
            x = [np.mean(P3.data['charges'].sample(i)) for j in range(300)]
            set_of_means.append(x)

        sns.distplot(set_of_means)

        k = 0
        fig, ax = plt.subplots(3, 2, figsize=(10, 11))
        for i in range(0, 3):
            for j in range(0, 2):
                ax[i, j].hist(set_of_means[k], 10, density=True, edgecolor='black', color='green')
                ax[i, j].set_title(label=("n = ", samples[k]))
                k += 1
        plt.show()

        std = P3.data['charges'].std()
        rang = P3.data['charges'].max() - P3.data['charges'].min()
        # noinspection PyArgumentList
        q1 = np.percentile(P3.data['charges'], 25, interpolation='midpoint')
        # noinspection PyArgumentList
        q3 = np.percentile(P3.data['charges'], 75, interpolation='midpoint')
        iqr1 = q3 - q1
        iqr2 = sts.iqr(P3.data['charges'], interpolation='midpoint')

        print('Standard Deviation: ', std)
        print('Range: ', rang)
        print('Quarter range using numpy: ', iqr1)
        print('Quarter range with scipy: ', iqr2)

    @staticmethod
    def t7():
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

    @staticmethod
    def t8():
        import pylab

        sts.probplot(P3.data['charges'], dist="norm", plot=pylab)
        pylab.show()
        sts.probplot(P3.data['bmi'], dist="norm", plot=pylab)
        pylab.show()

        print(sts.kstest(P3.data['bmi'], 'norm', sts.norm.fit(P3.data['bmi'])))
        print(sts.kstest(P3.data['charges'], 'norm', sts.norm.fit(P3.data['charges'])))

    @staticmethod
    def t9():
        P3.data2 = pd.read_csv('ECDCCases.csv')
        print(P3.data2)
        P3.data2.info()

    @staticmethod
    def t10():
        def check_na():
            for column in P3.data2.columns:
                na = np.mean(P3.data2[column].isna() * 100)
                print(f" {column} : {round(na, 1)}%")
        check_na()

        P3.data2 = P3.data2.drop(['Cumulative_number_for_14_days_of_COVID-19_cases_per_100000', 'geoId'], axis=1)
        P3.data2["countryterritoryCode"].fillna("Other", inplace=True)
        P3.data2["popData2019"].fillna(P3.data2['popData2019'].median(), inplace=True)
        print(P3.data2)

        check_na()

    @staticmethod
    def t11():
        print(P3.data2.describe())

        deaths_above_3000 = P3.data2['deaths'] >= 3000
        print(deaths_above_3000)

        print(sum(deaths_above_3000 == True))
        print(P3.data2[deaths_above_3000])

    @staticmethod
    def t12():
        print(P3.data2[P3.data2.duplicated()])

        P3.data3 = P3.data2.drop_duplicates()
        print(P3.data3)
        print(P3.data3[P3.data3.duplicated()])

    @staticmethod
    def t13():
        from statsmodels.stats.weightstats import ttest_ind

        P3.data3 = pd.read_csv('bmi.csv')
        print(P3.data3.head())

        data3_northwest = P3.data3.loc[P3.data3['region'] == 'northwest']
        print(data3_northwest)

        data3_southwest = P3.data3.loc[P3.data3['region'] == 'southwest']
        print(data3_southwest)

        print(np.var(data3_northwest['bmi']), np.var(data3_southwest['bmi']))
        print(sts.ttest_ind(a=data3_northwest['bmi'], b=data3_southwest['bmi'], equal_var=True))
        print(ttest_ind(data3_northwest['bmi'], data3_southwest['bmi']))

        print(sts.shapiro(data3_northwest['bmi']), '\n', sts.shapiro(data3_southwest['bmi']))

        print(sts.bartlett(data3_northwest['bmi'], data3_southwest['bmi']))

    @staticmethod
    def t14():
        data = [[1, 97], [2, 98], [3, 109], [4, 95], [5, 97], [6, 104]]

        data4 = pd.DataFrame(data, columns=["N", "Observed"])
        data4['Expected'] = 100
        print(data4)

        print(sts.chisquare(data4['Observed'], data4['Expected']))

    @staticmethod
    def t15():
        data = pd.DataFrame({
            'Married': [89, 17, 11, 43, 22, 1],
            'Civil marriage': [80, 22, 20, 35, 6, 4],
            'Doesn\'t stay in relationships': [35, 44, 35, 6, 8, 22]
        })

        data.index = [
            'Full working day',
            'Part-time employment',
            'Temporary doesn\'t work',
            'On the household',
            'Retired',
            'Studying'
        ]

        print(data.head())
        _, p_value, _, _ = sts.chi2_contingency(data)
        print(p_value)


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
