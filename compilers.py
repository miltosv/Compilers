#Stella Delia AM:2430 cse32430
#Miltiadis Vasiliadis AM:2944 cse52944 
# Reserve Words
import sys
import os
#from cProfile import label

PROGRAM_TK='programtk'
ENDPROGRAM_TK='endprogramtk'
DECLARE_TK='declaretk'
IF_TK='iftk'
THEN_TK='thentk'
ELSE_TK='elsetk'
ENDIF_TK='endiftk'
DOWHILE_TK='dotk'
WHILE_TK='whiletk'
ENDWHILE_TK='endwhiletk'
ENDDOWHILE_TK='enddowhiletk'
LOOP_TK='looptk'
ENDLOOP_TK='endlooptk'
EXIT_TK='exittk'
FORCASE_TK='forcasetk'
ENDFORCASE_TK='endforcasetk'
INCASE_TK='incasetk'
ENDINCASE_TK='endincasetk'
WHEN_TK='whentk'
DEFAULT_TK='defaulttk'
ENDDEFAULT_TK='enddefaulttk'
FUNCTION_TK='functiontk'
ENDFUNCTION_TK='endfunctiontk'
RETURN_TK='returntk'
IN_TK='intk'
INOUT_TK='inouttk'
INANDOUT_TK='inandouttk'
AND_TK='andtk'
OR_TK='ortk'
NOT_TK='nottk'
INPUT_TK='inputtk'
PRINT_TK='printtk'

ID_TK='idtk'
DIGIT_TK='digittk'
PLUS_TK='plustk'
MINUS_TK='minustk'
STAR_TK='startk'
SLASH_TK='slashtk'
OPENPAR_TK='openpartk'
CLOSEPAR_TK='closepartk'
OPENBRACKET_TK='openbrackettk'
CLOSEBRACKET_TK='closebrackettk'
SEMICOLON_TK='semicolontk'
COMMA_TK='commatk'
EQUAL_TK='equaltk'
ASSIGN_TK='assigntk'
COLON_TK='colontk'
DIF_TK='differenttk'
LESSOREQUAL_TK='smallorequaltk'
LESS_TK='smalltk'
GREATEROREQUAL_TK='greatorequaltk'
GREATER_TK='greattk'

state=0
line = 1
buffer="\0"*150
token=''
word=''
tempCounter=0
label=''
programID=''

symboltable = []


#classes gia pinaka symbolon


class entity:
	name = ''
	type = ''
	offset = 0
	
	
	startquad = -1
	arguments = emptyList()
	framelength = -1
	parMode = 0
	value = ''
	nextEntiy = None
	def __init__(self):
		name= ''
	


class scope:
	Entity = []
	
	nestingLevel=0
	enclosingScope= None
	
	def __init__(self):
		nestingLevel=0
		
class argument:
	parmode = 0
	
	type = ''
	next= None
	
	

##SYNARTISEIS GIA TON ENDIAMESO KODIKA##

def nextQuad():
	global label
	return label

def emptyList():
	return []

def newTemp():
	global tempCounter
	t='T_'+tempCounter
	return t

def genQuad(oper,x,y,z):
	global label
	global intermediate	
	lbl = 'L'+str(label)
	quad = [lbl, oper, x, y, z]
	label = label + 1
	
	intermediate = intermediate + [quad]
	
def makeList(x):
	z='L'+str(x)
	return[z]
	
def mergeList(L1,L2):
	return L1+L2

def backpatch(L,z):
	z = 'L'+str(z)
	global intermediate
	for i in range(len(L)):
		label = L[i]
	for j in range(len(intermediate)):
		x = intermediate[j]
		if x[0] == label:
			x[4] = z
			break



# Endiamesos

intermediate= emptyList()
variables= emptyList()

#BTrue = emptyList()
#BFalse = emptyList()
#QTrue = emptyList()
#QFalse = emptyList()
########END ENDIAMESOS KODIKAS #####

def getChar():   
	c=f.read(1)   
	return c

def backChar():
	f.seek(f.tell() - 1, os.SEEK_SET)

def isLetter(c):
	if (c>='A') and (c<='Z') or (c>='a') and (c<='z'):
		return True
	else:
		return False

def isDigit(c):
	if (c>='0') and (c<='9'):
		return True
	else:
		return False
		
