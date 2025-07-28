from odoo import models, fields

class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    description = fields.Html(string='Description')
