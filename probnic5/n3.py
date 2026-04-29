import pandas as pd

# Укажи путь к файлу
path = '/Users/shagal/Downloads/333__1psoe.xlsx'


def solve_3(file_path):
    # Загружаем листы
    df_move = pd.read_excel(file_path, sheet_name='Движение товаров')
    df_prod = pd.read_excel(file_path, sheet_name='Товар')
    df_shop = pd.read_excel(file_path, sheet_name='Магазин')

    # Находим артикул Овсяного молока
    art = df_prod[df_prod['Наименование'] == 'Овсяное молоко']['Артикул'].iloc[0]
    # Находим ID магазинов Первомайского района
    shops = df_shop[df_shop['Район'] == 'Первомайский']['ID магазина'].tolist()

    # Фильтруем движения
    mask = (df_move['Артикул'] == art) & (df_move['ID магазина'].isin(shops)) & \
           (df_move['Дата'] >= '2021-01-01') & (df_move['Дата'] <= '2021-01-10')
    filtered = df_move[mask]

    post = filtered[filtered['Тип операции'] == 'Поступление']['Количество упаковок, шт.'].sum()
    prod = filtered[filtered['Тип операции'] == 'Продажа']['Количество упаковок, шт.'].sum()

    return post - prod

print(solve_3(path))