def isSpace(c):
	if (c=='\n') or (c=='\t') or (c==' '):
		return True
	else:
		return False
		
		
def isNumOp(c):
	if c=='+' or c=='-' or c=='/' or c=='*':
		return True
	else:
		return False
		
def Reserved(word):
	
	word=''.join(word)
	if word=="program":
		return PROGRAM_TK,word
	if word=="endprogram":
		return ENDPROGRAM_TK,word
	if word=="declare":
		return DECLARE_TK,word
	if word=="if":
		return IF_TK,word
	if word=="then":
		return THEN_TK,word
	if word=="else":
		return ELSE_TK,word
	if word=="endif":
		return ENDIF_TK,word
	if word=="dowhile":
		return DOWHILE_TK,word
	if word=="while":
		return WHILE_TK,word
	if word=="enddowhile":
		return ENDDOWHILE_TK,word
	if word=="endwhile":
		return ENDWHILE_TK,word
	if word=="loop":
		return LOOP_TK,word
	if word=="endloop":
		return ENDLOOP_TK,word
	if word=="exit":
		return EXIT_TK,word
	if word=="forcase":
		return FORCASE_TK,word
	if word=="endforcase":
		return ENDFORCASE_TK,word
	if word=="incase":
		return INCASE_TK,word
	if word=="endincase":
		return ENDINCASE_TK,word
	if  word=="when":
		return WHEN_TK,word
	if word=="default":
		return DEFAULT_TK,word
	if word=="enddefault":
		return ENDDEFAULT_TK,word
	if word=="function":
		return FUNCTION_TK,word
	if word=="endfunction":
		return ENDFUNCTION_TK,word
	if word=="return":
		return RETURN_TK,word
	if word=="in":
		return IN_TK,word
	if word=="inout":
		return INOUT_TK,word
	if word=="inandout":
		return INANDOUT_TK,word
	if word=="and":
		return AND_TK,word
	if word=="or":
		return OR_TK,word
	if word=="not":
		return NOT_TK,word
	if word=="input":
		return INPUT_TK,word
	if word=="print":
		return PRINT_TK,word
	else:
		return ID_TK,word
		
def lex():

	buffer = []
	
	while 1:
	
		c=getChar()
		if c=="\n":
			global line
			line+=1
		if isSpace(c):
			continue
			
		if isLetter(c):
			buffer.append(c)
			
			while 1:
				c=getChar()
				
				while isLetter(c) or isDigit(c):
					buffer.append(c)
					c=getChar()
				backChar()
				
				del buffer[30:]
				#print(*buffer) 
				token, word = Reserved(buffer)
				del buffer[:]
				return token,word
		
		if isDigit(c):
			buffer.append(c)
			c=getChar()
			if isLetter(c):
				print('Error in lex ids cant start with digit at line', line )
				exit(0)
			while(isDigit(c)):
				buffer.append(c)
				c=getChar()
				if isLetter(c):
					print('Error in lex ids cant start with digit at line', line )
					exit(0)
			
			word=''.join(buffer)

			int_word=int(word)
			if int_word <= 32767:
				backChar()
				token=DIGIT_TK
				return token, word
			else:
				print ('Number is out of limits! Error in line: %d ') %line
				exit(1)
		
		if c == '+':
			token=PLUS_TK
			return token,c
		
		if c == '-':
			token=MINUS_TK
			return token,c
			
		if c == '*':
			token=STAR_TK
			return token,c
			
		if c == '/':
			c=getChar()
			if c =='*':
				while 1:
					c=getChar()
					if c =='':
						print ('Error in comments: line : EOF',line)
						exit(1)
					if c=='*':
						c=getChar()
						if c =='/':
							token, word = lex()
							return token, word
						#state=COMMENT_TK
			elif c=='/':
				while 1:
					c=getChar()
					if c=='\n':
						token, word = lex()
						return token, word
					#state=COMMENT_TK
			else:
				backChar()
				token=SLASH_TK
				return token,c
		
		if c == '(':
			token=OPENPAR_TK
			return token,c
			
		if c == ')':
			token=CLOSEPAR_TK
			return token,c
			
		if c == '[':
			token=OPENBRACKET_TK
			return token,c
			
		if c == ']':
			token=CLOSEBRACKET_TK
			return token,c
			
		if c == ';':
			token=SEMICOLON_TK
			return token,c
			
		if c == ',':
			token=COMMA_TK
			return token,c
			
		if c == '=':
			token=EQUAL_TK
			return token,c
	
		if c == ':':
			c=getChar()
			if c =='=':
				token=ASSIGN_TK
				return token,':='
			else:
				backChar()
				token=COLON_TK
				return token,c
		
		if c == '<':
			c=getChar()
			if c=='>':
				token=DIF_TK
				return token,'<>'
			elif c=='=':
				token=LESSOREQUAL_TK
				return token,'<='
			else:
				backChar()
				token=LESS_TK
				return token,c
				
		if c=='>':
			c=getChar()
			if c =='=':
				token=GREATEROREQUAL_TK
				return token, '>='
			else:
				backChar()
				token=GREATER_TK
				return token,c
				
	else:
		print ('Found unrecognizable character in line %d!' %line)
		exit(0)
		
				
				
				
