"""
Caso de Teste: TC-003 - Carregamento dinâmico no site the-internet.herokuapp.com
Objetivo: Clicar no botão Start, aguardar até o texto "Hello World!" estar visível e validar sua presença
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def test_dynamic_loading():
    """TC-003: Teste de carregamento dinâmico"""
    driver = setup_driver()
    
    try:
        # Registrar data/hora de início
        start_time = datetime.now()
        print(f"TC-003: Início do teste em {start_time.strftime('%d/%m/%Y %H:%M:%S')}")
        
        # Acessar o site
        driver.get("https://the-internet.herokuapp.com/dynamic_loading")
        
        # Clicar no link "Example 1: Element on page that is hidden"
        driver.find_element(By.XPATH, "//a[contains(text(), 'Example 1')]").click()
        
        # Clicar no botão Start
        driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]").click()
        
        # Registrar tempo antes de iniciar a espera
        wait_start_time = datetime.now()
        
        # Configurar explicit wait para aguardar até 30 segundos
        wait = WebDriverWait(driver, 30)
        
        # Aguardar até que o elemento com o texto "Hello World!" esteja visível
        hello_world_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'Hello World!')]"))
        )
        
        # Registrar tempo após a espera
        wait_end_time = datetime.now()
        wait_duration = (wait_end_time - wait_start_time).total_seconds()
        
        # Verificar se o texto está presente
        hello_world_text = hello_world_element.text
        
        # Registrar resultado
        if "Hello World!" in hello_world_text:
            print(f"TC-003: Texto 'Hello World!' encontrado após {wait_duration} segundos de espera.")
            result = "Passou"
        else:
            print(f"TC-003: Texto 'Hello World!' não encontrado após {wait_duration} segundos de espera.")
            result = "Falhou"
        
        # Registrar data/hora de fim
        end_time = datetime.now()
        print(f"TC-003: Fim do teste em {end_time.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"TC-003: Duração total do teste: {(end_time - start_time).total_seconds()} segundos")
        print(f"TC-003: Tempo de espera pelo carregamento: {wait_duration} segundos")
        
        return {
            "caso_teste": "TC-003",
            "objetivo": "Aguardar carregamento dinâmico e validar texto",
            "inicio": start_time.strftime('%d/%m/%Y %H:%M:%S'),
            "fim": end_time.strftime('%d/%m/%Y %H:%M:%S'),
            "duracao_total": f"{(end_time - start_time).total_seconds()} segundos",
            "tempo_espera": f"{wait_duration} segundos",
            "resultado": result,
            "mensagem": f"Texto '{hello_world_text}' encontrado com sucesso" if result == "Passou" else "Texto 'Hello World!' não encontrado"
        }
        
    except Exception as e:
        print(f"TC-003: Erro durante o teste: {str(e)}")
        end_time = datetime.now()
        return {
            "caso_teste": "TC-003",
            "objetivo": "Aguardar carregamento dinâmico e validar texto",
            "inicio": start_time.strftime('%d/%m/%Y %H:%M:%S'),
            "fim": end_time.strftime('%d/%m/%Y %H:%M:%S'),
            "duracao_total": f"{(end_time - start_time).total_seconds()} segundos",
            "tempo_espera": "N/A - Erro durante a espera",
            "resultado": "Falhou",
            "mensagem": f"Erro: {str(e)}"
        }
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Iniciando teste de carregamento dinâmico...")
    
    # Executar TC-003: Carregamento dinâmico
    resultado_tc003 = test_dynamic_loading()
    
    print("\nResumo do teste:")
    print(f"TC-003: {resultado_tc003['resultado']} - {resultado_tc003['mensagem']}")
    print(f"Tempo de espera: {resultado_tc003['tempo_espera']}")
    
    print("\nTeste concluído!")
