#!/usr/bin/pythons
# -*- coding: utf-8 -*-


class hola:

    def parse(self, request, rest):
        return None

    def process(self, request):
        html = "<html><body><h1>Hola</h1></body></html>"
        return ("200 OK", html)


class adios:

    def parse(self, request, rest):
        return None

    def process(self, request):
        html = '<html><head><meta charset="UTF-8"></head>' + \
                   '<body><h1>Adios</h1></body></html>'
        return ("200 OK", html)
