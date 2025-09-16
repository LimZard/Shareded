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

# Palindromi
palindromi = input("Anna palindromi: ")


while palindromi != palindromi[::-1]:
    print("ei ollut palindromi")
    palindromi = input("Anna palindromi: ")

print(f"{palindromi} on palindromi")


# positiiviset summat
def positiivisten_summa(lista):
    positiiviset = [i for i in lista if i > 0]
    print(sum(positiiviset))

positiivisten_summa([1, -2, 3, -4, 5])


# summalista
def summa(list1, list2):
    sum = [x + y for x, y in zip(list1, list2)]
    return sum

# kaikki väärinpäin 
def kaikki_vaarinpain(lista):
    lista.reverse()
    reverse = [i[::-1] for i in lista]
    print(reverse)

kaikki_vaarinpain(["moi", "moiioi", "hsjad"])





