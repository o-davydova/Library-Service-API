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

## Test Coverage Report

```plaintext
Name                                                                    Stmts   Miss  Cover
-------------------------------------------------------------------------------------------
books\__init__.py                                                           0      0   100%
books\admin.py                                                              3      2    33%
books\apps.py                                                               4      0   100%
books\migrations\0001_initial.py                                            5      0   100%
books\migrations\__init__.py                                                0      0   100%
books\models.py                                                            12      1    92%
books\permissions.py                                                        4      0   100%
books\serializers.py                                                        6      0   100%
books\tests\__init__.py                                                     0      0   100%
books\tests\test_book_api.py                                               72      0   100%
books\urls.py                                                               6      0   100%
books\views.py                                                              8      0   100%
borrowings\__init__.py                                                      0      0   100%
borrowings\admin.py                                                         7      6    14%
borrowings\apps.py                                                          4      0   100%
borrowings\migrations\0001_initial.py                                       7      0   100%
borrowings\migrations\0002_borrowing_borrow_date_not_past_and_more.py       7      0   100%
borrowings\migrations\0003_remove_borrowing_borrow_date_not_past.py         4      0   100%
borrowings\migrations\__init__.py                                           0      0   100%
borrowings\models.py                                                       27      2    93%
borrowings\serializers.py                                                  44      0   100%
borrowings\tests\__init__.py                                                0      0   100%
borrowings\tests\test_borrowing_api.py                                    137      0   100%
borrowings\urls.py                                                          6      0   100%
borrowings\views.py                                                        49      0   100%
library_service_api\__init__.py                                             0      0   100%
library_service_api\settings.py                                            26      0   100%
library_service_api\urls.py                                                 4      0   100%
manage.py                                                                  12      2    83%
telegram_api\__init__.py                                                    0      0   100%
telegram_api\telegram_helper.py                                            12      2    83%
users\__init__.py                                                           0      0   100%
users\admin.py                                                             12     11     8%
users\apps.py                                                               4      0   100%
users\migrations\0001_initial.py                                            7      0   100%
users\migrations\__init__.py                                                0      0   100%
users\models.py                                                            36      8    78%
users\serializers.py                                                       17      7    59%
users\tests\__init__.py                                                     0      0   100%
users\tests\test_user_api.py                                                0      0   100%
users\urls.py                                                               5      0   100%
users\views.py                                                             13      1    92%
-------------------------------------------------------------------------------------------
TOTAL                                                                     560     42    92%
```

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