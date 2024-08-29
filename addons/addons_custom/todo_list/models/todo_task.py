# models/todo_task.py
from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'

    name = fields.Char(string='Task Title', required=True)
    description = fields.Text(string='Description')
    color = fields.Integer(string='Color Index')
    is_done = fields.Boolean(string='Done', default=False)

    def toggle_done(self):
        self.is_done = not self.is_done