DECLARA n, p, pf, valor, indice_do_tipo: INTEIRO
p = 1							// 1cl + 1co
r = n							// 1cl + 1co
x = valor_digitado				// 1cl + 1co
								
ENQUANTO(p <= r) FAÇA:			// 1cl + (1 + log2(n)) * ( 1co
	q = (p+r)/2					// 1cl + 1co + 1co + 1co
	SE(A[q] == x):				// 1cl + 1co
		IMPRIMA("Encontrado")	// 1cl + 1co
		PARE					// 1cl
	SENÃO:
		SE(A[q] < x) ENTÃO:		// 1cl + 1co
			p = q				// 1cl + 1co
		SENÃO:
			r = q				// 1cl + 1co )
		FIMSE
	FIMSE
FIMENQUANTO

~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~

melhor f(n) = 8cl + 9co
//temos um algoritmo que varia 'q' de forma logarítmica
pior f(n) = 8cl + 9co + (1 + log2(n)) * 