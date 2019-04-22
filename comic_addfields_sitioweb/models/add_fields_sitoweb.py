# # -*- coding: utf-8 -*-

# from odoo import api
# from odoo import fields
# from odoo import models
# import random

# #class add_fields_sitoweb(models.Model):
# 	"""docstring for ClassName"""
# 	#_inherit='product.template'

# 	#@api.multi

#     #def _compute_depends(self):
#         #for editorial in self.x_editorial:
#         #    editoriales += editorial.name
#     #    self.x_edit="hola"#editoriales


# 	#x_edit= fields.Char(compute='_compute_depends')


# 	#x_edit = fields.Char(compute='_compute_depends')

# class fields_invisible_sitio(models.Model):
# 	_inherit='product.template'

# #	def _compute_fields(self):
# #		for editorial in self.x_editorial:
# #			editoriales+=editorial.name
# #		self.x_edit="hola"
# 	@api.one
#     @api.depends('x_editorial')
#     def _compute_name(self):
#     	print("hola")
#     	x_edit=x_editorial
# #        for record in self:
# #            record.x_edit = str(random.randint(1, 1e6))

#     x_edit = fields.Char(string="Estatus ordenado",
#     						readonly=True, 
#     						compute='_compute_name',) #campo 
# #	x_edit=fields.Char(compute='_compute_fields')

# # -*- coding: utf-8 -*-

# from odoo import api
# from odoo import fields
# from odoo import models
# import smtplib

# class AddProductFields(models.Model):
#     _inherit = 'product.template'
   
#     @api.one
#     @api.model
#     def _obtener_edit(self):        
#         #orden = self.env['sale.order'].search([('id', '=', self.sale_order.id)])
#         #self.xreferencia=orden.name 
#         #self.xreferencia=orden.id_numero_referencia.name
#         editoriales=""
#         for editorial in self.x_editorial:
#           editoriales += editorial.name
#         self.x_edit=editoriales
#         self.x_x=editoriales
   
#     @api.one
#     @api.model
#     def _obtener_author(self):        
#        autores=""
#         for author in self.x_autor:
#           authores += author.name
#         self.x_authores=authores

#     x_edit = fields.Char(string='edit',
#                           store=True,
#                           compute='_obtener_edit',
#                           )


#     x_authores = fields.Char(string='autor',
#                           store=True,
#                           compute='_obtener_author',
#                           )
#     x_x=fields.char(string='editoriales')