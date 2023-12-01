
import pandas as pd
import time
import matplotlib.pyplot as plt


class P8:
    data = pd.DataFrame
    times = []
    basket = []
    data2 = pd.DataFrame
    times2 = []
    basket2 = []

    @staticmethod
    def t1():
        P8.data = pd.read_csv("Market_Basket_Optimisation.csv")
        print(P8.data, '\n')
        P8.data.info()
        print()

    # noinspection PyArgumentList, PyUnresolvedReferences
    @staticmethod
    def visualize_frequencies(data):
        top_20 = data.stack().value_counts()[:20]
        print(top_20)

        top_20_normalized = data.stack().value_counts(normalize=True)[:20]
        print(top_20_normalized, '\n')
        top_20_normalized.plot(kind='bar')  # relative frequency

        top_20.apply(lambda item: item / data.shape[0]).plot(kind='bar')  # actual frequency

    @staticmethod
    def t2():
        P8.visualize_frequencies(P8.data)

    @staticmethod
    def apriori_algorithms(
        data,
        basket,
        times,
        first_min_sup,
        first_min_conf,
        second_min_support,
        second_min_confidence,
        second_min_lift,
        third_min_support,
        third_min_confidence
    ):
        # noinspection PyUnresolvedReferences, PyShadowingNames
        for i in range(data.shape[0]):
            # noinspection PyUnresolvedReferences
            row = data.iloc[i].dropna().tolist()
            basket.append(row)

        print(basket[0][0], basket[0], '\n')

        def first():
            from apriori_python import apriori

            start = time.perf_counter()
            _, rules = apriori(P8.basket, minSup=first_min_sup, minConf=first_min_conf)
            time2 = time.perf_counter() - start
            times.append(time2)

            print(rules, '\n')
        first()

        def second():
            from apyori import apriori

            start = time.perf_counter()
            rules = apriori(
                transactions=basket,
                min_support=second_min_support,
                min_confidence=second_min_confidence,
                min_lift=second_min_lift
            )

            results = list(rules)
            time2 = time.perf_counter() - start
            times.append(time2)

            print(results, '\n')

            # results beautifying

            y = list(results)
            for result in y:
                for subset in result[2]:
                    print(subset[0], subset[1])
                    print(f'Support: {result[1]}; Confidence: {subset[2]}; Lift: {subset[3]};')
                    print()
            print()
        second()

        def third():
            from efficient_apriori import apriori

            start = time.perf_counter()
            _, rules = apriori(basket, min_support=third_min_support, min_confidence=third_min_confidence)
            time2 = time.perf_counter() - start
            times.append(time2)

            # noinspection PyShadowingNames
            for i in range(len(rules)):
                print(rules[i])
            print()
        third()

    @staticmethod
    def t3():
        P8.apriori_algorithms(
            P8.data,
            P8.basket,
            P8.times,
            0.001,
            0.89,
            0.001,
            0.9,
            1.0001,
            0.001,
            0.9
        )

    @staticmethod
    def fpgrowth(basket, times, min_sup_ration, min_conf):
        from fpgrowth_py import fpgrowth

        start = time.perf_counter()
        _, rules = fpgrowth(basket, minSupRatio=min_sup_ration, minConf=min_conf)

        time2 = time.perf_counter() - start
        times.append(time2)

        # noinspection PyShadowingNames
        for i in range(len(rules)):
            print(rules[i])
        print()

    @staticmethod
    def t4():
        P8.fpgrowth(P8.basket, P8.times, 0.001, 0.9)

    # noinspection SpellCheckingInspection
    @staticmethod
    def compare_times(times):
        print(times, '\n')
        print('Time for apriori from apriori_python: ', times[0])
        print('Time for apriori from apryori: ', times[1])
        print('Time for apriori from efficient_apriori: ', times[2])
        print('Time for fpgrowth: ', times[3])
        print()

        plt.bar(['apriori_python', 'apryori', 'efficient_apriori', 'fpgrowth'], times)
        plt.show()

    @staticmethod
    def t5():
        P8.compare_times(P8.times)

    @staticmethod
    def t6():
        P8.data2 = pd.read_csv("data.csv")
        print(P8.data2)
        P8.data2.info()
        print()

    # noinspection PyArgumentList
    @staticmethod
    def t7():
        P8.visualize_frequencies(P8.data2)

    @staticmethod
    def t8():
        P8.apriori_algorithms(
            P8.data2,
            P8.basket2,
            P8.times2,
            0.001,
            0.76,
            0.001,
            0.76,
            1.0001,
            0.001,
            0.76
        )

    @staticmethod
    def t9():
        P8.fpgrowth(P8.basket2, P8.times2, 0.001, 0.81)

    @staticmethod
    def t10():
        P8.compare_times(P8.times2)


if __name__ == '__main__':
    for i in range(1, 11):
        getattr(locals().get('P8'), f't{i}')()
