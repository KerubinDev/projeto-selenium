"""
Caso de Teste: TC-001 e TC-002 - Login no site saucedemo.com
Objetivo: 
    - TC-001: Realizar login bem-sucedido com usuário padrão
    - TC-002: Realizar login mal-sucedido com usuário inválido
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

# Configuração do WebDriver
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executar em modo headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service('/home/ubuntu/projeto-selenium/drivers/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver

def test_login_success():
    """TC-001: Login bem-sucedido com usuário padrão"""
    driver = setup_driver()
    
    try:
        # Registrar data/hora de início
        start_time = datetime.now()
        print(f"TC-001: Início do teste em {start_time.strftime('%d/%m/%Y %H:%M:%S')}")
        
        # Acessar o site
        driver.get("https://www.saucedemo.com/")
        
        # Preencher credenciais
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        # Clicar no botão de login
        driver.find_element(By.ID, "login-button").click()
        
        # Verificar se o login foi bem-sucedido (verificando se a página de produtos foi carregada)
        time.sleep(2)  # Aguardar carregamento da página
        
        # Verificar se o elemento inventory_container está presente (indica página de produtos)
        success = driver.find_element(By.ID, "inventory_container").is_displayed()
        
        # Registrar resultado
        if success:
            print("TC-001: Login bem-sucedido! Página de produtos exibida.")
            result = "Passou"
        else:
            print("TC-001: Falha no login. Página de produtos não foi exibida.")
            result = "Falhou"
        
        # Registrar data/hora de fim
        end_time = datetime.now()
        print(f"TC-001: Fim do teste em {end_time.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"TC-001: Duração do teste: {(end_time - start_time).total_seconds()} segundos")
        
        return {
            "caso_teste": "TC-001",
            "objetivo": "Login bem-sucedido com usuário padrão",
            "inicio": start_time.strftime('%d/%m/%Y %H:%M:%S'),
            "fim": end_time.strftime('%d/%m/%Y %H:%M:%S'),
            "duracao": f"{(end_time - start_time).total_seconds()} segundos",
            "resultado": result,
            "mensagem": "Página de produtos exibida com sucesso" if success else "Falha ao exibir página de produtos"
        }
        
    except Exception as e:
        print(f"TC-001: Erro durante o teste: {str(e)}")
        end_time = datetime.now()
        return {
            "caso_teste": "TC-001",
            "objetivo": "Login bem-sucedido com usuário padrão",
            "inicio": start_time.strftime('%d/%m/%Y %H:%M:%S'),
            "fim": end_time.strftime('%d/%m/%Y %H:%M:%S'),
            "duracao": f"{(end_time - start_time).total_seconds()} segundos",
            "resultado": "Falhou",
            "mensagem": f"Erro: {str(e)}"
        }
    finally:
        driver.quit()

def test_login_failure():
    """TC-002: Login mal-sucedido com usuário inválido"""
    driver = setup_driver()
    
    try:
        # Registrar data/hora de início
        start_time = datetime.now()
        print(f"TC-002: Início do teste em {start_time.strftime('%d/%m/%Y %H:%M:%S')}")
        
        # Acessar o site
        driver.get("https://www.saucedemo.com/")
        
        # Preencher credenciais inválidas
        driver.find_element(By.ID, "user-name").send_keys("invalid_user")
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        
        # Clicar no botão de login
        driver.find_element(By.ID, "login-button").click()
        
        # Verificar se o login falhou (verificando a mensagem de erro)
        time.sleep(2)  # Aguardar exibição da mensagem
        
        # Verificar se o elemento error-message-container está presente e capturar a mensagem
        error_element = driver.find_element(By.CSS_SELECTOR, ".error-message-container")
        error_message = error_element.text
        
        # Registrar resultado
        if "Epic sadface" in error_message:
            print(f"TC-002: Login falhou conforme esperado. Mensagem: {error_message}")
            result = "Passou"
        else:
            print(f"TC-002: Teste falhou. Mensagem de erro não encontrada ou inesperada: {error_message}")
            result = "Falhou"
        
        # Registrar data/hora de fim
        end_time = datetime.now()
        print(f"TC-002: Fim do teste em {end_time.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"TC-002: Duração do teste: {(end_time - start_time).total_seconds()} segundos")
        
        return {
            "caso_teste": "TC-002",
            "objetivo": "Login mal-sucedido com usuário inválido",
            "inicio": start_time.strftime('%d/%m/%Y %H:%M:%S'),
            "fim": end_time.strftime('%d/%m/%Y %H:%M:%S'),
            "duracao": f"{(end_time - start_time).total_seconds()} segundos",
            "resultado": result,
            "mensagem": error_message
        }
        
    except Exception as e:
        print(f"TC-002: Erro durante o teste: {str(e)}")
        end_time = datetime.now()
        return {
            "caso_teste": "TC-002",
            "objetivo": "Login mal-sucedido com usuário inválido",
            "inicio": start_time.strftime('%d/%m/%Y %H:%M:%S'),
            "fim": end_time.strftime('%d/%m/%Y %H:%M:%S'),
            "duracao": f"{(end_time - start_time).total_seconds()} segundos",
            "resultado": "Falhou",
            "mensagem": f"Erro: {str(e)}"
        }
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Iniciando testes de login no site saucedemo.com...")
    
    # Executar TC-001: Login bem-sucedido
    resultado_tc001 = test_login_success()
    
    # Executar TC-002: Login mal-sucedido
    resultado_tc002 = test_login_failure()
    
    print("\nResumo dos testes:")
    print(f"TC-001: {resultado_tc001['resultado']} - {resultado_tc001['mensagem']}")
    print(f"TC-002: {resultado_tc002['resultado']} - {resultado_tc002['mensagem']}")
    
    print("\nTestes concluídos!")
