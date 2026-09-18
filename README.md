
# Homecare Platform Backend

This is the backend for my Homecare Platform project. The platform is designed to connect customers with homecare service providers.

I am building this project to practice backend development, database management, authentication, and API testing using FastAPI and PostgreSQL.

## Technologies

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- JWT Authentication
- Pytest
- Postman

## Main Features

- User registration and login
- User profile management
- Provider profiles
- Service categories
- Service requests
- Provider matching
- Assignments
- Quotes
- Payments
- Notifications
- Reviews
- Issue reporting
- Admin management

## Project Structure

```text
app/
├── core/
├── database/
├── models/
├── repositories/
├── routers/
├── schemas/
└── services/

tests/
├── routers/
├── services/
└── repositories/
```

The project separates routing, business logic, database operations, models, and schemas to keep the backend organized and easier to maintain.

## Running the Project

Clone the repository:

```bash
git clone git@github.com:angeliqueeumwali/homecare-platform-backend.git
cd homecare-platform-backend
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your environment variables in a `.env` file.

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Testing

Run the tests with:

```bash
pytest
```

The current test suite includes health router, health service, and database connection tests.

## Project Status

The backend is under development. I am continuing to build and test the platform's features.

## Author

Umwali Angelique