from odoo import models, fields

class Project(models.Model):
    _name = 'project.project'
    _description = 'Project model'
    
    name = fields.Char()
    description = fields.Text()
    initial_date = fields.Date()
    final_date = fields.Date()
    worker_ids = fields.One2many('project.employee', 'project_id', string='Workers')
    color = fields.Integer()
    state = fields.Selection([
        ('first_impressions', 'First impressions'),
        ('to_do', 'To do'),
        ('doing', 'Doing'),
        ('testing', 'Testing'),
        ('displayed', 'Displayed'),
        ('done', 'Done'),
        ('closed', 'Closed'),
        ('canceled', 'Canceled')
    ], default="first_impressions")
    
    task_ids = fields.One2many('project.task', 'project_id', string='tasks')
    document_ids = fields.One2many('project.document', 'project_id', string='Documents')
    report_ids = fields.One2many('project.report', 'project_id', string='Reports')
    
    def action_change_state(self):
        for project in self:
            if project.state == 'first_impressions':
                project.state = 'to_do'
            elif project.state ==  'to_do':
                project.state = 'doing'
            elif project.state ==  'doing':
                project.state = 'testing'
            elif project.state ==  'testing':
                project.state = 'displayed'
            elif project.state ==  'displayed':
                project.state = 'done'
            elif project.state == 'done':
                project.state = 'closed'

    def action_cancel(self):
        for project in self:
            project.state = "canceled"