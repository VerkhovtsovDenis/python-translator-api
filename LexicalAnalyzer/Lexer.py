import re

from .Token import Token
from .TokenType import TOKEN_TYPES_LIST


class Lexer:

    def __init__(self, inpt):
        self.__input = inpt
        self.__input_len = len(inpt)

        self.__line = 0
        self.__pos = 0
        self.__relative_pos = 0

        self.__tokens = []

    def __increment_pos(self, inc=1):
        self.__pos += inc
        self.__relative_pos += inc

    def tokenize(self):
        """Lazy returns tokens"""
        token = self.__next_token()
        while token:
            self.__tokens.append(token)
            yield token
            token = self.__next_token()

    def __next_token(self):
        """Return next token and move pointers"""
        if self.__pos >= self.__input_len:
            return None

        # first, need ignore double spaces
        self.__preprocess()

        # part of the input is analyzing now
        text = self.__input[self.__pos:]

        possible_tokens = []

        # find posiible tokens
        for token_type in TOKEN_TYPES_LIST.values():
            regex = token_type.regex
            result = re.match(regex, text, flags=re.I)

            if result:
                string = result.group(0)
                value = result.group(1)
                token = Token(token_type=token_type,
                              string=string,
                              value=value,
                              line=self.__line,
                              pos=self.__relative_pos)
                possible_tokens.append(token)

        if not possible_tokens:
            raise UnknownTokenException(self.__line, self.__relative_pos)

        # find max token by value lenngth
        # it need because one lexem can match with several tokens

        # in example lexem 'begin_value'
        # it match with keyword token 'begin'
        # and match with id token 'begin_value'
        # so need find the longest of them

        token = max(possible_tokens, key=lambda x: len(x.string))

        self.__postprocess(token)
        return token

    def __preprocess(self):
        """Move the pointer to last whitespace character"""
        if self.__input[self.__pos] not in (' ', '\t'):
            return

        next_pos = self.__pos + 1

        while (next_pos < self.__input_len
               and self.__input[next_pos] in (' ', '\t')):
            next_pos += 1

        inc = next_pos - self.__pos - 1
        self.__increment_pos(inc)

    def __postprocess(self, token):
        """Actions before find token"""
        self.__increment_pos(len(token.string))

        if token.token_type == TOKEN_TYPES_LIST.get('Newline'):
            self.__line += 1
            self.__relative_pos = 0

        # finding errors
        elif token.token_type == TOKEN_TYPES_LIST.get('Number Integer'):
            self.__check_number_integer_token(token)
        elif token.token_type == TOKEN_TYPES_LIST.get('Number Real'):
            self.__check_number_real_token(token)
        elif token.token_type == TOKEN_TYPES_LIST.get('String'):
            self.__check_string_token(token)
        elif token.token_type == TOKEN_TYPES_LIST.get('Id'):
            self.__check_id_token(token)

    def __check_number_integer_token(self, token):
        pass

    def __check_number_real_token(self, token):
        pass

    def __check_string_token(self, token):
        pass

    def __check_id_token(self, token):
        pass


class UnknownTokenException(Exception):
    def __init__(self, line, pos):
        self.line = line
        self.pos = pos

    def __str__(self):
        return f'Unknow token on line: {self.line}, pos: {self.pos}'
