# Desafio_sistema_bancario_Santander_bootCamp

💰 Sistema Bancário em Python

Este projeto apresenta um sistema bancário simples desenvolvido em Python, utilizando lógica condicional e loops para simular operações básicas de uma conta corrente.

🧠 Funcionalidades

O sistema oferece as seguintes opções para o usuário:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

[1] Depositar

- Permite adicionar fundos à conta.
- Só aceita valores positivos.
- Registra o depósito no extrato.

[2] Sacar

- Permite fazer retiradas de dinheiro.
- Valida múltiplos critérios:
- Se o valor excede o saldo + crédito disponível.
- Se ultrapassa o limite por saque (R$ 2500).
- Se já foram feitos 3 saques no dia.
- O saldo pode ficar negativo, indicando uso do limite de crédito.

[3] Extrato

- Exibe todas as movimentações (depósitos e saques).
- Mostra o saldo atual e, se necessário, o crédito utilizado.

[4] Sair

- Encerra a operação com uma mensagem de agradecimento.

🔒 Regras do Sistema

- 💸 Limite por saque: R$ 2500
- 🔁 Número máximo de saques: 3 por sessão
- 🧾 Limite de crédito disponível: R$ 200

🚀 Como Executar

Basta rodar o script Python no terminal:

python sistema_bancario.py


📌 Requisitos

- Python 3 instalado
- Terminal ou IDE para executar scripts .py

