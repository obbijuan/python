def outer(a, b):
    """Las funciones internas se usan cuando sabes que solo las usaras
    en una funcion en particular y en ninguna otra."""
    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)

outer(1, 2)
