from odoo import models, fields

class DoctorModel(models.Model):
    _name = 'hms.doctors'

    firstname = fields.Char()
    lastname = fields.Char()
    image = fields.Image()
