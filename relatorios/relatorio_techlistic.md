# Relatório de Teste - Techlistic

## Caso de Teste: TC-000
**ID:** TC-000  
**Título:** Preenchimento de formulário no site techlistic.com

### Objetivo
Preencher um formulário completo, incluindo upload de imagem, e validar a submissão bem-sucedida.

### Passos Executados
1. Acessar o site https://www.techlistic.com/p/selenium-practice-form.html
2. Preencher o campo "First name" com "João"
3. Preencher o campo "Last name" com "Silva"
4. Selecionar o gênero "Male" (radio button)
5. Selecionar a experiência "3 years" (radio button)
6. Inserir a data "16/04/2025"
7. Selecionar a profissão "Automation Tester" (checkbox)
8. Selecionar a ferramenta "Selenium Webdriver" (checkbox)
9. Selecionar o continente "Europe" (dropdown)
10. Selecionar o comando "Browser Commands" (dropdown)
11. Fazer upload de uma imagem de teste
12. Submeter o formulário
13. Verificar o sucesso da submissão

### Dados de Entrada
- Primeiro nome: João
- Sobrenome: Silva
- Gênero: Male
- Experiência: 3 years
- Data: 16/04/2025
- Profissão: Automation Tester
- Ferramenta: Selenium Webdriver
- Continente: Europe
- Comando: Browser Commands
- Imagem: /home/ubuntu/projeto-selenium/resources/test_image.png (imagem de teste criada pelo script)

### Resultado Esperado
Após submeter o formulário, o sistema deve processar a submissão sem erros.

### Resultado Obtido
Formulário submetido com sucesso. O script verificou que a submissão foi processada corretamente.

### Status
**Passou**

### Tempo de Execução
Início: 23/04/2025 18:43:07  
Fim: 23/04/2025 18:43:13  
Duração: 5.04 segundos

---

## Observações Gerais
O teste de preenchimento de formulário no site techlistic.com foi executado com sucesso, incluindo a criação e upload de uma imagem de teste. O script conseguiu interagir com todos os tipos de elementos do formulário (campos de texto, radio buttons, checkboxes, dropdowns) e realizar o upload de arquivo. A submissão do formulário foi processada sem erros, indicando que o teste foi bem-sucedido.
