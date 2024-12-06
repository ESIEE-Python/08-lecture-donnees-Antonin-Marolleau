"""
aa
"""
#### Imports et définition des variables globales
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, "r", encoding='utf8') as f:
        r = csv.reader(f, delimiter=';')
        l = [[int(num) for num in row] for row in r] # l'itérable est converti en liste

    return l

def get_list_k(data, k):
    """
    caca
    """
    return data[k]

def get_first(l):
    """
    caca
    """
    return int(l[0])

def get_last(l):
    """
    caca
    """
    return int(l[-1])

def get_max(l):
    """
    caca
    """
    return int(max(l))

def get_min(l):
    """
    caca
    """
    return int(min(l))

def get_sum(l):
    """
    caca
    """
    _somme = 0
    longueur = len(l)
    for i in range(longueur):
        _somme = _somme + int(l[i])
    return int(_somme)


#### Fonction principale


def main():
    """
    caca
    """
    #pass
    data = read_data(FILENAME)
    #for i, l in enumerate(data):
    #    print(i, l)
    k = 37
    l = get_list_k(data, 37)
    print(k, l)
    print(get_first(l))
    print(get_last(l))
    print(get_max(l))
    print(get_min(l))
    print(get_sum(l))




if __name__ == "__main__":
    main()
