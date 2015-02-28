#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


class aleatorio:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        randNumber = random.randint(1, 1000000)
        return ('200 OK', "<html><body><h1>Hola." +
                          "<a href=/aleat/" + str(randNumber) + ">" +
                          "Dame otra</a></h1></body></html>")
