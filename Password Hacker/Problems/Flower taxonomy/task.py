iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    iris[id_n] = {}
    iris[id_n]['species'] = species
    iris[id_n]['petal_length'] = petal_length
    iris[id_n]['petal_width'] = petal_width
    for key, value in kwargs.items():
        iris[id_n][key] = value