#syntax

def program():
	global token
	global word
	token,word=lex()
	if token==PROGRAM_TK:
		token,word=lex()
		if token==ID_TK:
			global programID
			programID=token
			token,word=lex();
			block();
		else:
			print ("Program Name expected at line",line)
			exit(0)
	else: 
		print("the keyword program was expected at line",line)
		exit(0)
	if token!=ENDPROGRAM_TK:
		print("ERROR expected endprogram at line",line)
		exit(0)
	else:
		print('SyntaxPassed')
		exit(0)
	

def block():
	global ID
	global token
	global word
	declarations()
	subprograms()
	genQuad("begin_block",ID,"_","_")
	statements()
	genQuad("halt", "_", "_", "_")
	genQuad("end_block",ID,"_","_")

def declarations():
	global token
	global word
	if token==DECLARE_TK:
		token,word=lex()
		varlist()
		if token!=SEMICOLON_TK:
			print("expected ; in line", line)
			exit(0)
		token,word=lex()
	else:
		return
		
def varlist():
	global token
	global word
	if token==ID_TK:
		token,word=lex()
		while token==COMMA_TK:
			token,word=lex()
			if token!=ID_TK:
				print("Expected ID", line)
				exit(0)
			token,word=lex()	
	else:
		return

def subprograms():
	global token
	global word
	while token==FUNCTION_TK:
		token,word=lex()
		subprogram()
	
def subprogram():
	global token
	global word	
	if token!=ID_TK:
		print("error in line",line,"function id expected")
		exit(0)
	token,word=lex()
	funcbody()
	if token!=ENDFUNCTION_TK:
		print("error in line",line,"endfunction expected")
		exit(0)
	token,word=lex()
	
def funcbody():
	formalpars()
	block()

def formalpars():
	global token
	global word
	if token!=OPENPAR_TK:
		print("error in line",line)
		exit(0)
	
	token,word=lex()
	formalparlist()
		
	if token!=CLOSEPAR_TK:
		print("error, expected ')', line", line)
		exit(0)
	token,word=lex()
		
def formalparlist():
	global token
	global word
	if token==CLOSEPAR_TK:
		return
		
	formalparitem()
	
	while token==COMMA_TK:	
		token,word=lex()
		formalparitem()
	return 		
	
def formalparitem():
	global token
	global word
	tp = ' '
	if token==IN_TK or token==INANDOUT_TK or token==INOUT_TK:
		if token== IN_TK:
			tp="cv"
		if token == INOUT_TK:
			tp = "REF"
		if token == INANDOUT_TK:
			tp = "RET"
		token,word=lex()
		if token!=ID_TK:
			print("error, expected ID at line", line)
			exit(0)
		
		genQuad("par", word, tp , "_")
		token,word=lex()
	
def statements():
	global token
	global word
	statement()
	while token==SEMICOLON_TK:
		token,word=lex()
		statement()
	
def statement():
	global token
	global word
	if token==ID_TK:
		assignment_stat()
	elif token==IF_TK:
		
		if_stat()
	elif token==WHILE_TK:
		
		while_stat()
	elif token==DOWHILE_TK:
		
		dowhile_stat()
	elif token==LOOP_TK:
		
		loop_stat()
	elif token==EXIT_TK:
		
		exit_stat()
	elif token==FORCASE_TK:
	
		for_stat()
	
	elif token==INCASE_TK:
		
		incase_stat()
		
	elif token==RETURN_TK:
		
		return_stat()
	
	elif token==INPUT_TK:
		
		input_stat()
		
	elif token==PRINT_TK:
		
		print_stat()
	else:
		return
	
