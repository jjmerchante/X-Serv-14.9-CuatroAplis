#!/usr/bin/python
# -*- coding: utf-8 -*-


class sumador:

    def parse(self, request, rest):
        try:
            num1 = int(rest.split("/")[1])
            num2 = int(rest.split("/")[2])
        except:
            return None
        return (num1, num2)

    def process(self, request):
        if request is None:
            return ("400 Bad Request", "Lo usas mal")

        resultado = str(request[0]) + " + " + str(request[1]) + " = " \
            + str(request[0] + request[1])

        return ('200 OK', "<html><body><p><h1>" + str(resultado) +
                "</h1></p></body></html>")
