# 1. Imagem base oficial do Python
FROM python:3.10-slim

# 2. Define diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia os arquivos de dependência
COPY requirements.txt .

# 4. Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# --- ADICIONE ESTAS DUAS LINHAS ---
# Instala o cliente PostgreSQL para ter acesso ao pg_isready
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*
# ---------------------------------


# 5. Copia todo o projeto para dentro do container
COPY . .

# 6. Cria variáveis de ambiente padrão
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 7. Comando que será executado ao subir o container
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]

EXPOSE 8000
