def task9():
    import pandas as pd
    from pathlib import Path

    df = pd.read_csv(Path('data/ECDCCases.csv'))


def task10_12():
    import pandas as pd
    from pathlib import Path

    df = pd.read_csv(Path('data/ECDCCases.csv'))

    print('Количество пропусков в процентах:')
    for column in df.keys():
        missing = df[column].isna().sum() / df[column].size
        print(f'{column} - {missing * 100:.2f}%')

    df = df.drop(columns=df.isna().sum().sort_values()[-2:].index.tolist())
    print(f'\nКоличество пропусков:\n{df.isna().sum()}\n')

    df['countryterritoryCode'] = df['countryterritoryCode'].fillna('other')
    df['popData2019'] = df['popData2019'].fillna(df['popData2019'].median())

    print(f'\nКоличество пропусков после заполнения:\n{df.isna().sum()}')

    ################## ЗАДАНИЕ 11 ##################
    input('\nНажми Enter для задания 11\n')

    deathCount = 3000

    print(df.describe())

    print(f'\nСтраны с количеством смертей за день больше {deathCount}:')
    print(df[df['deaths'] > deathCount]['countriesAndTerritories'].unique())

    print(f'\nКоличество дней с количеством смертей больше {deathCount}:')
    print(len(df[df['deaths'] > deathCount]['dateRep'].unique()))

    ################## ЗАДАНИЕ 12 ##################
    input('\nНажми Enter для задания 12\n')

    df = df.drop_duplicates()
    print(f'Таблица после удаления дубликатов:\n{df.describe()}')

def task13():
    import pandas as pd
    import scipy.stats as sts
    from pathlib import Path

    df = pd.read_csv(Path('data/bmi.csv'))

    northwest = df[df['region'] == 'northwest']
    southwest = df[df['region'] == 'southwest']

    print(f"Нормальность по Шапиро-Уилка для Северо-Западной выборки: {sts.shapiro(northwest['bmi'])}")
    print(f"Нормальность по Шапиро-Уилка для Юго-Западной выборки: {sts.shapiro(southwest['bmi'])}")

    print(f"\nГомогенность по критерию Бартлетта: {sts.bartlett(northwest['bmi'], southwest['bmi'])}")

    print(f"\nt-критерий Стьюдента: {sts.ttest_ind(northwest['bmi'], southwest['bmi'])}")


def task14():
    import pandas as pd
    import scipy.stats as sts

    cube_data = pd.DataFrame([[1, 97, 100],
                              [2, 98, 100],
                              [3, 109, 100],
                              [4, 95, 100],
                              [5, 97, 100],
                              [6, 104, 100]],
                             columns=['Сторона', 'Полученное', 'Ожидаемое'])

    print(f"Критерий Хи-квадрат: {sts.chisquare(cube_data['Полученное'], cube_data['Ожидаемое'])}")


def task15():
    import pandas as pd
    import scipy.stats as sts

    df = pd.DataFrame({'Женат': [89, 17, 11, 43, 22, 1],
                         'Гражданский брак': [80, 22, 20, 35, 6, 4],
                         'Не состоит в отношениях': [35, 44, 35, 6, 8, 22]})

    df.index = ['Полный рабочий день', 'Частичная занятость', 'Временно неработает',
                'На домохозяйстве','На пенсии','Учёба']

    print(f'Данные: {df}\n')

    print(f'Критерий Хи-квадрат: {sts.chi2_contingency(df)}')


if __name__ == '__main__':
    # task9()
    # task10_12()
    # task13()
    # task14()
    task15()
