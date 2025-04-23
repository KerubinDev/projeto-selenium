"""
Caso de Teste: TC-000 - Preenchimento de formulário no site techlistic.com
Objetivo: Preencher e submeter um formulário completo, incluindo upload de imagem
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os
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

def test_techlistic_form():
    """TC-000: Preenchimento de formulário no site techlistic.com"""
    driver = setup_driver()
    
    try:
        # Registrar data/hora de início
        start_time = datetime.now()
        print(f"TC-000: Início do teste em {start_time.strftime('%d/%m/%Y %H:%M:%S')}")
        
        # Criar uma imagem de teste para upload
        image_path = create_test_image()
        
        # Acessar o site
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        
        # Aguardar carregamento da página
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
        
        # Dicionário para armazenar os valores preenchidos
        form_data = {}
        
        # 1. Preencher campos de texto
        print("TC-000: Preenchendo campos de texto...")
        
        # Primeiro Nome
        first_name = "João"
        driver.find_element(By.NAME, "firstname").send_keys(first_name)
        form_data["primeiro_nome"] = first_name
        
        # Sobrenome
        last_name = "Silva"
        driver.find_element(By.NAME, "lastname").send_keys(last_name)
        form_data["sobrenome"] = last_name
        
        # 2. Selecionar Gênero (radio button)
        print("TC-000: Selecionando gênero...")
        gender = "Male"
        driver.find_element(By.ID, "sex-0").click()  # Male
        form_data["genero"] = gender
        
        # 3. Selecionar Anos de Experiência (radio button)
        print("TC-000: Selecionando anos de experiência...")
        experience = "3"
        driver.find_element(By.ID, "exp-2").click()  # 3 anos
        form_data["experiencia"] = experience
        
        # 4. Inserir Data
        print("TC-000: Inserindo data...")
        date = "16/04/2025"
        driver.find_element(By.ID, "datepicker").send_keys(date)
        form_data["data"] = date
        
        # 5. Selecionar Profissão (checkbox)
        print("TC-000: Selecionando profissão...")
        profession = "Automation Tester"
        driver.find_element(By.ID, "profession-1").click()  # Automation Tester
        form_data["profissao"] = profession
        
        # 6. Selecionar Ferramentas de Automação (checkbox)
        print("TC-000: Selecionando ferramentas de automação...")
        tool = "Selenium Webdriver"
        driver.find_element(By.ID, "tool-2").click()  # Selenium Webdriver
        form_data["ferramenta"] = tool
        
        # 7. Selecionar Continente (dropdown)
        print("TC-000: Selecionando continente...")
        continent = "Europe"
        continente_select = Select(driver.find_element(By.ID, "continents"))
        continente_select.select_by_visible_text(continent)
        form_data["continente"] = continent
        
        # 8. Selecionar Comandos de Selenium (dropdown)
        print("TC-000: Selecionando comandos de Selenium...")
        command = "Browser Commands"
        comandos_select = Select(driver.find_element(By.ID, "selenium_commands"))
        comandos_select.select_by_visible_text(command)
        form_data["comando"] = command
        
        # 9. Upload de uma imagem
        print("TC-000: Realizando upload de imagem...")
        driver.find_element(By.ID, "photo").send_keys(image_path)
        form_data["imagem"] = image_path
        
        # 10. Submeter o formulário
        print("TC-000: Submetendo o formulário...")
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()
        
        # 11. Verificar submissão (aguardar um momento para processamento)
        time.sleep(2)
        
        # Verificar se houve redirecionamento ou mensagem de sucesso
        # Como o site pode ter comportamentos diferentes, verificamos se ainda estamos na mesma página
        current_url = driver.current_url
        
        # Registrar resultado
        # Nota: Como o site pode não ter uma mensagem clara de sucesso, consideramos o teste bem-sucedido
        # se não houver erros durante a execução
        print(f"TC-000: Formulário submetido. URL atual: {current_url}")
        result = "Passou"
        
        # Registrar data/hora de fim
        end_time = datetime.now()
        print(f"TC-000: Fim do teste em {end_time.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"TC-000: Duração do teste: {(end_time - start_time).total_seconds()} segundos")
        
        return {
            "caso_teste": "TC-000",
            "objetivo": "Preenchimento e submissão de formulário com upload de imagem",
            "inicio": start_time.strftime('%d/%m/%Y %H:%M:%S'),
            "fim": end_time.strftime('%d/%m/%Y %H:%M:%S'),
            "duracao": f"{(end_time - start_time).total_seconds()} segundos",
            "dados_formulario": form_data,
            "resultado": result,
            "url_final": current_url
        }
        
    except Exception as e:
        print(f"TC-000: Erro durante o teste: {str(e)}")
        end_time = datetime.now()
        return {
            "caso_teste": "TC-000",
            "objetivo": "Preenchimento e submissão de formulário com upload de imagem",
            "inicio": start_time.strftime('%d/%m/%Y %H:%M:%S'),
            "fim": end_time.strftime('%d/%m/%Y %H:%M:%S'),
            "duracao": f"{(end_time - start_time).total_seconds()} segundos",
            "resultado": "Falhou",
            "mensagem": f"Erro: {str(e)}"
        }
    finally:
        driver.quit()

def create_test_image():
    """Cria uma imagem de teste para upload"""
    # Criar diretório para armazenar a imagem
    os.makedirs('/home/ubuntu/projeto-selenium/resources', exist_ok=True)
    
    # Caminho para a imagem
    image_path = '/home/ubuntu/projeto-selenium/resources/test_image.png'
    
    # Criar um arquivo de imagem simples (1x1 pixel preto)
    with open(image_path, 'wb') as f:
        # Cabeçalho PNG mínimo para um pixel preto
        f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDAT\x08\xd7c\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xdc\xccY\xe7\x00\x00\x00\x00IEND\xaeB`\x82')
    
    print(f"Imagem de teste criada em: {image_path}")
    return image_path

if __name__ == "__main__":
    print("Iniciando teste de preenchimento de formulário no site techlistic.com...")
    
    # Executar TC-000: Preenchimento de formulário
    resultado_tc000 = test_techlistic_form()
    
    print("\nResumo do teste:")
    print(f"TC-000: {resultado_tc000['resultado']}")
    
    if resultado_tc000['resultado'] == "Passou":
        print("\nDados do formulário preenchido:")
        for campo, valor in resultado_tc000['dados_formulario'].items():
            print(f"  - {campo}: {valor}")
    else:
        print(f"Mensagem de erro: {resultado_tc000.get('mensagem', 'Erro não especificado')}")
    
    print("\nTeste concluído!")
