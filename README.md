# app_logistica_voo
Essa empresa trabalha com encomendas de pequeno e médio porte e opera somente entre 3 cidades.
O valor que a empresa cobra por objeto é dado pela seguinte equação: Total = dimensões * peso * rota

Quadro 1: Dimensões versus Valor
*dimensões (cm³) valor (R$)*
Até 1000 10
Entre 1001 e 10000 20
Entre 10001 e 30000 30
Entre 30001 e 100000 50
Acima Não é aceito

Quadro 2: Peso versus multiplicador
*peso(kg) multiplicador*
Até 0.1 1
Entre 0.11 e 1 1.5
Entre 1.10 e 10 2
Entre 10.1 e 30 3
Acima de 30 Não é aceito

Quadro 3: Rota versus multiplicador
*rota multiplicador*
RS - De Rio de Janeiro até São Paulo 1
SR - De São Paulo até Rio de Janeiro 1
BS - De Brasília até São Paulo 1.2
SB - De São Paulo até Brasília 1.2
BR - De Brasília até Rio de Janeiro 1.5
RB - Rio de Janeiro até Brasília 1.5

Elabore um programa em Python que:
1. Pergunte a altura (em cm), comprimento (em cm) e largura (em cm) do objeto. Se digitar um valor não numérico e/ou as dimensões passarem do limite aceito repetir a pergunta;
2. Pergunte o peso do objeto (em kg). Se digitar um valor não numérico e/ou o peso passar do limite aceito repetir a pergunta;
3. Pergunte a rota do objeto. Se digitar uma opção que não esteja na tabela repetir a pergunta;
4. Encerre o total a ser pago com base na equação desse enunciado;
5. Deve-se codificar uma função dimensoesObejto;
  o Dentro da função perguntar altura do objeto (em cm);
  o Dentro da função perguntar o comprimento do objeto (em cm);
  o Dentro da função perguntar a largura do objeto (em cm)
  o Calcular o volume (em cm) da caixa para objeto (altura * largura * comprimento);
  Deve-se ter um try/except para o caso de o usuário digitar um valor não numérico;
  o Deve-se retornar o valor em (RS) conforme a Quadro 1
6. Deve-se codificar uma função pesoObejto;
  o Dentro da função perguntar peso do objeto (em kg);
  o Deve-se ter um try/except para o caso de o usuário digitar um valor não numérico;
  o Deve-se retornar o multiplicador conforme o Quadro 2
7. Deve-se codificar uma função rotaObjeto;
  o Dentro da função perguntar a rota do objeto desejada (Sugestão: utilize as siglas para facilitar os testes);
  o OBS: PODE MUDAR O NOME DAS CIDADES E SUAS SIGLAS
  o Deve-se retornar o multiplicador conforme o Quadro 3
