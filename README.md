# Database IS651

## Prerequisites

1. Install python library

    ```sh
    pipenv install
    ```

1. Setup Database Credential to `.env` 

    ```sh
    DB_HOST=
    DB_NAME=
    DB_PORT=
    DB_USER=
    DB_PASS=
    ```

1. Run first migration to your target database (optional)

    `sql_scripts/create.sql`

1. Getting models from database (optional)

    ```sh
    sqlacodegen postgresql://DB_USER:DB_PASS@DB_HOST:DB_PORT/DB_NAME --outfile models/models.py
    ```

## Development

1. Run first migration

    ```sh
    alembic upgrade head
    ```

1. New migration

    ```sh
    alembic revision --autogenerate -m "message"
    ```

1. Populate Data

    ```sh
    python main.py 
    ```

1. Format

    ```sh
    ruff format .
    ```
