# Parilliset

random_list = []
def parilliset(lista):
    for number in lista:
        if number % 2 == 0:
            random_list.append(number)
    print(f"Alkuperäinen: {lista}")
    print(f"Parilliset: {random_list}")

parilliset([1, 2, 3, 4, 5, 6])


# Uniikki
def uniikki(lista):
    updated_lista = set(lista)
    updated_set = list(updated_lista)
    print(updated_set)

uniikki([1, 2, 3, 4, 4, 2])






