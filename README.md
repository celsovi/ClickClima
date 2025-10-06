# ClickClima API

API REST construída com Django + PostgreSQL para monitoramento ambiental via sensores.

## Como rodar com Docker

```bash
git clone https://github.com/celsovi/ClickClima.git
cd clickclima-api
cp .env.example .env
docker-compose up --build
