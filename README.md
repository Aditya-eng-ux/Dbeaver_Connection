# DBeaver Connection Project - Django Edition

A Django REST API web application with SQLite database integration. Perfect for learning database management with DBeaver!

## Features

- Django REST Framework API
- SQLite database with Django ORM
- User and Post models with relationships
- Complete CRUD operations
- Built-in API documentation
- CORS support
- DBeaver-ready for database management

## Project Structure

```
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── config/               # Django configuration
│   ├── settings.py       # Django settings
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI configuration
├── api/                  # Main API application
│   ├── models.py        # Database models (User, Post)
│   ├── views.py         # API views and viewsets
│   ├── serializers.py   # DRF serializers
│   └── apps.py          # App configuration
└── README.md            # This file
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

The application will start on `http://localhost:8000`

### 5. Connect with DBeaver

1. Open DBeaver
2. Create a new connection:
   - **Database**: SQLite
   - **Database Path**: Point to `db.sqlite3` in the project directory
   - Or use the simple connection wizard in DBeaver
3. Browse and manage your data directly!

## Database Schema

### Users Table
- `id` (Integer, Primary Key)
- `name` (String)
- `email` (String, Unique)
- `created_at` (DateTime)

### Posts Table
- `id` (Integer, Primary Key)
- `title` (String)
- `content` (Text)
- `user_id` (Foreign Key → Users)
- `created_at` (DateTime)
- `updated_at` (DateTime)

## API Endpoints

### Users
- `GET /api/users/` - Get all users (with pagination)
- `POST /api/users/` - Create new user
- `GET /api/users/<id>/` - Get specific user
- `PUT /api/users/<id>/` - Update user
- `DELETE /api/users/<id>/` - Delete user

### Posts
- `GET /api/posts/` - Get all posts (with pagination)
- `POST /api/posts/` - Create new post
- `GET /api/posts/<id>/` - Get specific post
- `PUT /api/posts/<id>/` - Update post
- `DELETE /api/posts/<id>/` - Delete post

## Example Usage

### Create a User
```bash
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

### Create a Post
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Post", "content": "Hello World!", "user": 1}'
```

### Get All Users
```bash
curl http://localhost:8000/api/users/
```

### Search Users
```bash
curl "http://localhost:8000/api/users/?search=john"
```

### Filter Posts by User
```bash
curl "http://localhost:8000/api/posts/?search=user_name"
```

## Next Steps

1. Run migrations and start the Django server
2. Create sample data via the API endpoints
3. Open DBeaver and connect to the SQLite database
4. Explore the data in the database manager
5. Try modifying data through both the API and DBeaver

## Django Advantages Over Flask

- Built-in admin panel
- More structured project layout
- Powerful ORM
- Better security features out-of-the-box
- Django REST Framework for API development
- Better scalability for larger projects

Enjoy learning with Django and DBeaver! 🚀
