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

#samat
def samat(string, index1, index2):
    string = str(string)
    sama = string[index1] == string[index2]
    return sama
print(samat("koodari", 1, 2))


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


#poista isot 
def poista_isot(lista):
    karsittu = [i for i in lista if i.isupper() != True]
    return karsittu

print(poista_isot(["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]))


#eniten kirjaimia
def eniten_kirjaimia(string):
    listed = [i for i in string]
    return max(set(listed), key=listed.count)


print(eniten_kirjaimia("abcbdbe"))



puhelin_lista = []
while True:
    komento = int(input("Komento (1 hae, 2 lisää, 3 lopeta): "))
    if komento != 3:
        key = input("nimi: ")
        if komento == 2:
            value = input("numero: ")
            print("ok!")
            puhelin_lista.append({key: value})




        elif komento == 1:
            [print(item[key]) for item in puhelin_lista if key in item]
    else:
        print("lopetetaan..")
        break










