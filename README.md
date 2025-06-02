# Task Manager Application

A robust task management application built with Django, MySQL, HTML, CSS, and JavaScript.

## Features

- User authentication and authorization
- Create, read, update, and delete tasks
- Organize tasks by priority (low, medium, high)
- Track task status (pending, in progress, completed)
- Set due dates for tasks
- Responsive design for mobile and desktop
- User dashboard with task overview
- Task filtering and search capabilities

## Screenshots

![Task Manager Home Page](ScreeenShots/home.png)
![Dashboard View](ScreeenShots/dashboard.png)
![Task Management](ScreeenShots/tasks.png)

## Installation

1. Clone this repository
2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up MySQL:
   - Install MySQL if not already installed
   - Create a database named 'taskmanager_db'
   - Update database credentials in `taskmanager/settings.py` if needed

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

## Usage

1. Run the development server:
```bash
python manage.py runserver
```

2. Open your web browser and go to `http://127.0.0.1:8000/`
3. Log in with your credentials
4. Start managing your tasks!

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Authentication**: Django's built-in auth system
- **Static Files**: Django's static file handling

## Project Structure

```
taskmanager/
├── manage.py              # Django's command-line utility
├── taskmanager/          # Project configuration
│   ├── settings.py       # Project settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── tasks/               # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # App URL configuration
│   └── templates/       # HTML templates
├── static/              # Static files (CSS, JS, images)
├── venv/                # Virtual environment
└── requirements.txt     # Project dependencies
```

## Development

- The project uses Django's built-in development server for local development
- Static files are served from the `static/` directory
- Templates are located in `tasks/templates/`
- Database migrations are managed through Django's migration system

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
