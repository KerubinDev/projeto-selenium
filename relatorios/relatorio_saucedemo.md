# Relatório de Teste - Saucedemo

## Caso de Teste: TC-001
**ID:** TC-001  
**Título:** Login bem-sucedido no site saucedemo.com

### Objetivo
Verificar se é possível realizar login com sucesso utilizando credenciais válidas.

### Passos Executados
1. Acessar o site https://www.saucedemo.com/
2. Preencher o campo de usuário com "standard_user"
3. Preencher o campo de senha com "secret_sauce"
4. Clicar no botão de login
5. Verificar se a página de produtos é exibida

### Dados de Entrada
- Usuário: standard_user
- Senha: secret_sauce

### Resultado Esperado
Após o login, o usuário deve ser redirecionado para a página de produtos, identificada pela presença do elemento com ID "inventory_container".

### Resultado Obtido
Login realizado com sucesso. A página de produtos foi exibida corretamente, confirmada pela presença do elemento "inventory_container".

### Status
**Passou**

### Tempo de Execução
Início: 23/04/2025 18:39:22  
Fim: 23/04/2025 18:39:24  
Duração: 2.80 segundos

---

## Caso de Teste: TC-002
**ID:** TC-002  
**Título:** Login mal-sucedido no site saucedemo.com

### Objetivo
Verificar se o sistema exibe mensagem de erro apropriada ao tentar login com credenciais inválidas.

### Passos Executados
1. Acessar o site https://www.saucedemo.com/
2. Preencher o campo de usuário com "invalid_user"
3. Preencher o campo de senha com "wrong_password"
4. Clicar no botão de login
5. Verificar se a mensagem de erro é exibida

### Dados de Entrada
- Usuário: invalid_user
- Senha: wrong_password

### Resultado Esperado
O sistema deve exibir uma mensagem de erro indicando que as credenciais são inválidas.

### Resultado Obtido
O sistema exibiu a mensagem de erro esperada: "Epic sadface: Username and password do not match any user in this service"

### Status
**Passou**

### Tempo de Execução
Início: 23/04/2025 18:39:25  
Fim: 23/04/2025 18:39:28  
Duração: 2.71 segundos

---

## Observações Gerais
Os testes de login no site saucedemo.com foram executados com sucesso, validando tanto o cenário de login bem-sucedido quanto o cenário de login mal-sucedido. O sistema respondeu conforme esperado em ambos os casos, exibindo a página de produtos após login bem-sucedido e a mensagem de erro apropriada após tentativa de login com credenciais inválidas.
