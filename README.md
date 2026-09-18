# Homecare Platform Backend

FastAPI backend for a home-care service marketplace.

## Architecture

Router -> Schema -> Service -> Repository -> PostgreSQL

## Features

- JWT authentication
- Customer, service provider and admin roles
- Provider profiles, services and locations
- Service categories
- Multiple services per customer request
- Nearest-provider matching
- Provider assignments and status workflow
- Quotes
- Payment records and payment status
- Notifications
- Reviews and provider ratings
- Issue reporting and admin resolution
- PostgreSQL and Alembic

## Run

```bash
source .venv/bin/activate
uvicorn app.main:app --reload
```

API documentation:

`http://127.0.0.1:8000/docs`

## Database migrations

```bash
alembic upgrade head
```

For future schema changes:

```bash
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

Never commit `.env` or database credentials.
