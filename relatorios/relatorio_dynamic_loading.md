# Relatório de Teste - Dynamic Loading

## Caso de Teste: TC-003
**ID:** TC-003  
**Título:** Carregamento dinâmico no site the-internet.herokuapp.com

### Objetivo
Verificar se o sistema aguarda corretamente o carregamento dinâmico de um elemento e valida sua presença após o carregamento.

### Passos Executados
1. Acessar o site https://the-internet.herokuapp.com/dynamic_loading
2. Clicar no link "Example 1: Element on page that is hidden"
3. Clicar no botão "Start"
4. Aguardar até que o texto "Hello World!" esteja visível
5. Validar a presença do texto "Hello World!"
6. Registrar o tempo total de espera

### Dados de Entrada
- Não aplicável (apenas interações com elementos da página)

### Resultado Esperado
Após clicar no botão "Start", o sistema deve aguardar o carregamento e exibir o texto "Hello World!".

### Resultado Obtido
O texto "Hello World!" foi encontrado com sucesso após 5.27 segundos de espera.

### Status
**Passou**

### Tempo de Execução
Início: 23/04/2025 18:39:38  
Fim: 23/04/2025 18:39:44  
Duração total: 5.81 segundos  
Tempo de espera pelo carregamento: 5.27 segundos

---

## Observações Gerais
O teste de carregamento dinâmico foi executado com sucesso, utilizando explicit waits para aguardar o aparecimento do elemento. O WebDriverWait foi configurado com um timeout de 30 segundos, mas o elemento foi encontrado em aproximadamente 5.27 segundos, demonstrando que o sistema respondeu dentro de um tempo razoável.
