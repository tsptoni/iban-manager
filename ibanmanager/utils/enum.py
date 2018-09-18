# -*- coding: utf-8 -*-

from __future__ import absolute_import

from model_utils import Choices

class DumbEnum(Choices):

    def to_json_list(self):
        result = []

        for (k,v) in self.__iter__():
            if v[0].isupper():
                keyval = {'id': k,
                          'text': v}

                result.append(keyval)

        return result


    def to_dictionary_list(self):
        result = []
        for k, v in self.__iter__():
            result.append('{{"i": "{}", "text": "{}"}}, '.format(k, v))

        return result
