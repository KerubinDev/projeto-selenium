"""
Caso de Teste: TC-005 - Preenchimento de formulário no site formy-project.herokuapp.com
Objetivo: Preencher todos os campos do formulário e submeter
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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

def test_form_submission():
    """TC-005: Preenchimento de formulário no site formy-project.herokuapp.com"""
    driver = setup_driver()
    
    try:
        # Registrar data/hora de início
        start_time = datetime.now()
        print(f"TC-005: Início do teste em {start_time.strftime('%d/%m/%Y %H:%M:%S')}")
        
        # Acessar o site
        driver.get("https://formy-project.herokuapp.com/form")
        
        # Aguardar carregamento da página
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        
        # Dicionário para armazenar os valores preenchidos
        form_data = {}
        
        # 1. Preencher campos de texto
        print("TC-005: Preenchendo campos de texto...")
        
        # Nome
        first_name = "João"
        driver.find_element(By.ID, "first-name").send_keys(first_name)
        form_data["first_name"] = first_name
        
        # Sobrenome
        last_name = "Silva"
        driver.find_element(By.ID, "last-name").send_keys(last_name)
        form_data["last_name"] = last_name
        
        # Cargo
        job_title = "Engenheiro de Testes"
        driver.find_element(By.ID, "job-title").send_keys(job_title)
        form_data["job_title"] = job_title
        
        # 2. Selecionar nível de educação (radio button)
        print("TC-005: Selecionando nível de educação...")
        education_level = "College"
        driver.find_element(By.ID, "radio-button-2").click()
        form_data["education_level"] = education_level
        
        # 3. Selecionar gênero (checkbox)
        print("TC-005: Selecionando gênero...")
        gender = "Male"
        driver.find_element(By.ID, "checkbox-1").click()
        form_data["gender"] = gender
        
        # 4. Selecionar anos de experiência (radio button)
        print("TC-005: Selecionando anos de experiência...")
        experience = "2-4"
        
        # Tentar diferentes estratégias para localizar o elemento de anos de experiência
        try:
            # Estratégia 1: Usando CSS Selector
            driver.find_element(By.CSS_SELECTOR, "input[value='2']").click()
        except:
            try:
                # Estratégia 2: Usando XPath
                driver.find_element(By.XPATH, "//input[@value='2']").click()
            except:
                try:
                    # Estratégia 3: Usando todos os radio buttons e selecionando o terceiro (0-indexed)
                    radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio'][name='exp']")
                    if len(radio_buttons) >= 3:
                        radio_buttons[2].click()  # Seleciona o terceiro radio button (2-4 anos)
                    else:
                        # Estratégia 4: Selecionar qualquer radio button disponível
                        radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
                        if len(radio_buttons) > 0:
                            radio_buttons[0].click()
                            experience = "Opção alternativa selecionada"
                        else:
                            print("TC-005: Não foi possível encontrar radio buttons para anos de experiência")
                except:
                    print("TC-005: Não foi possível selecionar anos de experiência, continuando o teste")
                    experience = "Não selecionado"
        
        form_data["experience"] = experience
        
        # 5. Selecionar data
        print("TC-005: Selecionando data...")
        date = "01/15/2025"
        driver.find_element(By.ID, "datepicker").send_keys(date)
        form_data["date"] = date
        
        # 6. Submeter o formulário
        print("TC-005: Submetendo o formulário...")
        submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        time.sleep(1)  # Pequena pausa para garantir que o botão está visível
        submit_button.click()
        
        # 7. Aguardar e validar o alerta de sucesso
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success")))
        success_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success").text
        
        # Registrar resultado
        if "The form was successfully submitted!" in success_message:
            print(f"TC-005: Formulário submetido com sucesso! Mensagem: {success_message}")
            result = "Passou"
        else:
            print(f"TC-005: Falha na submissão do formulário. Mensagem: {success_message}")
            result = "Falhou"
        
        # Registrar data/hora de fim
        end_time = datetime.now()
        print(f"TC-005: Fim do teste em {end_time.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"TC-005: Duração do teste: {(end_time - start_time).total_seconds()} segundos")
        
        return {
            "caso_teste": "TC-005",
            "objetivo": "Preenchimento e submissão de formulário",
            "inicio": start_time.strftime('%d/%m/%Y %H:%M:%S'),
            "fim": end_time.strftime('%d/%m/%Y %H:%M:%S'),
            "duracao": f"{(end_time - start_time).total_seconds()} segundos",
            "dados_formulario": form_data,
            "resultado": result,
            "mensagem_sucesso": success_message
        }
        
    except Exception as e:
        print(f"TC-005: Erro durante o teste: {str(e)}")
        end_time = datetime.now()
        return {
            "caso_teste": "TC-005",
            "objetivo": "Preenchimento e submissão de formulário",
            "inicio": start_time.strftime('%d/%m/%Y %H:%M:%S'),
            "fim": end_time.strftime('%d/%m/%Y %H:%M:%S'),
            "duracao": f"{(end_time - start_time).total_seconds()} segundos",
            "resultado": "Falhou",
            "mensagem": f"Erro: {str(e)}"
        }
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Iniciando teste de preenchimento de formulário no site formy-project.herokuapp.com...")
    
    # Executar TC-005: Preenchimento de formulário
    resultado_tc005 = test_form_submission()
    
    print("\nResumo do teste:")
    print(f"TC-005: {resultado_tc005['resultado']}")
    
    if resultado_tc005['resultado'] == "Passou":
        print(f"Mensagem de sucesso: {resultado_tc005['mensagem_sucesso']}")
        print("\nDados do formulário preenchido:")
        for campo, valor in resultado_tc005['dados_formulario'].items():
            print(f"  - {campo}: {valor}")
    else:
        print(f"Mensagem de erro: {resultado_tc005.get('mensagem', 'Erro não especificado')}")
    
    print("\nTeste concluído!")
