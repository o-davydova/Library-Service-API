# Library Service API
> **Welcome to the online management system for book borrowings** 

###### The system optimizes the work of library administrators and makes the service much more user-friendly.

### Books Service
- **CRUD Functionality:** Implemented Create, Read, Update, and Delete functionality for the Books Service.
- **Permissions:** Only admin users can perform create, update, and delete operations on books. All users, even those not authenticated, can list books.
- **JWT Token Authentication:** Integrated JWT token authentication from the Users Service.

### Users Service
- **CRUD Functionality:** Successfully implemented Create, Read, Update, and Delete functionality for the Users Service.
- **JWT Support:** Added JWT support for secure authentication.

### Borrowings Service
- **Create Borrowing Endpoint:** Implemented the creation of borrowings with validation for book inventory and user attachment.
- **Filtering:** Added filtering options for the Borrowings List endpoint, ensuring non-admin users can see only their borrowings.
- **Return Borrowing Functionality:** Implemented the ability to return borrowings, ensuring it cannot be done twice, and updating the book inventory accordingly.
- **Notifications:** Integrated notifications on each borrowing creation with Telegram API.
- **Telegram Integration:** Set up a Telegram chat and bot for sending notifications.

### ModHeader Integration
**Chrome Extension Compatibility:**
Improved user experience during work with the `ModHeader` Chrome extension by changing the default `Authorization` header for JWT authentication to a custom `Authorize` header.

### API Documentation
- Spectacular Integration.
- **Swagger UI:** Access the Swagger UI for interactive API documentation at `/api/doc/swagger/`.
- **Redoc UI:** Utilize Redoc for clean and readable API documentation at `/api/doc/redoc/`.
- **Schema Endpoint:** The API schema is available at `/api/schema/`.

## Usage

1. Clone the repository.
2. Set up environment variables using `.env.sample` as a guide.
3. Run the application.

Feel free to explore and contribute!

## Installation

Python3 must be already installed.

```shell
git clone https://github.com/o-davydova/Library-Service-API
cd Library-Service-API

python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

set DJANGO_SECRET_KEY=<your django secret key>
set DJANGO_ALLOWED_HOSTS=<your allowed hosts>
set DJANGO_DEBUG=<your debug value>

set TELEGRAM_BOT_TOKEN=<your telegram secret key>
set TELEGRAM_CHAT_ID=<your telegram chat id>

python manage.py migrate
python manage.py runserver
```

## Getting access
- create a user via **/api/user/register**
- get access token via **/api/user/token**