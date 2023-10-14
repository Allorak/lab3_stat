def task1():
    import pandas as pd
    from pathlib import Path

    df = pd.read_csv(Path('data/insurance.csv'))


def task2():
    import pandas as pd
    from pathlib import Path

    df = pd.read_csv(Path('data/insurance.csv'))
    print(df.describe())
    '''
    Метод describe() выводит статистику для каждого столбца таблицы. 
    Например, можно увидеть максимальный возраст человека, среди представленных в исходной таблице - 64.
    Также для каждого столбца отображаются количество, среднее значение, стандартное отклонение, минимум, максимум и три квартиля.
    '''


def task3():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    df = pd.read_csv(Path('data/insurance.csv'))
    df.hist(figsize=(8, 8), edgecolor='black')
    plt.show()
    '''
    Из построенных графиков можно сделать следующие выводы:
    1. Наибольшее количество людей в таблице расположены в возрасте от 18 до 23 лет
    2. У большинства людей нет детей, и чем больше детей в семье, тем меньше подходящих людей 
    3. Индекс массы тела имеет распределение схожее с нормальным 
    4. У большинства людей сравнительно низкие расходы, ниже 7500 тысяч
    '''


def task4():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.stats as sts
    import matplotlib.patches as mpt
    from pathlib import Path

    df = pd.read_csv(Path('data/insurance.csv'))
    mean_bmi = np.mean(df['bmi'])
    mode_bmi = sts.mode(df['bmi'])[0]
    median_bmi = np.median(df['bmi'])

    standard_deviation_bmi = df['bmi'].std()
    range_bmi = df['bmi'].max() - df['bmi'].min()
    iqr_bmi = sts.iqr(df['bmi'], interpolation='midpoint')

    print(f'Среднее (ИМТ) - {mean_bmi}')
    print(f'Мода (ИМТ) - {mode_bmi}')
    print(f'Медиана (ИМТ) - {median_bmi}')
    print(f'Размах (ИМТ) - {range_bmi}')
    print(f'Стандартное отклонение (ИМТ) - {standard_deviation_bmi}')
    print(f'Межквартильный размах  (ИМТ) - {iqr_bmi}')

    df['bmi'].hist(edgecolor='black')
    line_height = 400
    plt.xlabel('Индекс Массы Тела', fontsize=16)
    plt.vlines(x=[mean_bmi], ymin=0, ymax=line_height, color='purple')
    plt.vlines(x=[mode_bmi], ymin=0, ymax=line_height, color='green')
    plt.vlines(x=[median_bmi], ymin=0, ymax=line_height, color='red')

    plt.legend(handles=[mpt.Patch(color='purple', label='Mean'),
                        mpt.Patch(color='green', label='Mode'),
                        mpt.Patch(color='red', label='Median')])
    plt.show()

    mean_charges = np.mean(df['charges'])
    mode_charges = sts.mode(df['charges'])[0]
    median_charges = np.median(df['charges'])

    standard_deviation_charges = df['charges'].std()
    range_charges = df['charges'].max() - df['charges'].min()
    iqr_charges = sts.iqr(df['charges'], interpolation='midpoint')

    print(f'Среднее (Расходы) - {mean_charges}')
    print(f'Мода (Расходы) - {mode_charges}')
    print(f'Медиана (Расходы) - {median_charges}')
    print(f'Размах (Расходы) - {range_charges}')
    print(f'Стандартное отклонение (Расходы) - {standard_deviation_charges}')
    print(f'Межквартильный размах (Расходы) - {iqr_charges}')

    df['charges'].hist(edgecolor='black')
    line_height = 600
    plt.xlabel('Расходы', fontsize=16)
    plt.vlines(x=[mean_charges], ymin=0, ymax=line_height, color='purple')
    plt.vlines(x=[mode_charges], ymin=0, ymax=line_height, color='green')
    plt.vlines(x=[median_charges], ymin=0, ymax=line_height, color='red')

    plt.legend(handles=[mpt.Patch(color='purple', label='Mean'),
                        mpt.Patch(color='green', label='Mode'),
                        mpt.Patch(color='red', label='Median')])
    plt.show()
    '''
    Для индекса массы тела:
    Среднее значение составляет - 30.663
    Мода составляет - 32.3
    Медиана составляет - 30.4
    Размах составляет - 37.17
    Стандартное отклонение составляет - 6.098
    Межквартильный размах составляет - 8.385
    
    Для расходов:
    Среднее значение составляет - 13270.422
    Мода составляет - 1639.563
    Медиана составляет - 9382.033
    Размах составляет - 62648.554
    Стандартное отклонение составляет - 12110.011
    Межквартильный размах составляет - 11879.801
    '''


