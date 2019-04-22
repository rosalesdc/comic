# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class Wizard_Descrip(models.TransientModel): 
	_inherit = 'product.template'
	

	def _default_category(self):
		print('RASTREANDO',str(self.env['product.product'].browse(self._context.get('categ_id'))))
		return self.env['product.category'].browse(self._context.get('product.category'))


	product_ids=fields.Many2many('product.product',string='Categorias', default=_default_category)

	def update_descrip(self):
		for record in self.product_ids:
			print('PROBANDO',str(record.categ_id))
			print('SEGUNDA PRUEBA',str(record.categ_id.id))
			if record.categ_id.id == 1:
				print('TERCERA PRUEBA',str(record.categ_id.id))
				record.write({'categ_id':34})
				

	# def write(self,vals):
	# 	res=super().write(vals)
	# 	return res	

	# @api.multi
 #    def write(self, values):
 #    	self.description_sale=self.description_sale+"/"+self.x_editorial+"/"+self.x_autor
 #    	return super(Wizard_Descrip,self).write(values)


    @api.multi
    def write(self, vals):
    	description=""      
        description=self.description_sale+"/"+self.x_editorial+"/"+self.x_autor
        self.description_sale=description
        res=super(Wizard_Descrip, self).write(vals)
        return res



