# ClickClima API

API REST construída com Django + PostgreSQL para monitoramento ambiental via sensores.

## Como rodar com Docker

```bash
git clone https://github.com/celsovi/ClickClima.git
cd clickclima-api
cp .env.example .env
docker-compose up --build
```

## Deploy

Faça o build e o push da imagem para o registry na Campari (não esqueça de ligar a VPN antes):

```bash
docker build -t registry.simple4decision.com/clickclima-api:latest .
docker push registry.simple4decision.com/clickclima-api:latest
```

Acesse o servidor via SSH e rode os comandos:

```bash
ssh <username>@10.4.0.21
cd /home/pedro.arantes/apps/clickclima-api
docker compose up -d
```
