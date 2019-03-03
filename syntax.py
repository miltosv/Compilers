def program()
	token=lex()
	if token==PROGRAM_TK
		token=lex()
		if token==ID_TK
			token=lex();
			block();
		else 
			print ("Program Name expected at line",line)
			exit(0)
	else error("the keyword program was expected at line,line)
	exit(0)

def block()
	declarations()
	subprograms()
	statements()

def declarations()
	if token==DECLARATIONS_TK
		varlist()
	else
		print("Expected word 'declare' at line",line)
		exit(0)
		
def varlist()
	varlist()
	tokenk=lex()
	while token==COMMA_TK
		token=lex()
		
		if token!=ID_TK
		print("Expected ID", line)
		exit(0)
	else
		return

def subprograms()
	while token==FUNCTION_TK
		subprogram()
		token=lex()
	
def subprogram()
	token=lex()
	if token!=ID_TK
		print("error in line",line,"function id expected")
		exit()
	funcbody()
	
def funcbody()
	formalpars()
	block()

def formalpars()
	token=lex()
	if token!=OPENPAR_TK
		print("error in line",line)
		exit(0)
	token=lex()
	if token==IN_TK or token==INANDOUT_TK or token==INOUT_TK
		formalparlist()
		
	token=lex()
	if token!=CLOSEPAR_TK
		print("error, expected ')', line" line)
		exit(0)

def formalparlist()
	token=lex()
	formalparitem()
	token=lex()
	while token=COMMA_TK
		
		formalparitem()
		token=lex()
	return token		
	
def formalparitem()
	if token!=ID_TK
		print("error, expected ID at line", line)
		exit(0)
	
def statements()
	statement()
	token=lex()
	if token==SEMICOLON_TK
		statements()
	
def statement()
	
	if token=ID_TK
		token=lex()
	if token=IF_STAT
		token=lex()
		if_stat()
	if token=WHILE_TK
		token=lex()
		while_stat()
	if token=DO_TK
		token=lex()
		do_stat()
	
		
	