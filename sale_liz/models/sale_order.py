# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    # _description = 'practica/sale_liz.practica/sale_liz'

    state = fields.Selection(selection_add=[('1','BORRADOR'),('2','COTIZACION'),('5','APROBACION'),('6','ORDEN DE VENTA')
                            ,('7','A FACTURAR'),('8','NOTA CREDITO'),('9','NOTA DEBITO'),('10','DOCUMENTO RFC'),('11','UNIONES TEMPORALES'),('12','FACTURADO')],string='state')
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
