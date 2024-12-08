from .ExpressionNode import ExpressionNode
from LexicalAnalyzer import Token


class VariableNode(ExpressionNode):
    """Класс для узла переменной."""
    
    def __init__(self, token: Token):
        self.variable = token