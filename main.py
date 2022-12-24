lista_zakupow = {
    "пекарня":['Хліб', 'Пончик', 'Булки'],
    "продуктовий": ['Морква', 'Селера', 'Рукола']
    }
total = 0
print('Список покупок')
lista_zakupow = {
    "пекарня":['Хліб', 'Пончик', 'Булки'],
    "продуктовий": ['Морква', 'Селера', 'Рукола']
    }
total = 0
print('Список покупок')
for shop, product in lista_zakupow.items():
    print(f"Я йду до {shop.capitalize()} і куплю там {product}")
    total = total + len(product)
print(f"Разом купую {total} товарів.")

