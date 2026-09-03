# Mini Mechanic Service API

A RESTful API built with Django and Django REST Framework for managing mechanics and vehicle service requests.

## Features

- Mechanic CRUD operations
- Service Request CRUD operations
- Mechanic → Service Request relationship
- JWT authentication
- Protected API endpoints
- Input validation and error handling
- Search mechanics by name or location
- Filtering by availability and rating
- Pagination
- Swagger/OpenAPI documentation
- Automated API tests
- SQLite database

## Tech Stack

- Python 3.14+
- Django 6.1
- Django REST Framework
- SQLite
- Simple JWT
- django-filter
- drf-spectacular
- python-dotenv

## Project Structure

```text
mechanic-service-api/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── mechanics/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── service_requests/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

## Database Models

### Mechanic

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Primary key |
| `name` | String | Mechanic name |
| `phone` | String | 10-digit phone number |
| `location` | String | Mechanic location |
| `rating` | Decimal | Rating between 0 and 5 |
| `is_open` | Boolean | Whether the mechanic is currently open |
| `services` | JSON | List of services offered |

### Service Request

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Primary key |
| `customer_name` | String | Customer name |
| `customer_phone` | String | 10-digit phone number |
| `vehicle_number` | String | Vehicle registration number |
| `mechanic` | Foreign Key | Associated mechanic |
| `service` | String | Requested service |
| `problem_description` | Text | Description of the vehicle problem |
| `status` | String | Current request status |
| `created_at` | DateTime | Request creation time |

Each Service Request belongs to one Mechanic through a ForeignKey relationship.

A new Service Request automatically receives the status:

```text
PENDING
```

## Authentication

The API uses JWT authentication to protect the API endpoints.

### Obtain Access Token

```http
POST /api/token/
```

Request:

```json
{
    "username": "admin",
    "password": "your-password"
}
```

Response:

```json
{
    "refresh": "your-refresh-token",
    "access": "your-access-token"
}
```

Use the access token in the request header:

```http
Authorization: Bearer <access-token>
```

### Refresh Access Token

```http
POST /api/token/refresh/
```

Request:

```json
{
    "refresh": "your-refresh-token"
}
```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/token/` | Obtain JWT access and refresh tokens |
| POST | `/api/token/refresh/` | Refresh access token |

### Mechanics

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/mechanics/` | Get all mechanics |
| POST | `/api/mechanics/` | Create a mechanic |
| GET | `/api/mechanics/{id}/` | Get a mechanic by ID |
| PUT | `/api/mechanics/{id}/` | Update a mechanic |
| PATCH | `/api/mechanics/{id}/` | Partially update a mechanic |
| DELETE | `/api/mechanics/{id}/` | Delete a mechanic |

### Service Requests

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/service-requests/` | Get all service requests |
| POST | `/api/service-requests/` | Create a service request |
| GET | `/api/service-requests/{id}/` | Get a service request by ID |
| PUT | `/api/service-requests/{id}/` | Update a service request |
| PATCH | `/api/service-requests/{id}/` | Partially update a service request |
| DELETE | `/api/service-requests/{id}/` | Delete a service request |

## Search, Filtering and Pagination

### Search by Mechanic Name

```http
GET /api/mechanics/?search=Raj
```

### Search by Location

```http
GET /api/mechanics/?search=Vadodara
```

### Filter by Availability

```http
GET /api/mechanics/?is_open=true
```

### Filter by Rating

```http
GET /api/mechanics/?rating=4.50
```

### Pagination

```http
GET /api/mechanics/?page=2
```

The API returns paginated results containing the total count and next/previous page links.

Search, filtering and pagination can also be combined.

## Validation and Error Handling

The API validates incoming data and returns appropriate HTTP status codes with meaningful error messages.

### Mechanic Validation

- Phone number must contain exactly 10 digits.
- Rating must be between 0 and 5.
- Required fields must be provided.

Example:

```json
{
    "phone": "12345"
}
```

Response:

```json
{
    "phone": [
        "Phone number must contain exactly 10 digits."
    ]
}
```

### Service Request Validation

- Customer phone number must contain exactly 10 digits.
- Vehicle number must follow the expected registration format.
- The selected mechanic must exist.
- The requested service must be offered by the selected mechanic.
- Required fields must be provided.

Example valid vehicle number:

```text
GJ06AB1234
```

If a mechanic does not offer the requested service:

```json
{
    "non_field_errors": [
        "This mechanic does not offer this service."
    ]
}
```

Invalid input returns a `400 Bad Request`.

## API Documentation

Interactive Swagger documentation is available at:

```text
http://127.0.0.1:8000/api/docs/
```

OpenAPI schema:

```text
http://127.0.0.1:8000/api/schema/
```

Swagger can be used to authenticate with a JWT access token and test the API directly from the browser.

## Setup and Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd mechanic-service-api
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Git Bash:

```bash
python -m venv venv
source venv/Scripts/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root using `.env.example` as a template.

Example:

```env
SECRET_KEY=your-secret-key
```

The `.env` file contains environment-specific secrets and should not be committed to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

Swagger documentation:

```text
http://127.0.0.1:8000/api/docs/
```

## Sample Requests

### Create a Mechanic

```http
POST /api/mechanics/
```

Request:

```json
{
    "name": "Raj Auto Care",
    "phone": "9876543210",
    "location": "Vadodara",
    "rating": 4.5,
    "is_open": true,
    "services": [
        "Oil Change",
        "Brake Repair"
    ]
}
```

Example response:

```json
{
    "id": 1,
    "name": "Raj Auto Care",
    "phone": "9876543210",
    "location": "Vadodara",
    "rating": "4.50",
    "is_open": true,
    "services": [
        "Oil Change",
        "Brake Repair"
    ]
}
```

### Create a Service Request

```http
POST /api/service-requests/
```

Request:

```json
{
    "customer_name": "Chetan",
    "customer_phone": "0987654321",
    "vehicle_number": "GJ06AB1234",
    "mechanic": 1,
    "service": "Oil Change",
    "problem_description": "Engine oil needs replacement"
}
```

Example response:

```json
{
    "id": 1,
    "customer_name": "Chetan",
    "customer_phone": "0987654321",
    "vehicle_number": "GJ06AB1234",
    "mechanic": 1,
    "service": "Oil Change",
    "problem_description": "Engine oil needs replacement",
    "status": "PENDING",
    "created_at": "2026-09-03T10:30:00Z"
}
```

## Running Tests

Run the Django test suite with:

```bash
python manage.py test
```

Run the Django system check with:

```bash
python manage.py check
```

The test suite covers:

- Authentication requirements
- Mechanic creation
- Invalid mechanic phone numbers
- Invalid mechanic ratings
- Missing required fields
- Service Request creation
- Invalid vehicle numbers
- Services not offered by a mechanic
- Non-existent mechanics

## HTTP Status Codes

| Status Code | Meaning |
|---|---|
| `200 OK` | Request successful |
| `201 Created` | Resource created successfully |
| `204 No Content` | Resource deleted successfully |
| `400 Bad Request` | Invalid input/data |
| `401 Unauthorized` | Authentication required or invalid |
| `404 Not Found` | Resource does not exist |

## Future Improvements

Possible future enhancements include:

- PostgreSQL database
- Docker containerization
- Application logging
- More advanced permissions and roles
- More comprehensive test coverage
- Mechanic availability scheduling
- Service Request status management
- API rate limiting

## License

This project was created as part of a backend development internship assignment.