#Stella Delia AM:2430
#Miltiadis Vasiliadis AM:2944

# Reserve Words
PROGRAM_TK='programtk'
ENDPROGRAM_TK='endprogramtk'
DECLARATIONS_TK='declarationstk'
IF_TK='iftk'
THEN_TK='thentk'
ELSE_TK='elsetk'
ENDIF_TK='endiftk'
DO_TK='dotk'
WHILE_TK='whiletk'
ENDWHILE_TK='endwhiletk'
LOOPF_TK='loopforevertk'
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
INANDOUT_TK='inandouttk'
AND_TK='andtk'
OR_TK='ortk'
NOT_TK='nottk'
INPUT_TK='inputtk'
PRINT_TK='printtk'


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
SMALLOREQUAL_TK='smallorequaltk'
SMALL_TK='smalltk'
GREATOREQUAL_TK='greatorequaltk'
GREAT_TK='greattk'

state=0
line = 1
buffer="\0"*150

def getChar()
	c=f.read(1)
	return c

def backChar()
	f.seek(-1,1)

def isLetter(c)
	if (c>='A') and (c<='Z') or (c>='a') and (c<='z'):
		return True
	else:
		return False

def isDigit(c)
	if (c>='0') and (c<='9'):
		return True
	else:
		return False
		
def ifSpace(c)
	if (c=='\n') or (c=='\t') or (c==' '):
		return True
	else:
		return False
		
		
def isNumOp(c)
	if c=='+' or c=='-' or c=='/' or c=='*':
		return True
	else:
		return False
		
def Reserved(word)
	
	word=''.join(word)
	if word=="program":
		return PROGRAM_TK,word
	if word=="endprogram":
		return ENDPROGRAM_TK,word
	if word=="declarations":
		return DECLARATIONS_TK,word
	if word=="if":
		return IF_TK,word
	if word=="then":
		return THEN_TK,word
	if word=="else":
		return ELSE_TK,word
	if word=="endif":
		return ENDIF_TK
	if word=="do":
		return DO_TK,word
	if word=="while":
		return WHILE_TK,word
	if word=="endwhile"
		return ENDWHILE_TK,word
	if word=="loopf":
		return LOOPF_TK,word
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
	if word=="and"
		return AND_TK,word
	if word=="or"
		return OR_TK,word
	if word=="not"
		return NOT_TK,word
	if word=="input"
		return INPUT_TK,word
	if word=="print"
		return PRINT_TK,word
	else:
		return ID_TK,word
		
def lex()

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
				c.getChar()
				
				while isLetter(c) or isDigit(c):
					buffer.append(c)
					c=getChar()
				backChar()
				
				del buffer[30:]
				token, word = Reserved(buffer)
				del buffer[:]
				return token,word
		
		if isDigit(c):
			buffer.append(c)
			c=getChar()
			while(isDigit(c))
				buffer.append(c)
				c=getChar()
			if c <= '32767' :
				backChar()
				word=''.join(buff)
				token=DIGIT_TK
				return token, word
			else:
				print 'Number is out of limits! Error in line: %d ' %line
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
			if c =='*'
				while 1:
					c=getChar()
					if c =='':
						print 'Error in comments: line : %d' %line
						exit(1)
					if c=='*'
						c=getChar()
						if c =='/':
							token, word = lex()
							return token, word
						state=COMMENT_TK
			elif c=='/':
				while 1:
					c=getChar()
					if c=='\n'
						token, word = lex()
						return token, word
					state=COMMENT_TK
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
				token=SMALLOREQUAL_TK
				return token,word
			else:
				backChar()
				token=SMALL_TK
				return token,c
				
		if c=='>':
			c=getChar()
			if c =='=':
				token=GREATOREQUAL_TK
				return token, '>='
			else:
				backChar()
				token=GREAT_TK
				return token,c
				
	else:
		print 'Found unrecognizable character in line %d!' %line
		exit(0)
		
				
				
				

	
		

