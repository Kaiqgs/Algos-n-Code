DECLARA nota, total, media, qtde: NUMERO
IMPRIMA("Digite a quantidade de notas")			// 1cl + 1co
LEIA(qtde);										// 1cl + 1co
total = 0										// 1cl + 1co
												// f(n) = 3cl + 3co

PARA I de 1 ATÉ qtde FAÇA:						// 1cl + 1co + 1co + n *
	IMPRIMA("Digite uma nota")					// ( 1cl + 1co
	LEIA(nota) 									// 1cl + 1co
	total = total + nota 						// 1cl + 1co + 1co | 3cl + 4co) 
												
												// f(n) = 4cl + 5co + n * 3cl + n * 4co
media = total/qtde 								// 1cl + 1co + 1co

IMPRIMA("A média foi:")							// 1cl + 1co
IMPRIMA(media)									// 1cl + 1co


SE(media >= 7) ENTÃO:							// 1cl + 1co
	ESCREVA "Aprovado"							// 1cl + 1co
SE(media < 4) ENTÃO:							// 1cl + 1co
	ESCREVA "REPROVADO"							// 1cl + 1co
SE(media >= 4) ENTÃO:							// 1cl + 1co
	ESCREVA "Precisa fazer prova final"			// 1cl + 1co

												// f(n) = 13cl + 15co + n * 3cl + n * 4co

~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~

melhor_f(n) = 13cl + 15co
pior_f(n) = 13cl + 15co + n * 3cl + n * 4co
assintótica_f(n) = n