FROM postgres:latest

# Definir um argumento de construção para o caminho do arquivo SQL
ARG DUMP_PATH

# Copiar o script SQL para o diretório de inicialização do Docker
COPY ${DUMP_PATH}/init.sql /docker-entrypoint-initdb.d/