def assignment_stat():
	global token
	global word
	IDplace=word
	
	token,word=lex()
	
	
	if token!=ASSIGN_TK:
		print("expected := at line",line)
		exit(0)
	token,word=lex()
	#place = word
	Eplace = expression()
	genQuad(":=", Eplace, "_", IDplace)	
	
		
def if_stat():
	global token
	global word
	token,word=lex()
	if token!=OPENPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	token,word=lex()
	condition()

	if token!=CLOSEPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	token,word=lex()
	
	if token!=THEN_TK:
		print ('Expected thentk! error in line %d' %line)
		exit(0)
	token,word=lex()	
	statements()
	else_part()

	if token != ENDIF_TK :
		print ('Expected endiftk! error in line %d' %line)
		exit(0)
	token,word=lex()
		
def else_part():
	global token
	global word
	if token == ELSE_TK:
		token,word=lex()
		statements()
	
def while_stat():
	global token
	global word
	Bquad=nextQuad()
	token,word=lex()
	if token!=OPENPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	token,word=lex()	
	CondTrue,CondFalse = condition()
	#backpatch(CondTrue, nextQuad())
	
	if token!=CLOSEPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
		
	
	token,word=lex()
	
	backpatch(CondTrue, nextQuad())
	
	statements()
	
	
	if token != ENDWHILE_TK :
		print ('Expected endwhiletk! error in line %d' %line)
		exit(0)
	genQuad("jump", "_", "_", Bquad)
	backpatch(CondFalse, nextQuad())
	token,word=lex()
	
def dowhile_stat():
	global token
	global word
	token,word=lex()
	
	sQuad = nextQuad()
	
	statements()

	if token != ENDDOWHILE_TK :
		print ('Expected whiletk! error in line %d' %line)
		exit(0)
	token,word=lex()	
	
	if token!=OPENPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	token,word=lex()	
	
	CondTrue,CondFalse=condition()
	
	if token!=CLOSEPAR_TK:
		print("Expected parenthesis! error in line",line)
		exit(0)
	backpatch(CondFalse, sQuad)
	backpatch(CondTrue, nextQuad())
	token,word=lex()
	
def loop_stat():
	global token
	global word
	token,word=lex()
	statements()
	if token != ENDLOOP_TK :
		print ('Expected endlooptk! error in line %d' %line)
		exit(0)
	token,word=lex()	
	
def exit_stat():
	global token
	global word
	token,word=lex()
	return
	
def for_stat():
	global token
	global word
	exitlist = emptyList()
	true = emptyList()
	false = emptyList()
	
	token,word=lex()
	while token== WHEN_TK:
		token,word=lex()
		if token!=OPENPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		token,word=lex()
		#t=makeList(nextQuad())
		true,false = condition()
		mergeList(exitlist, false)
		backpatch(true, nextQuad())
		if token!=CLOSEPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		token,word=lex()
		
		if token!=COLON_TK:
			print("Expected colontk! error in line",line)
			exit(0)
		token,word=lex()
		statements()
		
		t=makeList(nextQuad())
		makeList(genQuad("jump", "_", "_", "_"))
		
	if token!=DEFAULT_TK:
			print("Expected defaulttk! error in line",line)
			exit(0)
	token,word=lex()
	
	if token!=COLON_TK:
			print("Expected colontk! error in line",line)
			exit(0)
	token,word=lex()		
	statements()

	if token!=ENDDEFAULT_TK:
			print("Expected enddefaulttk! error in line",line)
			exit(0)
	token,word=lex()
	
	if token!=ENDFORCASE_TK:
			print("Expected endforcasetk! error in line",line)
			exit(0)	
	token,word=lex()
	
def incase_stat():
	global token
	global word
	token,word=lex()
	while token== WHEN_TK:
		token,word=lex()
		if token!=OPENPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		token,word=lex()
		condition()
		
		if token!=CLOSEPAR_TK:
			print("Expected parenthesis! error in line",line)
			exit(0)
		token,word=lex()
		
		if token!=COLON_TK:
			print("Expected colontk! error in line",line)
			exit(0)
		token,word=lex()	
		statements()
		
	
	if token!=ENDINCASE_TK:
			print("Expected endincasetk! error in line",line)
			exit(0)	
	token,word=lex()
	
