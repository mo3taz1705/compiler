###############################################################################
#                                                                             #
#  LEXER                                                                      #
#                                                                             #
###############################################################################
from collections import OrderedDict

register_id = 0
label_id = 1
line_no = 1
out_file = None
newLine_pos = None

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER_TYPE = 'INTEGER_TYPE'
INTEGER_VALUE = 'INTEGER_VALUE'
CONSTANT = 'CONSTANT'
IF = 'IF'
ELSE = 'ELSE'
FOR = 'FOR'
WHILE = 'WHILE'
DO = 'DO'
SWITCH = 'SWITCH'
CASE = 'CASE'
BREAK = 'BREAK'
DEFAULT = 'DEFAULT'
TRUE = 'TRUE'
FALSE = 'FALSE'
AND = 'AND'
OR = 'OR'
NOT = 'NOT'
EQUAL = 'EQUAL'
NOT_EQUAL = 'NOT_EQUAL'
LESS_EQUAL = 'LESS_EQUAL'
GREATER_EQUAL = 'GREATER_EQUAL'
LESS = 'LESS'
GREATER = 'GREATER'
COLON = 'COLON'
COMMA = 'COMMA'
ASSIGN = 'ASSIGN'
SEMI_COLON = 'SEMI_COLON'
L_PAREN = 'L_PAREN'  # (
R_PAREN = 'R_PAREN'  # )
L_BRACE = 'L_BRACE'  # {
R_BRACE = 'R_BRACE'  # }
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
ID = 'ID'
EOF = 'EOF'


def locations_of_substring(string, substring):
    """Return a list of locations of a substring."""

    substring_length = len(substring)

    def recurse(locations_found, start):
        location = string.find(substring, start)
        if location != -1:
            return recurse(locations_found + [location], location + substring_length)
        else:
            return locations_found

    return recurse([], 0)


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


RESERVED_KEYWORDS = {
    'int': Token(INTEGER_TYPE, INTEGER_TYPE),
    'const': Token(CONSTANT, CONSTANT),
    'if': Token(IF, IF),
    'else': Token(ELSE, ELSE),
    'for': Token(FOR, FOR),
    'while': Token(WHILE, WHILE),
    'do': Token(DO, DO),
    'switch': Token(SWITCH, SWITCH),
    'case': Token(CASE, CASE),
    'break': Token(BREAK, BREAK),
    'default': Token(DEFAULT, DEFAULT),
    'true': Token(TRUE, TRUE),
    'false': Token(FALSE, FALSE),
    'and': Token(AND, AND),
    'or': Token(OR, OR),
    'not': Token(NOT, NOT)
}


