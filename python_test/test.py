#!/usr/bin/python

import unittest


def split_bill(price, discount, people):
    """
    divide la cuenta de una mesa
    :param print()rice: precio a dividir
    :param discount: descuento, si no hay descuento el valor es 0.
     el valor representa el porcentaje [0,100]
    :param people: array con numeros de la parte que
     le corresponde a cada persona
    Ej:
    - si dividen 1 plato entre 3 seria [(1/3), (1/3), (1/3)]
    - tambien pueden existir divisiones desiguales:
       3 personas pero 1 de ellas paga la mitad
       [(1/2), (1/4), (1/4)]
    :return: array con el monto a pagar para cada persona
     despues de aplicar el descuento
    Ej:
    monto S/. 20 y people = [(1/2), (1/2)] => [10, 10]
    """
    # Verificacion si el monto es una cantidad valida
    if(price <= 0):
        print "Cantidad incorrecta del Precio"
        return []
    # Verificacion si el array de personas esta vacio
    if(len(people) == 0):
        print "Array vacio de monto a pagar"
        return []
    # Verificacion si la suma de partes es la unidad.
    # Se convierte a string para poder hacer una
    # comparacion muy cercana entre float's
    if(str(sum(people)) != '1.0'):
        print "Las divisiones no coinciden con el monto a pagar."
        return []
    else:
        # Se calcula el porcentaje a pagar sin el descuento
        percent_to_pay = 1 - (discount / 100.0)
        # Se calcla la cantidad que cada persona debe pagar
        res = [round(amount * percent_to_pay * price, 2) for amount in people]
        # Se calcula la cantidad que puede sobrar y/o faltar
        # al realizar el redondeo
        extra = round(price * percent_to_pay, 2) - sum(res)
        # Se le asigna esta cantidad a la primera persona(podria ser random)
        # Por simplicidad se le asigna a la primera persona
        res[0] += extra
        return res


class SplitBillTestCase(unittest.TestCase):
    def setUp(self):
        return

    def test_wrong_split(self):
        s = split_bill(price=149.99,
                       discount=15,
                       people=[(1.0 / 2), (1.0 / 6), (1.0 / 6), (1.0 / 6)])
        s = sum(s)
        self.assertEquals(s, 127.49)

    def test_right_sum(self):
        s = split_bill(price=149.99,
                       discount=15,
                       people=[(1.0 / 7), (2.0 / 7), (1.0 / 7), (3.0 / 7)])
        s = sum(s)
        self.assertEquals(s, 127.49)

    def wrong_sum(self):
        s = split_bill(price=1,
                       discount=0,
                       people=[(1.0 / 10), (1.0 / 10),
                               (1.0 / 10), (1.0 / 10),
                               (1.0 / 10), (1.0 / 10),
                               (1.0 / 10), (1.0 / 10),
                               (1.0 / 10), (1.0 / 10) ])
        s = sum(s)
        self.assertEquals(s, 1.0)

import sys
import getopt


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], 'h', ['help'])
        except getopt.error, msg:
            raise Usage(msg)
        # more code, unchanged
        # print sum([.4, self.5, .1]) == 1
        unittest.main()

    except Usage, err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, 'for help use --help'
        return 2


if __name__ == '__main__':
    sys.exit(main())
