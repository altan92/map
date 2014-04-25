import sys
import unittest
import yacc 
import MAPlexer 
import traverse 
from MAPtestfiles import MapTests
from asciitree import *


class TestTraverseSyntax(unittest.TestCase):
	def setUp(self):
		self.lex=MAPlexer.MAPlex()

	def testhelloworld(self):
		 test= MapTests.helloworld
		 m=yacc.MAPparser(self.lex,test)
		 t=traverse.Traverse(m.ast)
		 t.enter()


if __name__ == "__main__": 
	unittest.main()