def return_stat():
	global token
	global word
	token,word=lex()
	expression()	
	genQuad("retv",word,"_","_")
	
def print_stat():
	global token
	global word
	token,word=lex()
	expression()
	genQuad("out", "word", "_", "_")

def input_stat():
	global token
	global word
	idplace= ''
	token,word=lex()

	if token!=ID_TK:
		print("Expected ID at line,", line)
		exit(0)
	genQuad("inp", idplace, "_", "_")
	token,word=lex()
		
def actualpars():
	global token
	global word

	if token!=OPENPAR_TK:
		print("Expected ( at line,",line)
		exit(0)
	token,word=lex()
	actualparlist()
	
	if token!=CLOSEPAR_TK:
		print("expected ) at line", line)
		exit(0)
	token,word=lex()
	
def actualparlist():
	global token
	global word
	if token!=CLOSEPAR_TK:
		actualparitem()
		while token==COMMA_TK:
			token,word=lex()
			actualparitem()
	else:
		return

def actualparitem():
	global token
	global word

	if token==IN_TK:
		token,word=lex()
		expression()
	elif token==INOUT_TK:
		token,word=lex()
		if token!=ID_TK:
			print("error expected ID", line)
			exit(0)
		token,word=lex()
	elif token==INANDOUT_TK:
		token,word=lex()
		if token!=ID_TK:
			print("error expected ID", line)
			exit(0)
		token,word=lex()
	else:
		print("error actual par item",line)
		exit(0)

def condition():
	global token
	global word
	
	BTrue = emptyList()
	
	BFalse = emptyList()
	
	BTrue,BFalse=boolterm()
	
	while token==OR_TK:
		
		backpatch(BFalse,nextQuad())
		
		token,word=lex()
		qTrue = emptyList()
		qFalse = emptyList()
		qTrue,qFalse = boolterm()
		mergeList(BFalse, qFalse)
		
	return BTrue,BFalse
	
def boolterm():
	global token
	global word
	QTrue=emptyList()
	QFalse=emptyList()
	
	Qtrue,QFalse=boolfactor()
	
	while token==AND_TK:
		backpatch(QTrue, nextQuad())
		token,word=lex()
		
		rTrue,rFalse=boolfactor()
		
		mergeList(QFalse,rFalse)
		
	return QTrue,QFalse	
def boolfactor():
	global token
	global word
	RTrue=emptyList()
	RFalse=emptyList()

	if token==NOT_TK:
		token,word=lex()
		if token==OPENBRACKET_TK:
			token,word=lex()
			condition()
		
		else:
			print("expected [ at line",line)
			exit(0)
			
		if token!=CLOSEBRACKET_TK:
			print("error expected ] at line", line)
			exit(0)
		token,word=lex()
		
	elif token==OPENBRACKET_TK:
		token,word=lex()
		condition()
		
		if token!=CLOSEBRACKET_TK:
			print("error expected ] at line", line)
			exit(0)
		token,word=lex()
	else:
		expression()
		relational_oper()
		expression()
	return RTrue,RFalse


def expression():
	global token
	global word
	
	T1Place=''
	
	T1Place=word
	T2Place=''
	EPlace=''
	
	optional_sign()
	term()
	
	while(token==PLUS_TK or token==MINUS_TK):
		add_oper()
		opeator=''
		operator=word
		term()
		
		token,word=lex()
		
		T2Place=word
		w = newTemp()
		genQuad(operator, T1Place, T2Place, w)
	EPlace=T1Place
	return EPlace

def term():
	global token
	global word
	F1Place=''
	F2Place=''
	Tplace=''
	factor()
	F1Place=word
	
	while(token==STAR_TK or token==SLASH_TK):
		mul_oper()
		operator=word
		
		factor()
		F2Place=word
		w=newTemp()
		genQuad(operator, F1Place, F2Place, w)
	TPlace=F1Place
	
	
