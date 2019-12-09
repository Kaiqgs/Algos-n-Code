DECLARA a, b, c, delta, delta_parc, x1, x2: REAL
LEIA(a, b, c) 										// 1cl + 1co + 1co + 1co
SE(A!=0) ENTAO: 									// 1cl + 1co
	delta_parc = b - 4 * a * c						// 1cl + 1co + 1co + 1co + 1co
	delta = b *delta_parc							// 1cl + 1co + 1co

	SE(delta >= 0) ENTAO:							// 1cl + 1co
		X1 = (-b + SQRT(delta))/(2*a)				// 1cl + 1co + 1co + 1co + 1co + 1co + 1co
		X2 = (-b - SQRT(delta))/(2*a)				// 1cl + 1co + 1co + 1co + 1co + 1co + 1co
		IMPRIMA("RAIZES")							// 1cl + 1co 
													// f(n) = 8cl + 24co
	SENÃO
		IMPRIMA("DELTA NEGATIVO")					// 1cl + 1co
													// f(n) = 5cl + 11co
	FIMSE
SENÃO
	X1 = -c/b										// 1cl + 1co + 1co + 1co
	IMPRIMA("Teste")								// 1cl + 1co
													// f(n) = 4cl + 7co
FIMSE
FIM

~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~

melhor f(n) = 4cl + 8co
pior f(n) 8cl + 24co
assintótica_f(n) = co || assintótica_f(n) = 1

