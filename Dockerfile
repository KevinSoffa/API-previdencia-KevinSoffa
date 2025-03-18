# Usando a imagem oficial do Python como base
FROM python:3.11-slim

# Diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo requirements.txt (ou o arquivo que contém as dependências)
COPY requirements.txt /app/

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para dentro do contêiner
COPY . /script/

# Expor a porta 8000, que é a porta padrão do FastAPI
EXPOSE 8000

# Comando para rodar a aplicação FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
