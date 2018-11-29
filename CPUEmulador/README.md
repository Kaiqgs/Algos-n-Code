# Emulador CPU
Projeto de Arquitetura de Computadores, sobre o funcionamento. Sem suporte para valores de ponto flutuante ou negativos.

## Instruction Set:
Todas instruções recebem apenas um operando, sendo um valor ou um endereço de memória. <br>
ender. = endereço da memória, valor. = valor real, indef. = indefinido (ou desnecessário);

HLT indef. -> Não faz nada, apenas passa um passo vazio; <br>
SET valor. -> Muda o valor do AC para o valor passado; <br>
LDD ender. -> Carrega valor do endereço da memória pro AC; <br>
STO ender. -> Guarda o valor do AC para a memória; <br>
JMP ender. -> Pula para o endereço de memória passado; <br>
JPC ender. -> Pula para o endereço de memória apenas se o AC for igual a 1 (True), é um pulo condicional; <br>
CEQ ender. -> Compara se valor do endereço de memória(argumento) tem valor igual ao do AC; <br>
CGT ender. -> Compara se valor do endereço da memória(argumento) tem valor maior que ao do AC; <br>
CGE ender. -> Compara se valor do endereço de memória(argumento) tem valor maior ou igual ao do AC; <br>
CLT ender. -> Compara se valor do endereço de memória(argumento) tem valor menor ao do AC; <br>
CLE ender. -> Compara se valor do endereço de memória(argumento) tem valor menor ou igual ao do AC; <br>
ADD ender. -> Adiciona o valor do endereço de memória(argumento) ao valor do AC; <br>
SUB ender. -> Subtrai o valor do endereço de memória(argumento) do valor do AC; <br>
MLT ender. -> Multiplica o valor do endereço de memória(argumento) com o valor do AC; <br>
DIV ender. -> Divide o valor do endereço de memória(argumento) com o valor do AC; <br>
CLR indef. -> Atribui ao AC o valor zero; <br>

### Especificações;
O opcode tem tamanho 4 bits e os dados 16 bits. Então o endereçamento total de 20 bits. A memória conta com 64 posições (20 * 64), podendo ser variável em código. As instruções são salvas em memória, junto com os operandos.