class Lexer(object):
    def __init__(self, text, warn_file, error_file):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.error_file = error_file
        self.warn_file = warn_file

    def error(self):
        self.error_file.write('Lexical Error: Invalid character at line: ' + str(line_no) + '\n')
        raise Exception('Lexical Error: Invalid character at line: ' + str(line_no))

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        global line_no
        if len(newLine_pos) > 0 and self.pos > newLine_pos[0]:
            line_no = line_no + 1
            del newLine_pos[0]
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos > len(self.text) - 1:
            return None
        else:
            return self.text[peek_pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        self.advance()  # the starting hash
        while self.current_char != '#':
            self.advance()
        self.advance()  # the closing hash

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        token = Token(INTEGER_VALUE, int(result))
        return token

    def _id(self):
        """Handle identifiers and reserved keywords"""
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()

        token = RESERVED_KEYWORDS.get(result, Token(ID, result))
        return token

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == '#':
                self.skip_comment()
                continue

            if self.current_char.isalpha():
                return self._id()

            if self.current_char.isdigit():
                return self.integer()

            if self.current_char == '=' and self.peek() == '=':  # EQUAL
                self.advance()
                self.advance()
                return Token(EQUAL, '==')

            if self.current_char == '!' and self.peek() == '=':  # NOT_EQUAL
                self.advance()
                self.advance()
                return Token(NOT_EQUAL, '!=')

            if self.current_char == '<' and self.peek() == '=':  # LESS_EQUAL
                self.advance()
                self.advance()
                return Token(LESS_EQUAL, '<=')

            if self.current_char == '>' and self.peek() == '=':  # GREATER_EQUAL
                self.advance()
                self.advance()
                return Token(GREATER_EQUAL, '>=')

            if self.current_char == '<':  # LESS
                self.advance()
                return Token(LESS, '<')

            if self.current_char == '>':  # GREATER
                self.advance()
                return Token(GREATER, '>')

            if self.current_char == ':':  # COLON
                self.advance()
                return Token(COLON, ':')

            if self.current_char == ',':  # COMMA
                self.advance()
                return Token(COMMA, ',')

            if self.current_char == '=':  # ASSIGN
                self.advance()
                return Token(ASSIGN, '=')

            if self.current_char == ';':  # SEMI_COLON
                self.advance()
                return Token(SEMI_COLON, ';')

            if self.current_char == '(':  # L_PAREN
                self.advance()
                return Token(L_PAREN, '(')

            if self.current_char == ')':  # R_PAREN
                self.advance()
                return Token(R_PAREN, ')')

            if self.current_char == '{':  # L_BRACE
                self.advance()
                return Token(L_BRACE, '{')

            if self.current_char == '}':  # R_BRACE
                self.advance()
                return Token(R_BRACE, '}')

            if self.current_char == '+':  # PLUS
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':  # MINUS
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':  # MULTIPLY
                self.advance()
                return Token(MULTIPLY, '*')

            if self.current_char == '/':  # DIVIDE
                self.advance()
                return Token(DIVIDE, '/')

            self.error()

        return Token(EOF, None)


###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################

boolean_e = []


class AST(object):  # parent node, abstract syntax tree
    pass


# BASIC NODES
class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Number(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Boolean(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr


class Compound(AST):
    def __init__(self):
        self.children = []


class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Var(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Program(AST):
    def __init__(self):
        self.children = []


class NoOp(AST):
    pass


class SwitchStat(AST):
    def __init__(self, var, case_stats, cmpd_stats):
        self.var = var
        self.case_stats = case_stats
        self.cmpd_stats = cmpd_stats


class VarDecl(AST):
    def __init__(self, var, type, exp, isConst):
        self.left = var
        self.var_type = type
        self.right = exp
        self.isConst = isConst


class IfStat(AST):
    def __init__(self, expr, cmpd1, cmpd2):
        self.expr = expr
        self.cmpd1 = cmpd1
        self.cmpd2 = cmpd2


class WhileStat(AST):
    def __init__(self, expr, cmpd):
        self.expr = expr
        self.cmpd1 = cmpd


class DoWhileStat(AST):
    def __init__(self, expr, cmpd):
        self.expr = expr
        self.cmpd1 = cmpd


class BoolOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class ForStat(AST):
    def __init__(self, init, middle, end, cmpd_stat):
        self.init = init
        self.middle = middle
        self.end = end
        self.cmpd_stat = cmpd_stat


class BreakStat(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Type(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Parser(object):
    def __init__(self, lexer, warn_file, error_file):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()
        self.error_file = error_file
        self.warn_file = warn_file

    def error(self):
        self.error_file.write('Syntax Error: Invalid syntax at line: ' + str(line_no) + '\n')
        raise Exception('Syntax Error: Invalid syntax at line: ' + str(line_no))

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    # Grammar
    def variable(self):
        """
        variable : ID
        """
        token = self.current_token
        self.eat(ID)
        node = Var(token)
        return node

    def type_spec(self):
        """
        type_spec : INTEGER_TYPE
        """
        token = self.current_token
        self.eat(INTEGER_TYPE)
        node = Type(token)
        return node

    def program(self):
        """
        program : statement_list
        """
        nodes = self.statement_list()
        root = Program()
        for node in nodes:
            root.children.append(node)
        return root

    def statement_list(self):
        """
        statement_list : statement
                       | statement statement_list
        """
        node = self.statement()
        results = [node]

        while self.current_token.type in (BREAK, IF, SWITCH, WHILE, DO, FOR, ID, INTEGER_TYPE, CONSTANT, SEMI_COLON):
            results.append(self.statement())

        return results

    def statement(self):
        """
        statement : BREAK SEMI_COLON
                  | selection_statement
                  | iteration_statement
                  | assignment_statement SEMI_COLON
                  | declaration_statement SEMI_COLON
                  | const_statement SEMI_COLON
                  | SEMI_COLON
        """
        node = NoOp()
        if self.current_token.type == BREAK:
            node = BreakStat()
        elif self.current_token.type in (IF, SWITCH):
            node = self.selection_statement()
        elif self.current_token.type in (WHILE, DO, FOR):
            node = self.iteration_statement()
        elif self.current_token.type == ID:
            node = self.assignment_statement()
            self.eat(SEMI_COLON)
        elif self.current_token.type in (INTEGER_TYPE):
            node = self.variable_declaration()
            self.eat(SEMI_COLON)
        elif self.current_token.type == CONSTANT:
            node = self.const_declaration()
            self.eat(SEMI_COLON)
        elif self.current_token.type == SEMI_COLON:
            self.eat(SEMI_COLON)

        return node

    def init_for(self):
        """
        init_for : assignment_statement
                 | declaration_statement
        """
        node = NoOp()
        if self.current_token.type == ID:
            node = self.assignment_statement()
        elif self.current_token.type == INTEGER_TYPE:
            node = self.variable_declaration()
        return node

    def compound_statement(self):
        """
        compound_statement: L_BRACE statement_list R_BRACE
                          | L_BRACE R_BRACE
        """
        nodes = []
        self.eat(L_BRACE)
        if self.current_token.type in (BREAK, IF, SWITCH, WHILE, DO, FOR, ID, INTEGER_TYPE, CONSTANT, SEMI_COLON):
            nodes = self.statement_list()
        self.eat(R_BRACE)

        root = Compound()
        for node in nodes:
            root.children.append(node)

        return root

    def assignment_statement(self):
        """
        assignment_statement : variable ASSIGN expr
        """
        left = self.variable()
        token = self.current_token
        self.eat(ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    def selection_statement(self):
        """
        selection_statement : IF L_PAREN boolean_expression R_PAREN compound_statement
                            | IF L_PAREN boolean_expression R_PAREN compound_statement ELSE compound_statement
                            | SWITCH L_PAREN variable R_PAREN L_BRACE (CASE (INTEGER_VALUE | MINUS INTEGER_VALUE) COLON compound_statement)+ (DEFAULT COLON compound_statement) R_BRACE
        """
        node = NoOp()
        global boolean_e
        if self.current_token.type == IF:
            self.eat(IF)
            self.eat(L_PAREN)
            boolean_e.append(self.boolean_expression())
            self.eat(R_PAREN)
            self.cmpd_stat1 = self.compound_statement()
            self.cmpd_stat2 = None
            if self.current_token.type == ELSE:
                self.eat(ELSE)
                self.cmpd_stat2 = self.compound_statement()
            node = IfStat(boolean_e[-1], self.cmpd_stat1, self.cmpd_stat2)
            del boolean_e[-1]
            return node
        elif self.current_token.type == SWITCH:
            self.eat(SWITCH)
            self.eat(L_PAREN)
            self.var = self.variable()
            self.eat(R_PAREN)
            self.eat(L_BRACE)
            self.eat(CASE)
            self.case_stats = []
            self.cmpd_stats = []
            if self.current_token.type == INTEGER_VALUE:
                num_token = self.current_token
                self.eat(INTEGER_VALUE)
                self.eat(COLON)
                self.cmpd_stats.append(self.compound_statement())
                self.case_stats.append(Number(num_token))
            elif self.current_token.type == MINUS:
                minus_token = self.current_token
                self.eat(MINUS)
                num_token = self.current_token
                self.eat(INTEGER_VALUE)
                self.eat(COLON)
                self.cmpd_stats.append(self.compound_statement())
                self.case_stats.append(UnaryOp(minus_token, Number(num_token)))
            while self.current_token.type == CASE:
                self.eat(CASE)
                if self.current_token.type == INTEGER_VALUE:
                    num_token = self.current_token
                    self.eat(INTEGER_VALUE)
                    self.eat(COLON)
                    self.cmpd_stats.append(self.compound_statement())
                    self.case_stats.append(Number(num_token))
                elif self.current_token.type == MINUS:
                    minus_token = self.current_token
                    self.eat(MINUS)
                    num_token = self.current_token
                    self.eat(INTEGER_VALUE)
                    self.eat(COLON)
                    self.cmpd_stats.append(self.compound_statement())
                    self.case_stats.append(UnaryOp(minus_token, Number(num_token)))
            if self.current_token.type == DEFAULT:
                default_token = self.current_token
                self.eat(DEFAULT)
                self.eat(COLON)
                self.cmpd_stats.append(self.compound_statement())
                self.case_stats.append(default_token)
            self.eat(R_BRACE)
            node = SwitchStat(self.var, self.case_stats, self.cmpd_stats)
            return node

    def iteration_statement(self):
        """
        iteration_statement : WHILE L_PAREN boolean_expression R_PAREN compound_statement
                            | DO compound_statement WHILE L_PAREN boolean_expression R_PAREN SEMI_COLON
                            | FOR L_PAREN init_for SEMI_COLON boolean_expression SEMI_COLON assignment_statement R_PAREN compound_statement
        """
        node = NoOp()
        if self.current_token.type == WHILE:
            self.eat(WHILE)
            self.eat(L_PAREN)
            bool_expr = self.boolean_expression()
            self.eat(R_PAREN)
            self.cmpd_stat = self.compound_statement()
            node = WhileStat(bool_expr, self.cmpd_stat)
            return node
        elif self.current_token.type == DO:
            self.eat(DO)
            self.cmpd_stat = self.compound_statement()
            self.eat(WHILE)
            self.eat(L_PAREN)
            bool_expr = self.boolean_expression()
            self.eat(R_PAREN)
            self.eat(SEMI_COLON)
            node = DoWhileStat(bool_expr, self.cmpd_stat)
            return node
        elif self.current_token.type == FOR:
            self.eat(FOR)
            self.eat(L_PAREN)
            self.init = self.init_for()
            self.eat(SEMI_COLON)
            self.middle = self.boolean_expression()
            self.eat(SEMI_COLON)
            self.end = self.assignment_statement()
            self.eat(R_PAREN)
            self.cmpd_stat = self.compound_statement()
            node = ForStat(self.init, self.middle, self.end, self.cmpd_stat)
            return node

    def variable_declaration(self):
        """
        variable_declaration : TYPE variable ASSIGN expr
                             | TYPE variable
        """
        type_node = self.type_spec()
        var_node = self.variable()

        if self.current_token.type == ASSIGN:
            self.eat(ASSIGN)
            expr_node = self.expr()
        else:
            expr_node = None

        var_declaration = VarDecl(var_node, type_node, expr_node, False)

        return var_declaration

    def const_declaration(self):
        """
        const_declaration : CONSTANT TYPE variable ASSIGN expr
        """
        self.eat(CONSTANT)
        type_node = self.type_spec()
        var_node = self.variable()
        self.eat(ASSIGN)
        expr_node = self.expr()

        var_declaration = VarDecl(var_node, type_node, expr_node, True)

        return var_declaration

    def empty(self):
        """An empty production"""
        return NoOp()

    def expr(self):
        """
        expr : term ((PLUS | MINUS) term)*
        """
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def term(self):
        """
        term : factor ((MULTIPLY | DIVIDE) factor)*
        """
        node = self.factor()

        while self.current_token.type in (MULTIPLY, DIVIDE):
            token = self.current_token
            if token.type == MULTIPLY:
                self.eat(MULTIPLY)
            elif token.type == DIVIDE:
                self.eat(DIVIDE)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def factor(self):
        """
        factor : PLUS factor
               | MINUS factor
               | INTEGER_VALUE
               | LPAREN expr RPAREN
               | variable
        """
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == MINUS:
            self.eat(MINUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == INTEGER_VALUE:
            self.eat(INTEGER_VALUE)
            return Number(token)
        elif token.type == L_PAREN:
            self.eat(L_PAREN)
            node = self.expr()
            self.eat(R_PAREN)
            return node
        else:
            node = self.variable()
            return node

    def boolean_expression(self):
        """
        boolean_expression : boolean_term (relation boolean_term)*
        """
        node = self.boolean_term()

        while self.current_token.type in (AND, OR, NOT, EQUAL, NOT_EQUAL, LESS_EQUAL, GREATER_EQUAL, LESS, GREATER):
            token = self.current_token
            if token.type == AND:
                self.eat(AND)
            elif token.type == OR:
                self.eat(OR)
            elif token.type == NOT:
                self.eat(NOT)
            elif token.type == EQUAL:
                self.eat(EQUAL)
            elif token.type == NOT_EQUAL:
                self.eat(NOT_EQUAL)
            elif token.type == LESS_EQUAL:
                self.eat(LESS_EQUAL)
            elif token.type == GREATER_EQUAL:
                self.eat(GREATER_EQUAL)
            elif token.type == LESS:
                self.eat(LESS)
            elif token.type == GREATER:
                self.eat(GREATER)

            node = BoolOp(left=node, op=token, right=self.boolean_term())

        return node

    def boolean_term(self):
        """
        boolean_term : NOT boolean_term
                     | TRUE
                     | FALSE
                     | L_PAREN boolean_expression R_PAREN
        """
        token = self.current_token
        if token.type == NOT:
            self.eat(NOT)
            node = UnaryOp(token, self.boolean_term)
            return node
        elif token.type == TRUE:
            self.eat(TRUE)
            return Boolean(token)
        elif token.type == FALSE:
            self.eat(FALSE)
            return Boolean(token)
        elif token.type == L_PAREN:
            self.eat(L_PAREN)
            node = self.boolean_expression()
            self.eat(R_PAREN)
            return node
        elif token.type == INTEGER_VALUE:
            self.eat(INTEGER_VALUE)
            return Number(token)
        else:
            node = self.variable()
            return node

    def parse(self):
        node = self.program()
        if self.current_token.type != EOF:
            self.error()

        return node


class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


###############################################################################
#                                                                             #
#  Semantic Analyzer                                                          #
#                                                                             #
###############################################################################
class Symbol(object):
    def __init__(self, name, type=None):
        self.name = name
        self.type = type


class BuiltInSymbol(Symbol):
    def __init__(self, name):
        super(BuiltInSymbol, self).__init__(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<{class_name}(name='{name}')>".format(
            class_name=self.__class__.__name__,
            name=self.name,
        )


class VarSymbol(Symbol):
    def __init__(self, name, type):
        super(VarSymbol, self).__init__(name, type)

    def __str__(self):
        return "<{class_name}(name='{name}', type='{type}')>".format(
            class_name=self.__class__.__name__,
            name=self.name,
            type=self.type,
        )

    __repr__ = __str__


class WhileSymbol(Symbol):
    def __init__(self, name, ):
        super(WhileSymbol, self).__init__(name)

    def __str__(self):
        return '<{class_name}(name={name})>'.format(
            class_name=self.__class__.__name__,
            name=self.name,
        )

    __repr__ = __str__


class IfSymbol(Symbol):
    def __init__(self, name, ):
        super(IfSymbol, self).__init__(name)

    def __str__(self):
        return '<{class_name}(name={name})>'.format(
            class_name=self.__class__.__name__,
            name=self.name,
        )

    __repr__ = __str__


class DoWhileSymbol(Symbol):
    def __init__(self, name, ):
        super(DoWhileSymbol, self).__init__(name)

    def __str__(self):
        return '<{class_name}(name={name})>'.format(
            class_name=self.__class__.__name__,
            name=self.name,
        )

    __repr__ = __str__


class ForSymbol(Symbol):
    def __init__(self, name, ):
        super(ForSymbol, self).__init__(name)

    def __str__(self):
        return '<{class_name}(name={name})>'.format(
            class_name=self.__class__.__name__,
            name=self.name,
        )

    __repr__ = __str__


class ScopedSymbolTable(object):
    def __init__(self, scope_name, scope_level, enclosing_scope=None):
        self._symbols = OrderedDict()
        self.scope_name = scope_name
        self.scope_level = scope_level
        self.enclosing_scope = enclosing_scope
        self.symtable_file = open('symtable.txt', 'a+')

    def _init_builtins(self):
        self.insert(BuiltInSymbol('INTEGER'))
        self.insert(BuiltInSymbol('REAL'))

    def insert(self, symbol):
        # print('Insert: %s' % symbol.name)
        self._symbols[symbol.name] = symbol

    def lookup(self, name, current_scope_only=False):
        # print('Lookup: %s. (Scope name: %s)' % (name, self.scope_name))
        # 'symbol' is either an instance of the Symbol class or None
        symbol = self._symbols.get(name)

        if symbol is not None:
            return symbol

        if current_scope_only:
            return None

        # recursively go up the chain and lookup the name
        if self.enclosing_scope is not None:
            return self.enclosing_scope.lookup(name)

    def __str__(self):
        h1 = 'SCOPE (SCOPED SYMBOL TABLE)'
        lines = ['\n', h1, '=' * len(h1)]
        for header_name, header_value in (
                ('Scope name', self.scope_name),
                ('Scope level', self.scope_level),
                ('Enclosing scope',
                 self.enclosing_scope.scope_name if self.enclosing_scope else None
                 )
        ):
            lines.append('%-15s: %s' % (header_name, header_value))
        h2 = 'Scope (Scoped symbol table) contents'
        lines.extend([h2, '-' * len(h2)])
        lines.extend(
            ('%7s: %r' % (key, value))
            for key, value in self._symbols.items()
        )
        lines.append('\n')
        s = '\n'.join(lines)
        self.write_file()
        return s

    def write_file(self):
        for key, _ in self._symbols.items():
            self.symtable_file.write(
                "{}\t{}\t{}\t{}\n".format(key, self.scope_name, self.scope_level,
                                          self.enclosing_scope.scope_name if self.enclosing_scope else None))

    __repr__ = __str__


class SemanticAnalyzer(NodeVisitor):
    def __init__(self, warn_file, error_file):
        self.current_scope = None
        self.warn_file = warn_file
        self.error_file = error_file

    def visit_Program(self, node):
        print('ENTER scope: global')
        global_scope = ScopedSymbolTable(
            scope_name='global',
            scope_level=1,
            enclosing_scope=self.current_scope,  # None
        )
        global_scope._init_builtins()
        self.current_scope = global_scope

        for child in node.children:
            self.visit(child)

        print(global_scope)

        self.current_scope = self.current_scope.enclosing_scope
        print('LEAVE scope: global')

    def visit_VarDecl(self, node):
        type_name = node.var_type.value
        # bring the type from the scope
        type_symbol = self.current_scope.lookup(type_name)
        var_name = node.left.value
        var_symbol = VarSymbol(var_name, type_symbol)
        if self.current_scope.lookup(var_name, current_scope_only=True):
            self.warn_file.write("Warning: Duplicate identifier {} found\n".format(var_name))
            # raise Exception("Warning: Duplicate identifier {} found".format(var_name))
        self.current_scope.insert(var_symbol)
        if node.right is not None:
            self.visit(node.right)

    def visit_Type(self, node):
        # Do nothing
        pass

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_Number(self, node):
        pass

    def visit_UnaryOp(self, node):
        self.visit(node.expr)

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node):
        var_name = node.left.value
        if var_name is not None:
            var_symbol = self.current_scope.lookup(var_name)
            if var_symbol is None:
                self.error_file.write("Variable {} is not defined\n".format(var_name))
                raise Exception("Variable {} is not defined".format(var_name))

    def visit_Var(self, node):
        var_name = node.value
        if var_name is not None:
            var_value = self.current_scope.lookup(var_name)
            if var_value is None:
                self.error_file.write("Variable {} is not defined\n".format(var_name))
                raise Exception("Variable {} is not defined".format(var_name))

    def visit_NoOp(self, node):
        pass

    def visit_Boolean(self, node):
        pass

    def visit_SwitchStat(self, node):
        var_name = node.var.value
        if var_name is not None:
            var_value = self.current_scope.lookup(var_name)
            if var_value is None:
                self.error_file.write("Variable {} is not defined\n".format(var_name))
                raise Exception("Variable {} is not defined".format(var_name))
        else:
            self.warn_file.write("No Variable is for switch\n".format(var_name))
            raise Exception("No Variable is for switch".format(var_name))
        for i, case in enumerate(node.case_stats):
            cmpd = node.cmpd_stats[i]
            self.visit(cmpd)

    def visit_IfStat(self, node):
        if_symbol = IfSymbol(IF)
        self.current_scope.insert(if_symbol)
        print('ENTER scope: {}'.format(IF))
        # Scope for parameters and local variables
        if_scope = ScopedSymbolTable(
            scope_name=IF,
            scope_level=self.current_scope.scope_level + 1,
            enclosing_scope=self.current_scope
        )
        self.current_scope = if_scope

        self.visit(node.expr)
        self.visit(node.cmpd1)
        if node.cmpd2 is not None:
            self.visit(node.cmpd1)

        print(if_scope)

        self.current_scope = self.current_scope.enclosing_scope
        print('LEAVE scope: {}'.format(IF))

    def visit_WhileStat(self, node):
        while_symbol = WhileSymbol(WHILE)
        self.current_scope.insert(while_symbol)
        print('ENTER scope: {}'.format(WHILE))
        # Scope for parameters and local variables
        while_scope = ScopedSymbolTable(
            scope_name=WHILE,
            scope_level=self.current_scope.scope_level + 1,
            enclosing_scope=self.current_scope
        )
        self.current_scope = while_scope

        self.visit(node.expr)
        self.visit(node.cmpd1)

        print(while_scope)
        self.current_scope = self.current_scope.enclosing_scope
        print('LEAVE scope: {}'.format(WHILE))

    def visit_DoWhileStat(self, node):
        do_while_symbol = DoWhileSymbol('Do..While')
        self.current_scope.insert(do_while_symbol)
        print('ENTER scope: {}'.format('Do..While'))
        # Scope for parameters and local variables
        do_while_scope = ScopedSymbolTable(
            scope_name='Do..While',
            scope_level=self.current_scope.scope_level + 1,
            enclosing_scope=self.current_scope
        )
        self.current_scope = do_while_scope

        self.visit(node.cmpd1)
        self.visit(node.expr)

        print(do_while_scope)
        self.current_scope = self.current_scope.enclosing_scope
        print('LEAVE scope: {}'.format('Do..While'))

    def visit_ForStat(self, node):
        do_while_symbol = ForSymbol(FOR)
        self.current_scope.insert(do_while_symbol)
        print('ENTER scope: {}'.format(FOR))
        # Scope for parameters and local variables
        for_scope = ScopedSymbolTable(
            scope_name=FOR,
            scope_level=self.current_scope.scope_level + 1,
            enclosing_scope=self.current_scope
        )
        self.current_scope = for_scope

        var_name = self.visit(node.init)
        var_value = self.current_scope.lookup(var_name)
        if var_value is None:
            self.error_file.write("Variable {} is not defined\n".format(var_name))
            raise Exception("Variable {} is not defined".format(var_name))

        self.visit(node.middle)
        self.visit(node.cmpd_stat)
        self.visit(node.end)

        print(for_scope)
        self.current_scope = self.current_scope.enclosing_scope
        print('LEAVE scope: {}'.format(FOR))

    def visit_BoolOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_BreakStat(self, node):
        pass


###############################################################################
#                                                                             #
#  INTERPRETER                                                                #
#                                                                             #
###############################################################################
class Interpreter(NodeVisitor):
    def __init__(self, tree, warn_file, error_file):
        self.tree = tree
        self.GLOBAL_SCOPE = OrderedDict()
        self.error_file = error_file
        self.warn_file = warn_file

    def visit_Program(self, node):
        for child in node.children:
            self.visit(child)

    def visit_VarDecl(self, node):
        var_name = node.left.value
        if node.right:
            value = self.visit(node.right)
            self.GLOBAL_SCOPE[var_name] = value
            out_file.write("(=, " + str(value) + ", , " + str(var_name) + ")\n")

    def visit_Type(self, node):
        # Do nothing
        pass

    def visit_BinOp(self, node):
        global register_id
        if node.op.type == PLUS:
            # value = self.visit(node.left) + self.visit(node.right)
            left_val = str(self.visit(node.left))
            right_val = str(self.visit(node.right))
            destination_register = 'R' + str(register_id)
            out_file.write('(+, ' + left_val + ', ' + right_val + ', ' + destination_register + ')\n')
            register_id = register_id + 1
            return destination_register
        elif node.op.type == MINUS:
            # value = self.visit(node.left) - self.visit(node.right)
            left_val = str(self.visit(node.left))
            right_val = str(self.visit(node.right))
            destination_register = 'R' + str(register_id)
            out_file.write('(-, ' + left_val + ', ' + right_val + ', ' + destination_register + ')\n')
            register_id = register_id + 1
            return destination_register
        elif node.op.type == MULTIPLY:
            # value = self.visit(node.left) * self.visit(node.right)
            left_val = str(self.visit(node.left))
            right_val = str(self.visit(node.right))
            destination_register = 'R' + str(register_id)
            out_file.write('(*, ' + left_val + ', ' + right_val + ', ' + destination_register + ')\n')
            register_id = register_id + 1
            return destination_register
        elif node.op.type == DIVIDE:
            # value = self.visit(node.left) / self.visit(node.right)
            left_val = str(self.visit(node.left))
            right_val = str(self.visit(node.right))
            destination_register = 'R' + str(register_id)
            out_file.write('(/, ' + left_val + ', ' + right_val + ', ' + destination_register + ')\n')
            register_id = register_id + 1
            return destination_register

    def visit_Number(self, node):
        return str(node.value)

    def visit_UnaryOp(self, node):
        global register_id
        op = node.op.type
        if op == PLUS:
            return '' + str(self.visit(node.expr))
        elif op == MINUS:
            # return '-' + str(self.visit(node.expr))
            value = str(self.visit(node.expr))
            destination_register = 'R' + str(register_id)
            out_file.write('(uminus, ' + value + ', , ' + destination_register + ')\n')
            register_id = register_id + 1
            return destination_register

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node):
        global register_id
        var_name = node.left.value
        # self.GLOBAL_SCOPE[var_name] = self.visit(node.right)
        value = self.visit(node.right)

        # out_file.write('(=, ' + str(var_name) + ', ' + str(self.visit(node.right)) + ', R' + str(register_id) + ')\n')
        out_file.write("(=, " + str(value) + ", , " + str(var_name) + ")\n")
        # register_id = register_id + 1
        # return 'R' + str(register_id - 1)

    def visit_Var(self, node):
        var_name = node.value
        var_value = self.GLOBAL_SCOPE.get(var_name)
        if var_value is None:
            self.error_file.write("Name Error {}\n".format(repr(var_name)))
            raise NameError(repr(var_name))
        else:
            return str(var_name)

    def visit_NoOp(self, node):
        return ""

    def visit_Boolean(self, node):
        return str(node.value)

    def visit_SwitchStat(self, node):
        global register_id, label_id
        v = str(node.var.value)
        for i, case in enumerate(node.case_stats):
            cmpd = node.cmpd_stats[i]
            my_label = label_id
            label_id = label_id + 1
            out_file.write('L' + str(my_label) + ':\n')
            if not (str(case.value) == 'DEFAULT'):
                destination_register = 'R' + str(register_id)
                out_file.write('(equal, ' + v + ', ' + str(case.value) + ', ' + destination_register + ')\n')
                register_id = register_id + 1
                out_file.write('(jfalse, L' + str(label_id) + ', ' + destination_register + ', )\n')
            self.visit(cmpd)

    def visit_IfStat(self, node):
        global register_id, label_id
        value = str(self.visit(node.expr))
        my_label = label_id
        label_id = label_id + 1
        out_file.write('(jfalse, L' + str(my_label) + ', ' + value + ', )\n')
        value = str(self.visit(node.cmpd1))
        if node.cmpd2 is not None:
            my_label = label_id
            label_id = label_id + 1
            out_file.write('(jmp, L' + str(my_label) + ', , )\n')
            value = str(self.visit(node.cmpd1))
        out_file.write('L' + str(my_label) + ':\n')

    def visit_WhileStat(self, node):
        global register_id, label_id
        my_label1 = label_id
        label_id = label_id + 1
        out_file.write('L' + str(my_label1) + ':\n')
        cond = str(self.visit(node.expr))
        my_label2 = label_id
        label_id = label_id + 1
        out_file.write('(jfalse, L' + str(my_label2) + ', ' + cond + ', )\n')
        val = str(self.visit(node.cmpd1))
        out_file.write('(jmp, L' + str(my_label1) + ', , )\n')
        out_file.write('L' + str(my_label2) + ':\n')

    def visit_DoWhileStat(self, node):
        global register_id, label_id
        my_label1 = label_id
        label_id = label_id + 1
        out_file.write('L' + str(my_label1) + ':\n')
        cond = str(self.visit(node.cmpd1))
        # my_label2 = label_id
        # label_id = label_id + 1
        # out_file.write('(jfalse, L' + str(my_label2) + ', ' + cond + ', )\n')
        val = str(self.visit(node.expr))
        out_file.write('(jtrue, L' + str(my_label1) + ', ' + val + ', )\n')

    def visit_BoolOp(self, node):
        global register_id
        left_val = str(self.visit(node.left))
        right_val = str(self.visit(node.right))
        destination_register = 'R' + str(register_id)
        out_file.write(
            '(' + str(node.op.type) + ', ' + left_val + ', ' + right_val + ', ' + destination_register + ')\n')
        register_id = register_id + 1
        return destination_register

    def visit_ForStat(self, node):
        global register_id, label_id
        value = str(self.visit(node.init))
        my_label1 = label_id
        label_id = label_id + 1
        out_file.write('L' + str(my_label1) + ':\n')
        cond = str(self.visit(node.middle))
        my_label2 = label_id
        label_id = label_id + 1
        out_file.write('(jfalse, L' + str(my_label2) + ', ' + cond + ', )\n')
        cmpd = str(self.visit(node.cmpd_stat))
        it = str(self.visit(node.end))
        out_file.write('(jmp, L' + str(my_label1) + ', , )\n')
        out_file.write('L' + str(my_label2) + ':\n')

    def visit_BreakStat(self, node):
        pass

    def interpret(self):
        tree = self.tree
        if tree is None:
            return ''
        return self.visit(tree)


def main():
    global newLine_pos
    import sys
    warn_file = open("warns.txt", 'w')
    error_file = open("errors.txt", 'w')
    text = open(sys.argv[1], 'r').read()
    # text = open('part10.pas', 'r').read()
    newLine_pos = locations_of_substring(text, '\n')
    lexer = Lexer(text, warn_file, error_file)
    parser = Parser(lexer, warn_file, error_file)
    tree = parser.parse()
    semantic_analyzer = SemanticAnalyzer(warn_file, error_file)

    try:
        semantic_analyzer.visit(tree)
    except Exception as e:
        print(e)

    interpreter = Interpreter(tree, warn_file, error_file)
    with open("out.txt", 'w') as outfile:
        global out_file
        out_file = outfile
        interpreter.interpret()


if __name__ == '__main__':
    main()
