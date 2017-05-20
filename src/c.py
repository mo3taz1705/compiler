###############################################################################
#                                                                             #
#  LEXER                                                                      #
#                                                                             #
###############################################################################

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER_TYPE  = 'INTEGER_TYPE'
INTEGER_VALUE = 'INTEGER_VALUE'
CONSTANT      = 'CONSTANT'
IF            = 'IF'
ELSE          = 'ELSE'
FOR           = 'FOR'
WHILE         = 'WHILE'
DO            = 'DO'
SWITCH        = 'SWITCH'
CASE          = 'CASE'
BREAK         = 'BREAK'
DEFAULT       = 'DEFAULT'
TRUE          = 'TRUE'
FALSE         = 'FALSE'
AND           = 'AND'
OR            = 'OR'
NOT           = 'NOT'
EQUAL         = 'EQUAL'
NOT_EQUAL     = 'NOT_EQUAL'
LESS_EQUAL    = 'LESS_EQUAL'
GREATER_EQUAL = 'GREATER_EQUAL'
LESS          = 'LESS'
GREATER       = 'GREATER'
COLON         = 'COLON'
COMMA         = 'COMMA'
ASSIGN        = 'ASSIGN'
SEMI_COLON    = 'SEMI_COLON'
L_PAREN       = 'L_PAREN'   # (
R_PAREN       = 'R_PAREN'   # )
L_BRACE       = 'L_BRACE'   # {
R_BRACE       = 'R_BRACE'   # }
PLUS          = 'PLUS'
MINUS         = 'MINUS'
MULTIPLY      = 'MULTIPLY'
DIVIDE        = 'DIVIDE'
ID            = 'ID'
EOF           = 'EOF'

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
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Lexical Error: Invalid character')

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
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

            if self.current_char == '=' and self.peek() == '=':   # EQUAL
                self.advance()
                self.advance()
                return Token(EQUAL, '==')

            if self.current_char == '!' and self.peek() == '=':   # NOT_EQUAL
                self.advance()
                self.advance()
                return Token(NOT_EQUAL, '!=')

            if self.current_char == '<' and self.peek() == '=':   # LESS_EQUAL
                self.advance()
                self.advance()
                return Token(LESS_EQUAL, '<=')

            if self.current_char == '>' and self.peek() == '=':   # GREATER_EQUAL
                self.advance()
                self.advance()
                return Token(GREATER_EQUAL, '>=')

            if self.current_char == '<':   # LESS
                self.advance()
                return Token(LESS, '<')

            if self.current_char == '>':   # GREATER
                self.advance()
                return Token(GREATER, '>')

            if self.current_char == ':':   # COLON
                self.advance()
                return Token(COLON, ':')

            if self.current_char == ',':   # COMMA
                self.advance()
                return Token(COMMA, ',')

            if self.current_char == '=':   # ASSIGN
                self.advance()
                return Token(ASSIGN, '=')

            if self.current_char == ';':   # SEMI_COLON
                self.advance()
                return Token(SEMI_COLON, ';')

            if self.current_char == '(':   # L_PAREN
                self.advance()
                return Token(L_PAREN, '(')

            if self.current_char == ')':   # R_PAREN
                self.advance()
                return Token(R_PAREN, ')')   

            if self.current_char == '{':   # L_BRACE
                self.advance()
                return Token(L_BRACE, '{')

            if self.current_char == '}':   # R_BRACE
                self.advance()
                return Token(R_BRACE, '}')         

            if self.current_char == '+':   # PLUS
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':   # MINUS
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':   # MULTIPLY
                self.advance()
                return Token(MULTIPLY, '*')

            if self.current_char == '/':   # DIVIDE
                self.advance()
                return Token(DIVIDE, '/')

            self.error()

        return Token(EOF, None)


###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################

class AST(object):   # parent node, abstract syntax tree
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

class VarDecl(AST):
    def __init__(self, var, type, exp, isConst):
        self.left = var
        self.var_type = type
        self.right = exp
        self.isConst = isConst

class Type(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Syntax Error: Invalid syntax')

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

        while self.current_token.type in (L_BRACE, ID, INTEGER_TYPE, CONSTANT, SEMI_COLON):
            results.append(self.statement())

        return results

    def statement(self):
        """
        statement : compound_statement SEMI_COLON
                  | assignment_statement SEMI_COLON
                  | declaration_statement SEMI_COLON
                  | const_statement SEMI_COLON
                  | SEMI_COLON
        """
        node = NoOp()
        if self.current_token.type == L_BRACE:
            node = self.compound_statement()
            self.eat(SEMI_COLON)
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

    def compound_statement(self):
        """
        compound_statement: L_BRACE statement_list R_BRACE
        """
        self.eat(L_BRACE)
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
                self.eat(INTEGER_DIV)

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

    def parse(self):
        node = self.program()
        if self.current_token.type != EOF:
            self.error()

        return node


###############################################################################
#                                                                             #
#  INTERPRETER                                                                #
#                                                                             #
###############################################################################

class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser
        import collections
        self.GLOBAL_SCOPE = collections.OrderedDict()

    def visit_Program(self, node):
        for child in node.children:
            self.visit(child)


    def visit_VarDecl(self, node):
        var_name = node.left.value
        if node.right:
            self.GLOBAL_SCOPE[var_name] = self.visit(node.right)

    def visit_Type(self, node):
        # Do nothing
        pass

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIVIDE:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Number(self, node):
        return node.value

    def visit_UnaryOp(self, node):
        op = node.op.type
        if op == PLUS:
            return +self.visit(node.expr)
        elif op == MINUS:
            return -self.visit(node.expr)

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node):
        var_name = node.left.value
        self.GLOBAL_SCOPE[var_name] = self.visit(node.right)

    def visit_Var(self, node):
        var_name = node.value
        var_value = self.GLOBAL_SCOPE.get(var_name)
        if var_value is None:
            raise NameError(repr(var_name))
        else:
            return var_value

    def visit_NoOp(self, node):
        pass

    def interpret(self):
        tree = self.parser.parse()
        if tree is None:
            return ''
        return self.visit(tree)


def main():
    import sys
    text = open(sys.argv[1], 'r').read()

    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    result = interpreter.interpret()

    for k, v in sorted(interpreter.GLOBAL_SCOPE.items()):
        print('%s = %s' % (k, v))


if __name__ == '__main__':
    main()