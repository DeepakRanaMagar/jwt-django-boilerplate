## Django JWT Authentication with Custom User Model

This repository provides an implementation of Django JWT authentication with a custom user model that includes email for authentication instead of username. It also includes fields for name, address, and phone number.

### Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/DeepakRanaMagar/jwt-django-tutorial.git
    ```

2. Navigate to the project directory:

    ```shell
    cd your-repo
    ```

3. Create a virtual environment:

    ```shell
    python -m venv venv
    ```

4. Activate the virtual environment:

    - For Windows:

      ```shell
      venv\Scripts\activate
      ```

    - For macOS and Linux:

      ```shell
      source venv/bin/activate
      ```

5. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

6. Apply the database migrations:

    ```shell
    python manage.py migrate
    ```

7. Start the development server:

    ```shell
    python manage.py runserver
    ```

### Usage

To use the Django JWT authentication with the custom user model, follow these steps:

1. Register a new user by making a `POST` request to `/api/register` with the following parameters:

    - `email`: The user's email address.
    - `password`: The user's password.
    - `name`: The user's name.
    - `address`: The user's address.
    - `phone_num`: The user's phone number.

2. Log in by making a `POST` request to `/api/login` with the following parameters:

    - `email`: The user's email address.
    - `password`: The user's password.

    This will return a JSON response containing the JWT token.

3. Use the JWT token for subsequent authenticated requests by including it in the `Authorization` header:

    ```shell
    Authorization: Bearer <JWT_TOKEN>
    ```

    Replace `<JWT_TOKEN>` with the actual JWT token obtained from the login response.

### API Endpoints

- `POST /api/register`: Register a new user.
- `POST /api/login`: Log in and obtain a JWT token.

### Custom User Model

The custom user model used in this implementation includes the following fields:

- `email`: The user's email address (used for authentication).
- `password`: The user's password.
- `name`: The user's name.
- `address`: The user's address.
- `phone_num`: The user's phone number.

### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
