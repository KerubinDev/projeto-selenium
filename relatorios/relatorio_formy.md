# Relatório de Teste - Formy

## Caso de Teste: TC-005
**ID:** TC-005  
**Título:** Preenchimento de formulário no site formy-project.herokuapp.com

### Objetivo
Preencher todos os campos do formulário e validar a submissão bem-sucedida.

### Passos Executados
1. Acessar o site https://formy-project.herokuapp.com/form
2. Preencher o campo "First name" com "João"
3. Preencher o campo "Last name" com "Silva"
4. Preencher o campo "Job title" com "Engenheiro de Testes"
5. Selecionar o nível de educação "College" (radio button)
6. Selecionar o gênero "Male" (checkbox)
7. Selecionar a opção de experiência (radio button)
8. Preencher o campo de data com "01/15/2025"
9. Clicar no botão "Submit"
10. Validar a mensagem de sucesso

### Dados de Entrada
- First name: João
- Last name: Silva
- Job title: Engenheiro de Testes
- Education level: College
- Gender: Male
- Experience: Opção alternativa selecionada
- Date: 01/15/2025

### Resultado Esperado
Após submeter o formulário, o sistema deve exibir uma mensagem de sucesso indicando que o formulário foi enviado com sucesso.

### Resultado Obtido
Formulário submetido com sucesso. O sistema exibiu a mensagem "The form was successfully submitted!".

### Status
**Passou**

### Tempo de Execução
Início: 23/04/2025 18:42:56  
Fim: 23/04/2025 18:42:58  
Duração: 2.22 segundos

---

## Observações Gerais
O teste de preenchimento de formulário foi executado com sucesso após ajustes na estratégia de localização dos elementos, especialmente para o campo de experiência. Foram implementadas múltiplas estratégias de localização para garantir a robustez do teste. O sistema respondeu conforme esperado, exibindo a mensagem de sucesso após a submissão do formulário.