def task5():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    df = pd.read_csv(Path('data/insurance.csv'))
    _, plots = plt.subplots(2, 2, figsize=(12, 12))
    plots[0, 0].boxplot(df['age'])
    plots[0, 0].set_title('Возраст')

    plots[0, 1].boxplot(df['bmi'])
    plots[0, 1].set_title('ИМТ')

    plots[1, 0].boxplot(df['children'])
    plots[1, 0].set_title('Дети')

    plots[1, 1].boxplot(df['charges'])
    plots[1, 1].set_title('Расходы')

    plt.show()
    '''
    По графику возраста можно наблюдать, что 50% людей выборки находятся в диапазоне от 27 до 50 лет со средним значением около 39
    По графику ИМТ можно наблюдать, что 50% людей выборки находятся в диапазоне 26 до 35, тем не менее присутствует ряд выбросов со значениями больше 47
    По графику количества детей можно наблюдать, что у 50% людей выборки от 0 до 2 детей, а у вторых 50% от 3 до 5
    По графику расходов можно наблюдать, что 50% людей выборки расходы от 4700 до 16600, тем не менее присутствует большое количество выбросов после 34400
    '''


def task6():
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path
    import numpy as np

    df = pd.read_csv(Path('data/insurance.csv'))

    selections = 300
    sample_sizes = [500, 750, 1000, 1250]
    means = []

    for sample_size in sample_sizes:
        for i in range(selections // len(sample_sizes)):
            bmi_sample = df['bmi'].sample(n=sample_size)
            means.append(np.mean(bmi_sample))

        means_df = pd.DataFrame(means)
        means_df.hist(edgecolor='black')
        plt.title(f'Размер выборки - {sample_size}')

        print(f'Размер выборки - {sample_size}')
        print(f'Стандартное отклонение - {means_df.std()[0]}')
        print(f'Среднее - {means_df.mean()[0]}\n')

        plt.show()

        means = []
    '''
    По графикам можно наблюдать что распределения выборочных средних являются нормальными, причем при увеличении размера выборки, рапсределение средних все сильнее приближается к нормальному
    '''


def task7():
    import pandas as pd
    import math
    from pathlib import Path

    df = pd.read_csv(Path('data/insurance.csv'))

    bmi_std = df['bmi'].std()
    bmi_mean = df['bmi'].mean()
    bmi_count = df['bmi'].count()

    charges_std = df['charges'].std()
    charges_mean = df['charges'].mean()
    charges_count = df['charges'].count()

    bmi_std_error = bmi_std / math.sqrt(bmi_count)
    charges_std_error = charges_std / math.sqrt(charges_count)

    bmi_lower_interval_95 = bmi_mean - 1.96 * bmi_std_error
    bmi_upper_interval_95 = bmi_mean + 1.96 * bmi_std_error
    bmi_lower_interval_99 = bmi_mean - 2.58 * bmi_std_error
    bmi_upper_interval_99 = bmi_mean + 2.58 * bmi_std_error

    charges_lower_interval_95 = charges_mean - 1.96 * charges_std_error
    charges_upper_interval_95 = charges_mean + 1.96 * charges_std_error
    charges_lower_interval_99 = charges_mean - 2.58 * charges_std_error
    charges_upper_interval_99 = charges_mean + 2.58 * charges_std_error

    print(f'95% доверительный интервал ИМТ - [{bmi_lower_interval_95:.2f}; {bmi_upper_interval_95:.2f}]')
    print(f'99% доверительный интервал ИМТ - [{bmi_lower_interval_99:.2f}; {bmi_upper_interval_99:.2f}]\n')

    print(f'95% доверительный интервал Расходов - [{charges_lower_interval_95:.2f}; {charges_upper_interval_95:.2f}]')
    print(f'95% доверительный интервал Расходов - [{charges_lower_interval_99:.2f}; {charges_upper_interval_99:.2f}]')


def task8():
    import pandas as pd
    from pathlib import Path
    import scipy.stats as sts
    import seaborn as sns

    df = pd.read_csv(Path('data/insurance.csv'))

    normalized_bmi = (df['bmi']-df['bmi'].min())/(df['bmi'].max()-df['bmi'].min())
    normalized_charges = (df['charges']-df['charges'].min())/(df['charges'].max()-df['charges'].min())

    ks_test_bmi = sts.kstest(normalized_bmi, 'norm')
    ks_test_charges = sts.kstest(normalized_charges, 'norm')

    print(ks_test_bmi)
    print(ks_test_charges)


if __name__ == '__main__':
    # task2()
    # task3()
    # task4()
    # task5()
     task6()
    # task7()
    # task8()
