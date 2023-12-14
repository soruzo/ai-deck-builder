# Usar uma imagem base do Python
FROM python:3.8

# Definir o diretório de trabalho no container
WORKDIR /usr/src/app

# Copiar o arquivo de dependências e instalar as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos os arquivos do projeto para o diretório de trabalho no container
COPY . .

# Comando para rodar o aplicativo
CMD [ "python", "./main.py" ]
