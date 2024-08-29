# __manifest__.py
{
    'name': 'Todo List by Leo',
    'version': '1.0',
    'summary': 'Task list creator with colors and strike-through functionality',
    'description': 'This module allows users to create task lists, assign colors, and mark tasks as completed.',
    'author': 'Leo Santo Dev',
    'depends': ['base'],
    'data': [
        'views/todo_task_views.xml',
    ],
    'installable': True,
    'application': True,
}