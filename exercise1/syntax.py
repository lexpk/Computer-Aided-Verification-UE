'''
This file contains the syntax of expressions and formulas.
Each connective has its own class, to similify your job you might want
to redifine the connectives in terms of each other, for example

    NotEquals(left, right) = Not(Equals(left, right))
    
is a valid definition, which is already used.
'''


from abc import ABC

class Expression(ABC):
    pass


class BooleanExpression(Expression):
    pass


class EnumExpression(Expression):
    pass


class LTLFormula(Expression):
    pass


class Enum(EnumExpression):
    def type_check(elements):
        for element in elements:
            if not isinstance(element, EnumIdentifier) and \
                not isinstance(element, EnumValue):
                raise Exception("Enum elements must be identifiers")
    
    def __init__(self, elements):
        Enum.type_check(elements)
        self.elements = elements


class EnumIdentifier(EnumExpression):
    def type_check(name):
        if not isinstance(name, str):
            raise Exception("Identifier name must be a string")
    
    def __init__(self, name):
        EnumIdentifier.type_check(name)
        self.name = name


class BooleanIdentifier(BooleanExpression, LTLFormula):
    def type_check(name):
        if not isinstance(name, str):
            raise Exception("Identifier name must be a string")
    
    def __init__(self, name):
        BooleanIdentifier.type_check(name)
        self.name = name


class EnumValue(EnumExpression):
    def type_check(name):
        if not isinstance(name, str):
            raise Exception("Enum value must be a string")
    
    def __init__(self, name):
        EnumValue.type_check(name)
        self.name = name


class BooleanValue(BooleanExpression):
    def type_check(name):
        if name not in ["TRUE", "FALSE"]:
            raise Exception("Boolean value must be True or False")
    
    def __init__(self, name):
        BooleanValue.type_check(name)
        self.name = name


class Not(BooleanExpression, LTLFormula):
    def type_check(expression):
        if not isinstance(expression, BooleanExpression) and not isinstance(expression, LTLFormula):
            raise Exception("Negated expression must be a boolean expression or LTL formula")
    
    def __init__(self, expression):
        self.expression = expression


class And(BooleanExpression, LTLFormula):
    def type_check(left, right):
        if (not isinstance(left, BooleanExpression) and not isinstance(left, LTLFormula)) or \
              (not isinstance(right, BooleanExpression) and not isinstance(right, LTLFormula)):
            raise Exception("And expression must have boolean expressions or LTL formulas")
    
    def __init__(self, left, right):
        And.type_check(left, right)
        self.left = left
        self.right = right


class Or(BooleanExpression, LTLFormula):
    def type_check(left, right):
        if (not isinstance(left, BooleanExpression) and not isinstance(left, LTLFormula)) or \
              (not isinstance(right, BooleanExpression) and not isinstance(right, LTLFormula)):
            raise Exception("Or expression must have boolean expressions or LTL formulas")
    
    def __init__(self, left, right):
        Or.type_check(left, right)
        self.left = left
        self.right = right


class Implies(BooleanExpression, LTLFormula):
    def type_check(left, right):
        if (not isinstance(left, BooleanExpression) and not isinstance(left, LTLFormula)) or \
              (not isinstance(right, BooleanExpression) and not isinstance(right, LTLFormula)):
            raise Exception("Implies expression must have boolean expressions or LTL formulas")
    
    def __init__(self, left, right):
        Implies.type_check(left, right)
        self.left = left
        self.right = right


class Eq(BooleanExpression):
    def type_check(left, right):
        if not (isinstance(left, EnumExpression) and isinstance(right, EnumExpression)) and \
                not (isinstance(left, BooleanExpression) and isinstance(right, BooleanExpression)):
            raise Exception("Equals expression must have two expressions of same type")
    
    def __init__(self, left, right):
        Eq.type_check(left, right)
        self.left = left
        self.right = right


def Neq(left, right):
    return Not(Eq(left, right))


class In(BooleanExpression):
    def type_check(left, right):
        if not isinstance(left, EnumExpression) or not isinstance(right, EnumExpression):
            raise Exception("In expression must have enum arguments") 
    
    def __init__(self, left, right):
        In.type_check(left, right)
        self.left = left
        self.right = right


class EnumCase(EnumExpression):
    def type_check(conditions, values):
        if not all(isinstance(condition, BooleanExpression) for condition in conditions):
            raise Exception("Enum case conditions must be boolean expressions")
        if not all(isinstance(value, EnumExpression) for value in values):
            raise Exception("Enum case values must be enum expressions")

    def __init__(self, conditions, values):
        EnumCase.type_check(conditions, values)
        self.conditions = conditions
        self.values = values


class BooleanCase(EnumExpression):
    def type_check(conditions, values):
        if not all(isinstance(condition, BooleanExpression) for condition in conditions):
            raise Exception("Boolean case conditions must be boolean expressions")
        if not all(isinstance(value, BooleanExpression) for value in values):
            raise Exception("Boolean case values must be boolean expressions")

    def __init__(self, conditions, values):
        BooleanCase.type_check(conditions, values)
        self.conditions = conditions
        self.values = values


class G(LTLFormula):
    def type_check(formula):
        if not isinstance(formula, LTLFormula) and not isinstance(formula, BooleanExpression):
            raise Exception("G operator must have a boolean expression or LTL formula")
    
    def __init__(self, formula):
        G.type_check(formula)
        self.formula = formula


class F(LTLFormula):
    def type_check(formula):
        if not isinstance(formula, LTLFormula) and not isinstance(formula, BooleanExpression):
            raise Exception("F operator must have a boolean expression or LTL formula")
        
    def __init__(self, formula):
        F.type_check(formula)
        self.formula = formula
        

class X(LTLFormula):
    def type_check(formula):
        if not isinstance(formula, LTLFormula) and not isinstance(formula, BooleanExpression):
            raise Exception("X operator must have a boolean expression or LTL formula")
        
    def __init__(self, formula):
        X.type_check(formula)
        self.formula = formula


class U(LTLFormula):
    def type_check(left, right):
        if not isinstance(left, LTLFormula) and not isinstance(left, BooleanExpression):
            raise Exception("U operator left operand must be a boolean expression or LTL formula")
        if not isinstance(right, LTLFormula) and not isinstance(right, BooleanExpression):
            raise Exception("U operator right operand must be a boolean expression or LTL formula")
    
    def __init__(self, left, right):
        U.type_check(left, right)
        self.left = left
        self.right = right


class R(LTLFormula):
    def type_check(left, right):
        if not isinstance(left, LTLFormula) and not isinstance(left, BooleanExpression):
            raise Exception("R operator left operand must be a boolean expression or LTL formula")
        if not isinstance(right, LTLFormula) and not isinstance(right, BooleanExpression):
            raise Exception("R operator right operand must be a boolean expression or LTL formula")
    
    def __init__(self, left, right):
        R.type_check(left, right)
        self.left = left
        self.right = right
