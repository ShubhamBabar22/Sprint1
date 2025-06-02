# Task Manager Application

A simple yet elegant task management application built with Python Flask, SQLite, HTML, and CSS.

## Features

- Create, read, update, and delete tasks
- Organize tasks by priority (low, medium, high)
- Track task status (pending, in progress, completed)
- Set due dates for tasks
- Responsive design for mobile and desktop

## Screenshots

![Task Manager Home Page](screenshots/home.png)
![Add Task Form](screenshots/add-task.png)
![Edit Task Form](screenshots/edit-task.png)

## Installation

1. Clone this repository
2. Navigate to the project directory
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:

```bash
python app.py
```

2. Open your web browser and go to `http://127.0.0.1:5000/`
3. Start managing your tasks!

## Technologies Used

- **Backend**: Python, Flask, SQLite3
- **Frontend**: HTML, CSS, Font Awesome
- **Database**: SQLite

## Project Structure

```
task_manager/
├── app.py                  # Main Flask application
├── task_manager.db         # SQLite database (created automatically)
├── requirements.txt        # Python dependencies
├── static/
│   └── css/
│       └── style.css       # CSS styles
└── templates/
    ├── base.html           # Base template
    ├── index.html          # Home page with task list
    ├── add.html            # Add task form
    └── edit.html           # Edit task form
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 