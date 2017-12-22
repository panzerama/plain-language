#!/usr/bin/env python3

import re

class Token:

    def __init__(self, **kwds):
        self.__dict__ = kwds

class Tokenizer:

    terminals = [
        ('define', "\\bdefine\\b"),
        ('end', "\\bend\\b"),
        ('var_sep', ","),
        ('identifier', "\\b[a-zA-Z]+\\b"),
        ('number', "\\b[0-9]+\\b")
    ]

    def __init__(self, file):
        self.code = file.read()

    def tokenize(self):
        tokens = []

        while self.code:
            # print(self.code)
            for token, regex_string in self.terminals:
                reg = re.compile("\\A({})".format(regex_string))
                reg_match = reg.match(self.code)

                if reg_match:
                    token_values = {"token":token, "value":reg_match.group()}
                    current_token = Token(**token_values)
                    tokens.append(current_token)
                    self.code = self.code[reg_match.end():].strip()
                    break

        return tokens

class Parser:

    def __init__(self, token_set):
        self.tokens = token_set

    def parse(self):
        # consume the define keyword
        parse_def()
        # consume the arguments passed into the function
        # consume the body of the function

    def parse_def():
        consume('define')

    def consume(expected_token_type):
        next_token = self.tokens.pop(0)
        if next_token == expected_token_type:
            return next_token
        else:
            raise RuntimeError


    # parse the tree by consuming tokens in the list
    # consume is a function that verifies the token expected is the token found
    # types for nodes like DefineNode, IntegerNode
    # when it comes to parameters, I think I'll need to consume, then peek and
    # see if there's a comma coming. if there is, consume the next as parameter
    # if not, consume the next as the body of the function




def compiler():
    program_file = open("test.plain", 'r')

    tokens = Tokenizer(program_file).tokenize()
    tree = Parser(tokens).parse
    tree.print_tree()

if __name__ == '__main__':
    compiler()
