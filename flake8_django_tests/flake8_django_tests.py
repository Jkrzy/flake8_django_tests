# -*- coding: utf-8 -*-
"""
"""
import ast
NONCOMPLIANT_STARTSWITH = ('test', 'ensure')

class DjangoTestDocStrings(object):
    name = 'flake8-django-test-docstrings'
    version = '0.0.1'
    message = "DJT001 Don't include preambles such as \"Tests that\" or \"Ensures that\"."

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree

    @classmethod
    def parse_options(self, options):
        """Only check test_ modules"""
        self.options = options
        self.options.filename = ['*test_*.py']

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                docstring = ast.get_docstring(node)
                if not check_compliance(docstring):
                    yield node.lineno+1, node.col_offset+4, self.message, type(self)

def check_compliance(docstring):
    """
    Return True if doc_string is compliant
    Compliance determined by Django's coding-style.txt
    """
    compliant = False
    if docstring is None or not docstring.lower().startswith(NONCOMPLIANT_STARTSWITH):
        compliant = True
    return compliant
