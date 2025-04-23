"""
Caso de Teste: TC-004 - Simulação de compra no site demoblaze.com
Objetivo: Simular uma compra de um produto qualquer
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

def test_purchase_simulation():
    """TC-004: Simulação de compra no site demoblaze.com"""
    driver = setup_driver()
    
    try:
        # Registrar data/hora de início
        start_time = datetime.now()
        print(f"TC-004: Início do teste em {start_time.strftime('%d/%m/%Y %H:%M:%S')}")
        
        # Acessar o site
        driver.get("https://www.demoblaze.com/")
        
        # Aguardar carregamento da página inicial com tempo maior
        wait = WebDriverWait(driver, 20)  # Aumentado para 20 segundos
        wait.until(EC.visibility_of_element_located((By.ID, "tbodyid")))
        
        # Aguardar um pouco mais para garantir que os produtos sejam carregados
        time.sleep(3)
        
        # 1. Escolher um produto clicando em um elemento da lista
        print("TC-004: Selecionando um produto...")
        
        # Tentar diferentes estratégias de localização
        produtos = None
        estrategias = [
            (By.CSS_SELECTOR, ".card-title a"),
            (By.CSS_SELECTOR, ".card-block h4 a"),
            (By.CSS_SELECTOR, ".card h4 a"),
            (By.XPATH, "//div[@class='card-block']//a"),
            (By.XPATH, "//a[contains(@class, 'hrefch')]")
        ]
        
        for by, selector in estrategias:
            produtos = driver.find_elements(by, selector)
            if len(produtos) > 0:
                print(f"TC-004: Produtos encontrados usando seletor: {selector}")
                break
        
        if not produtos or len(produtos) == 0:
            # Se ainda não encontrou produtos, tente navegar para um produto diretamente
            print("TC-004: Tentando acessar um produto diretamente...")
            driver.get("https://www.demoblaze.com/prod.html?idp_=1")
            nome_produto = "Samsung galaxy s6"  # Nome padrão para o primeiro produto
        else:
            # Selecionar o primeiro produto da lista
            nome_produto = produtos[0].text
            print(f"TC-004: Produto selecionado: {nome_produto}")
            produtos[0].click()
        
        # Aguardar carregamento da página do produto
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-content")))
        time.sleep(2)  # Aguardar um pouco mais para garantir carregamento completo
        
        # 2. Clicar em Add to cart e aceitar alerta
        print("TC-004: Adicionando produto ao carrinho...")
        add_to_cart_button = driver.find_element(By.CSS_SELECTOR, ".btn-success")
        add_to_cart_button.click()
        
        # Aguardar e aceitar o alerta
        time.sleep(3)  # Aumentado para 3 segundos para garantir que o alerta apareça
        try:
            # Mudar para o alerta e aceitá-lo
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"TC-004: Alerta exibido: {alert_text}")
            alert.accept()
        except:
            print("TC-004: Nenhum alerta encontrado ou já foi fechado")
        
        # 3. Ir para o carrinho
        print("TC-004: Navegando para o carrinho...")
        time.sleep(2)  # Aumentado para garantir que o alerta foi processado
        cart_link = driver.find_element(By.ID, "cartur")
        cart_link.click()
        
        # Aguardar carregamento da página do carrinho
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".table-responsive")))
        time.sleep(2)  # Aguardar um pouco mais para garantir carregamento completo
        
        # 4. Clicar em Place Order
        print("TC-004: Iniciando processo de compra...")
        place_order_button = driver.find_element(By.CSS_SELECTOR, ".btn-success")
        place_order_button.click()
        
        # Aguardar carregamento do modal de compra
        wait.until(EC.visibility_of_element_located((By.ID, "orderModalLabel")))
        time.sleep(1)  # Pequena pausa para garantir que o modal está completamente carregado
        
        # 5. Preencher o formulário de cadastro
        print("TC-004: Preenchendo formulário de compra...")
        driver.find_element(By.ID, "name").send_keys("João Silva")
        driver.find_element(By.ID, "country").send_keys("Brasil")
        driver.find_element(By.ID, "city").send_keys("São Paulo")
        driver.find_element(By.ID, "card").send_keys("4111111111111111")
        driver.find_element(By.ID, "month").send_keys("12")
        driver.find_element(By.ID, "year").send_keys("2025")
        
        # 6. Confirmar a compra
        print("TC-004: Confirmando a compra...")
        purchase_button = driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary")
        purchase_button.click()
        
        # Aguardar o modal de confirmação
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sweet-alert")))
        time.sleep(1)  # Pequena pausa para garantir que o modal está completamente carregado
        
        # 7. Validar a mensagem de confirmação
        confirmation_message = driver.find_element(By.CSS_SELECTOR, ".sweet-alert h2").text
        confirmation_details = driver.find_element(By.CSS_SELECTOR, ".sweet-alert p.lead").text
        
        # Extrair ID do pedido e valor
        order_id = None
        amount = None
        
        if "Id:" in confirmation_details:
            order_details = confirmation_details.split("\n")
            for detail in order_details:
                if "Id:" in detail:
                    order_id = detail.split("Id:")[1].strip()
                if "Amount:" in detail:
                    amount = detail.split("Amount:")[1].strip()
        
        # Registrar resultado
        if "Thank you" in confirmation_message and order_id is not None:
            print(f"TC-004: Compra realizada com sucesso! ID do pedido: {order_id}, Valor: {amount}")
            result = "Passou"
        else:
            print("TC-004: Falha na confirmação da compra.")
            result = "Falhou"
        
        # Registrar data/hora de fim
        end_time = datetime.now()
        print(f"TC-004: Fim do teste em {end_time.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"TC-004: Duração do teste: {(end_time - start_time).total_seconds()} segundos")
        
        return {
            "caso_teste": "TC-004",
            "objetivo": "Simulação de compra de produto",
            "inicio": start_time.strftime('%d/%m/%Y %H:%M:%S'),
            "fim": end_time.strftime('%d/%m/%Y %H:%M:%S'),
            "duracao": f"{(end_time - start_time).total_seconds()} segundos",
            "produto": nome_produto,
            "resultado": result,
            "mensagem_confirmacao": confirmation_message,
            "id_pedido": order_id,
            "valor": amount
        }
        
    except Exception as e:
        print(f"TC-004: Erro durante o teste: {str(e)}")
        end_time = datetime.now()
        return {
            "caso_teste": "TC-004",
            "objetivo": "Simulação de compra de produto",
            "inicio": start_time.strftime('%d/%m/%Y %H:%M:%S'),
            "fim": end_time.strftime('%d/%m/%Y %H:%M:%S'),
            "duracao": f"{(end_time - start_time).total_seconds()} segundos",
            "resultado": "Falhou",
            "mensagem": f"Erro: {str(e)}"
        }
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Iniciando teste de simulação de compra no site demoblaze.com...")
    
    # Executar TC-004: Simulação de compra
    resultado_tc004 = test_purchase_simulation()
    
    print("\nResumo do teste:")
    print(f"TC-004: {resultado_tc004['resultado']}")
    
    if resultado_tc004['resultado'] == "Passou":
        print(f"Produto: {resultado_tc004['produto']}")
        print(f"Mensagem de confirmação: {resultado_tc004['mensagem_confirmacao']}")
        print(f"ID do pedido: {resultado_tc004['id_pedido']}")
        print(f"Valor: {resultado_tc004['valor']}")
    else:
        print(f"Mensagem de erro: {resultado_tc004.get('mensagem', 'Erro não especificado')}")
    
    print("\nTeste concluído!")
