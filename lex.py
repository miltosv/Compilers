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
LOOPFOREVER_TK='loopforevertk'
ENDLOOP_TK='endlooptk'
EXIT_TK='exittk'
FORCASE_TK='forcasetk'
ENDFORCASE_TK='endforcasetk'
INCASE_TK='incasetk'
ENDINCASE_TK='endincasetk'
WHEN_TK='whentk'
ENDWHEN_TK='endwhentk'




def getChar()
	c=f.read(1)
	return c
	

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
	if word=="loopforever":
		return LOOPFOREVER_TK,word
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
	if word=="endwhen":
		return ENDWHEN_TK,word
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

		

