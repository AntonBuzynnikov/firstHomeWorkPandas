import pandas as pd

df = pd.read_csv('california_housing_test.csv')
print('Самостоятельная практика №1')
print('Количество строк и столбцов')
print(df.shape)

print('Тип данных столбцов')
print(df.dtypes)

print('Проверка на пустые ячейки')
print(df.isnull())

print('Самостоятельная практика №2')
print('Показать median_house_value где median_income < 2')
print(df.loc[df['median_income'] < 2, ['median_house_value']])


print('(Доп) Показать данные в первых 2 столбцах')
print(df[['longitude', 'latitude', ]])


print('(Доп) Выбрать данные где housing_median_age < 20 и median_house_value > 70000')
print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])


print('/n/nОпределить какое максимальное и минимальное значение median_house_value')
print(df['median_house_value'].min())
print(df['median_house_value'].max())

