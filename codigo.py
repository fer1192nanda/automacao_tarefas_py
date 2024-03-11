# passo a passo do projeto
#passo 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5    


# pyautogui.click - Clicar em algum lugar da tela
# pyautogui.write - Escrever um texto
# pyautogui.press - Pressiona uma tecla do teclado 

# Abrir navegador do chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("Enter")

# Entrar no site 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa maior (3 segundos)
time.sleep(3)

# passo 2: Fazer login 
pyautogui.click(x=2077, y=403)
pyautogui.write("qualqueremail@gmail.com")

# Escrever a senha
pyautogui.press("tab")
pyautogui.write("sua senha")

# Clicar no botão de logar
pyautogui.click(x=2328, y=571)
time.sleep(3)

# passo 3: Importar base dados p fazer cadastro
# ferramenta pandas - base de dados
import pandas 
tabela = pandas.read_csv("produtos.csv")

print(tabela)   

# passo 4: cadastrar um produto
for linha in tabela.index:

    # clicar no primeiro campo 
    pyautogui.click(x=2126, y=293)

    # codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write("codigo")  
    pyautogui.press("tab")

    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo    
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")  

    # categoria do produto
    # str() transforma numero em string
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # OBS
    # isna = significa vazio NaN = NOT A NUMBER  
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write("obs")
    pyautogui.press("tab")

    # Enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# passo 5: Repetir processo de cadastro até acabar