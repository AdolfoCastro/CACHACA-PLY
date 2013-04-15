def p_expresion_1(t):
	'''expresion_1 : MIN exp
				   | MIN_EQ exp
			 	   | MAY exp
				   | MAY_EQ exp
				   | DIF exp
				   | EQ_EQ exp
				   | empty
				   '''