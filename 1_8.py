def task2():
    import pandas as pd

    df = pd.read_csv('data\\insurance.csv')
    print(df.describe())


def task3():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('data\\insurance.csv')
    df.hist(figsize=(8, 8), edgecolor='black')
    plt.show()


def task4():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.stats as sts
    import matplotlib.patches as mpt

    df = pd.read_csv('data\\insurance.csv')
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


def task5():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('data\\insurance.csv')
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


def task6():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('data\\insurance.csv')

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


def task7():
    import pandas as pd
    import matplotlib.pyplot as plt
    import math

    df = pd.read_csv('data\\insurance.csv')

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

    df = pd.read_csv(Path('data/insurance.csv'))


if __name__ == '__main__':
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    task8()