def factor():
	global token
	global word
	if token==DIGIT_TK:
		digit=word
		token,word=lex()
		return digit
	elif token==OPENPAR_TK:
		token,word=lex()
		expression()
		
		if token!=CLOSEPAR_TK:
			print("expected ) at line", line)
			exit(0)
		token,word=lex()
	elif token==ID_TK:
		token,word=lex()
		idtail()
	else: 
		print("error in factor", line)
		exit(0)
		
def idtail():
	global token
	global word

	if token==OPENPAR_TK:
		actualpars()
	else:
		return

def relational_oper():
	global token
	global word
	RTrue = emptyList()
	RFalse = emptyList()
	if token==EQUAL_TK:
		RTrue=makeList(nextQuad())
		genQuad(word, E1Place, E2Place, "_")
		RFalse=makeList(nextQuad())
		genQuad("jump", "_", "_", "_")
		token,word=lex()
		return
	if token==LESSOREQUAL_TK:
		RTrue=makeList(nextQuad())
		genQuad(word, E1Place, E2Place, "_")
		RFalse=makeList(nextQuad())
		genQuad("jump", "_", "_", "_")
		token,word=lex()
		return
	if token==GREATEROREQUAL_TK:
		RTrue=makeList(nextQuad())
		genQuad(word, E1Place, E2Place, "_")
		RFalse=makeList(nextQuad())
		genQuad("jump", "_", "_", "_")
		token,word=lex()
		return
	if token==LESS_TK:
		RTrue=makeList(nextQuad())
		genQuad(word, E1Place, E2Place, "_")
		RFalse=makeList(nextQuad())
		genQuad("jump", "_", "_", "_")
		token,word=lex()
		return
	if token==GREATER_TK:
		RTrue=makeList(nextQuad())
		genQuad(word, E1Place, E2Place, "_")
		RFalse=makeList(nextQuad())
		genQuad("jump", "_", "_", "_")
		token,word=lex()
		return
	if token==DIF_TK:
		RTrue=makeList(nextQuad())
		genQuad(word, E1Place, E2Place, "_")
		RFalse=makeList(nextQuad())
		genQuad("jump", "_", "_", "_")
		token,word=lex()
		return
	else:
		print("expected = <= >= <> < > at line", line)
		exit(0)
		
def add_oper():
	global token
	global word
	if token==PLUS_TK:
		token,word=lex()
		return
	if token==MINUS_TK:
		token,word=lex()
		return
	else:
		print("expected, + or - ", line)
		exit(0)
		
def mul_oper():
	global word
	global token
	if token==STAR_TK:
		token,word=lex()
		return
	if token==SLASH_TK:
		token,word=lex()
		return
	else:
		print("expected * or /", line)
		
def optional_sign():
	global word
	global token
	if token==PLUS_TK or token==MINUS_TK:
		add_oper()
	else:
		return
		

def C_code(FileName):
	global intermediate
	FileName_new = FileName[:len(FileName)-3] + ".c"
	f = open(FileName_new,"w")
	code = "int main(){ \n " + ",".join(variables)+ ";\n"
	f.write(code)
	for i in range(len(intermediate)):
		interm = intermediate[i]
		code = str(interm[0])+" :"+" "
		
		if interm[1]==":=":
			code = code + interm[4]+"="+interm[2]
		if interm[1]=="+" or interm[1]=="-" or interm[1]=="*" or interm[1]=="/":
			code = code + interm[4]+"="+interm[2]+interm[1]+interm[3]
		if interm[1]=='<' or interm[1]=='>' or interm[1]=='<=' or interm[1]=='>=' or interm[1]=='<>':
			code = code + "if("+interm[2]+interm[1]+interm[3]+") goto"+interm[4]
		if interm[1]=='jump' :
			code = code + "goto "+interm[4]
		if interm[1]== "halt":
			code = code + "{}"
		code = code + '\n'
		
		f.write(code)
	
	f.write("} \n")
	f.close()		
			
def add_scope():
	global symboltable
	
	Scope = scope()
	Scope.offset = 12
	if len(symboltable)==0:
		scope.nestingLevel = 0
	else:
		scope.nestingLevel = 1 + symboltable[0].nestingLevel
		
		
	symboltable = [Scope]+symboltable
			
	
def delete_scope():
	global symboltable
	if len(symboltable)>1:
		Scope = symboltable	
		
	

			
f=open(sys.argv[1],"r")
program()

