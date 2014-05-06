import os
import yacc 
import MAPlexer 
import traverse 
import sys
from asciitree import * 
from nltk.tokenize import *
import re
#sudo pip install -U pyyaml nltk

symbol_table={}


symbol_table['MultiDiGraph']=0
symbol_table['add_node']=0
symbol_table['remove_node']=0
symbol_table['def']=0
symbol_table['print']=0
symbol_table['=']=0
symbol_table[':']=0
symbol_table[',']=0
symbol_table['for']=0
symbol_table['else']=0
symbol_table['if']=0
symbol_table['elif']=0
symbol_table['for']=0
symbol_table['range']=0
symbol_table['return']=0
symbol_table['each']=0
symbol_table['nx']=0
symbol_table['and']=0
symbol_table['in']=0
symbol_table['yield']=0
symbol_table['not']=0
symbol_table['as']=0
symbol_table['assert']=0
symbol_table['break']=0
symbol_table['class']=0
symbol_table['continue']=0
symbol_table['except']=0
symbol_table['try']=0
symbol_table['elif']=0
symbol_table['exec']=0
symbol_table['finally']=0




def main(argv):
	#parse and translate map file
	inputfile=argv[1]
	filename=inputfile.split('.')
	parser=yacc.MAPparser
	lex=MAPlexer.MAPlex()
	f=open(argv[1],'r')
	test=f.read()

	#type checking
	test4=test.split("\n")
	#print test4
	typecheck(test4)

	m=parser(lex,test)
	t=traverse.Traverse(m.ast)
	
	#write the file
	#add more to the header here if necessary
	header="import networkx as nx\nimport sys\n"
	content=header
	
	
	
	#Bruteforce
	test=t.complete()
	test1=test.split("\n")
	#print test1
	
	test2=indentcheck(test1)
	test3=scopecheck(test1)
	print test2
	#main body of file
	outputfile=filename[0]+".py"
	output=open(outputfile,'w')
	content=content+test2
	
	mainstatement="if __name__ == '__main__': \n\ttry:\n\t\tmain()\n\texcept:\n\t\tprint'Error:',sys.exc_info()[0]\n\t\tprint'Resolve error before running again!'"
	content=content+mainstatement
	output.write(content)
	return outputfile

def indentcheck(test1):		
	scope=0
	numtab=0
	temptab=0
	test2=""

	for line in test1:
		#print line
		while line.startswith('\t'):
			temptab+=1
			line=line[1:]
		if not line:
			temptab=0
			continue
		if temptab<numtab:
			numtab=temptab
			scope=scope-1
		else:
			numtab=temptab

		if line.startswith('d') and line[1]=='e' and line[2]=='f':
			scope=0
			numtab=0
		i=0
		space=''
		while i<scope:
			#print scope
			space+="    "
			i+=1
		line=space+line
		#print line
		if line.endswith(':'):
			scope+=1
			numtab=temptab
			#print scope
		temptab=0
		test2+=line+'\n'
	return test2

def scopecheck(test1):
	scope=0
	numtab=0
	temptab=0
	test2=""
	line_num=0
	pattern=re.compile(r'\:|\=|\'[A-Za-z ,!]*\'|\"[A-Za-z ,!]*\"|[A-Za-z_,!]*')

	for line in test1:
		line_num+=1
		while line.startswith('\t'):
			temptab+=1
			line=line[1:]
		if not line:
			#print "hi"
			temptab=0
		if temptab<numtab:
			numtab=temptab

			temp=[]
			for key in symbol_table:
				if symbol_table[key]==scope:
					temp.append(key)
			for item in temp:
				symbol_table.pop(item,None)
			scope=scope-1
		else:
			numtab=temptab

		if line.endswith(':'):
			scope+=1
			numtab=temptab

		temptab=0
		toklist= list(regexp_tokenize(line,pattern))
		toklist=filter(None,toklist)
		if not toklist:
			continue
		if toklist[0]=="def":
			assert(symbol_table[toklist[0]]==0),"Cannot have function declaration within a function"
			#add function name to outer scope
			symbol_table[toklist[1]]=0
			print symbol_table
			for item in toklist:
				if item not in symbol_table:
					symbol_table[item]=scope
					print item
			continue	

		if toklist[1]=="=":
			symbol_table[toklist[0]]=scope


		i=0
		for item in toklist:
			#check if a literal
			if (item.startswith('\"') and item.endswith('\"')) or (item.startswith('\'') and item.endswith('\'')):
				continue
			else:
				if item not in symbol_table:
					print toklist[i]
					print item
					print "ERROR: \""+item+"\" not defined in scope"
					print "Error on line "+str(line_num) 
					sys.exit()
			i+=1
	#print symbol_table
	return

def typecheck(test1):
	scope=0
	typearray={}
	line_num=0
	for line in test1:
	#	print typearray
		line_num+=1
		array=[]
		lex=MAPlexer.MAPlex()
		lex.build()
		lexer=lex.lexer
		lexer.input(line)
		while True:
			tok=lexer.token()
			if tok:
				array.append(tok)
				#print tok.type
			else:
				break
		if len(array)<2:
			continue
		if array[0].type=="FUNC":
			i=0
			scope+=1
			for element in array:
				if (element.value not in typearray) and element.type=='ID':
					#print element.value
					typearray[element.value]=array[i-1].value
				#	print typearray
				i+=1
			continue
		if array[1].value in typearray and array[0].type!='RETURN':
			print "ERROR: Casting a variable more than once"
			print "Error on line "+str(line_num)
			sys.exit()
		if array[0].type=="TYPE":
			typearray[array[1].value]=array[0].value
	#		print typearray
		i=0
		for item in array:
			if i==0:
				i+=1
				continue

			if item.type=="ID":
				print item
				if item.value not in typearray:
					print item.value
					if array[i-1].type=="FOR" or array[i-1].type=="FOREACH":
						typearray[item.value]="NUMERIC"
						continue
					print "ERROR: "+item.value+" is not casted properly"
					print "Error on line "+str(line_num)
					sys.exit()


	#		print typearray
		#print " "
		del array

	if 'main' not in typearray:
		print "Function does not have main function"
		sys.exit()
	return


if __name__ == '__main__':
	f=main(sys.argv)
	command="python " + f

	#os.system(command)
	#os.remove(f)

