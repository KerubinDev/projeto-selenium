# Relatório de Teste - Demoblaze

## Caso de Teste: TC-004
**ID:** TC-004  
**Título:** Simulação de compra no site demoblaze.com

### Objetivo
Simular uma compra completa de um produto, desde a seleção até a confirmação do pedido.

### Passos Executados
1. Acessar o site https://www.demoblaze.com/
2. Escolher um produto da lista (Samsung galaxy s6)
3. Clicar no botão "Add to cart"
4. Aceitar o alerta de confirmação
5. Navegar para o carrinho
6. Clicar em "Place Order"
7. Preencher o formulário de cadastro com os dados do cliente
8. Confirmar a compra
9. Validar a mensagem de confirmação e capturar o ID do pedido e valor

### Dados de Entrada
- Produto: Samsung galaxy s6
- Nome: João Silva
- País: Brasil
- Cidade: São Paulo
- Cartão de crédito: 4111111111111111
- Mês: 12
- Ano: 2025

### Resultado Esperado
Após confirmar a compra, o sistema deve exibir uma mensagem de confirmação com o ID do pedido e o valor total.

### Resultado Obtido
Compra realizada com sucesso. O sistema exibiu a mensagem "Thank you for your purchase!" e forneceu os seguintes detalhes:
- ID do pedido: 2174232
- Valor: 360 USD

### Status
**Passou**

### Tempo de Execução
Início: 23/04/2025 18:41:12  
Fim: 23/04/2025 18:41:29  
Duração: 16.63 segundos

---

## Observações Gerais
O teste de simulação de compra foi executado com sucesso após ajustes na estratégia de localização dos elementos. O sistema respondeu conforme esperado em todas as etapas do processo de compra, desde a seleção do produto até a confirmação do pedido, gerando um ID único e exibindo o valor total da compra.
