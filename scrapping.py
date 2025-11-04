import csv
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


with open("classificacaoTimes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Time","Classificação", "Serie", "Ano",  "Pontos","Jogos", "Vitórias", "Empates", "Derrotas",
                     "Gols_Pro", "Gols_Contra", "Saldo_Gols", "Cartoes_Amarelos", "Cartoes_Vermelhos",
                     "Aproveitamento (%)"])

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        years = ["2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
        series = ["serie-a", "serie-b"]
        
        for year in years:
            for serie in series:
                
                page.goto(f"https://www.cbf.com.br/futebol-brasileiro/tabelas/campeonato-brasileiro/{serie}/{year}")

                page.wait_for_selector("div.styles_tableContent__dh0gO table")
                
                linhas = page.locator("div.styles_tableContent__dh0gO table tbody tr")
                n = linhas.count()
                
                for i in range(n):
                    #seleciona todas as celulas
                    linha  = linhas.nth(i)
                    tds = linha.locator("td")
                    print(linha)
                    # Time selecionado
                    time = tds.nth(0).locator("a strong").inner_text().strip()
                    print(time)
                    #Classificação do time
                    classificacao = str(i+1)
                    #Pontos
                    pontos = tds.nth(1).inner_text().strip()
                    #Jogos
                    jogos = tds.nth(2).inner_text().strip()
                    #vitórias
                    vitorias = tds.nth(3).inner_text().strip()
                    #empates
                    empates = tds.nth(4).inner_text().strip()
                    #derrotas
                    derrotas = tds.nth(5).inner_text().strip()
                    #golspro
                    gols_pro = tds.nth(6).inner_text().strip()
                    #golscontra
                    gols_contra = tds.nth(7).inner_text().strip()
                    #salgoGols
                    saldo_gols = tds.nth(8).inner_text().strip()
                    #cartoes_amarelos
                    cartoes_amarelos = tds.nth(9).inner_text().strip()
                    #cartoes_vermelhos
                    cartoes_vermelhos = tds.nth(10).inner_text().strip()
                    #aproveitamento
                    aproveitamento = tds.nth(11).inner_text().strip()
                    
                    writer.writerow([
                        time, classificacao, serie, year, pontos, jogos, vitorias, empates,
                        derrotas, gols_pro, gols_contra, saldo_gols,
                        cartoes_amarelos, cartoes_vermelhos, aproveitamento
                    ])
                    
                
            
        browser.close()