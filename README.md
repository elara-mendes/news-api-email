# 📰 news-api-email  

[Eng Ver.](README_en.md)

Um script em **Python** que busca as últimas notícias da **NewsAPI** e as envia diretamente para o seu e-mail via **SMTP**.  

---

## 📌 Como o programa funciona?  

1. **Obtém notícias** de uma API.  
2. **Tradução automática**: Converte a descrição da notícia para inglês.  
3. **Análise de sentimentos**: Avalia se a notícia tem um tom **positivo, neutro ou negativo**.  
4. **Filtragem**: Mantém apenas as notícias **positivas**.  
5. **Entrega por e-mail**: Envia as melhores notícias diretamente para você.  

---

## ✉️ Como obter uma App Password do Gmail?  

Você precisa de **autenticação em dois fatores (2FA)** no Gmail, não pode usar sua senha normal para autenticar via SMTP. Em vez disso, precisa gerar uma **Senha de App**.  

**Passos para ativar a Verificação em Duas Etapas e gerar uma Senha de App:**

1. **Ativar a Verificação em Duas Etapas (2FA):**
   - Acesse sua [Conta do Google](https://myaccount.google.com/security).
   - Na seção **"Como você faz login no Google"**, selecione **"Verificação em duas etapas"** e siga as instruções para ativá-la.

2. **Gerar uma Senha de App:**
   - Após ativar a 2FA, retorne à seção **"Segurança"** da sua conta.
   - Selecione **"Senhas de app"**.
   - Escolha **"Selecionar app"**, depois **"Outro (nome personalizado)"**, e insira um nome (por exemplo, `news-bot`).
   - Clique em **"Gerar"** e anote a senha fornecida.

**Importante:** Armazene essa senha com segurança e não a compartilhe publicamente.

**Copie a senha** e use no seu código.  

Em **`send_email.py`**

```python
YOUR_EMAIL = "elaradomingos@gmail.com" # Seu email
APP_PASSWORD = os.getenv("GMAIL_PASSWORD") # Sua senha de app
```

---

## ⚙️ Configuração do script  

No arquivo **`main.py`**, você pode personalizar o **tópico**, o **idioma** e a **data** da pesquisa das notícias.  

Para obter uma **chave de API da NewsAPI**, basta criar uma conta aqui: [NEWS API](https://newsapi.org/). Consulte a documentação oficial caso queira personalizar a busca conforme suas necessidades.  

### 🔧 Exemplo de configuração no código:  

```python
import os

NEWS_API = os.getenv("NEWS_API")  # Sua chave da API
TOPIC = "trans, diversity"  # Tópicos de busca
LANGUAGE = "en"  # Idioma das notícias
DATE = "2025-03-06"  # Data inicial da busca (YYYY-MM-DD)
```

---