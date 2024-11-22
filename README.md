# Transaction Management System

This is a Django-based web application designed for managing transactions. It allows users to track, manage, and view transactions in an organized manner. The application provides an API for handling transaction-related operations and integrates basic authentication for secure access.

## Features

- Create, view, update, and delete transactions.
- User authentication using Django's built-in authentication system.
- REST API built using Django Rest Framework for transaction management.
- Database-backed storage for transactions.

## Requirements

Before running the project, ensure that you have the following installed:

- Python (3.x)
- Django (3.x or 4.x)
- Django Rest Framework
- SQLite (default database)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/Transaction_M.git
    cd Transaction_M
    ```

2. Create a virtual environment:

    ```bash
    python -m venv .env
    ```

3. Activate the virtual environment:
   - On Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source env/bin/activate
     ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Setup

1. **Database Migration**: Run the following command to apply migrations and set up the database:

    ```bash
    python manage.py migrate
    ```

2. **Create Superuser** (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

3. **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.

## API Endpoints

- `GET /api/transactions/` - List all transactions
- `POST /api/transactions/` - Create a new transaction
- `GET /api/transactions/<id>/` - Retrieve a specific transaction
- `PUT /api/transactions/<id>/` - Update a specific transaction
- `DELETE /api/transactions/<id>/` - Delete a specific transaction

## Testing

You can run the tests using:

```bash
python manage.py test

