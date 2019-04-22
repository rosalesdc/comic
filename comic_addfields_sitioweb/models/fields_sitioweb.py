# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
import smtplib

class AddProductFields(models.Model):
    _inherit = 'product.template'
   
    @api.one
    @api.model
    def _obtener_edit(self):        
        editoriales=""
        for editorial in self.x_editorial:
          editoriales += editorial.name
        self.x_edit=editoriales
  #      self.write({'x_x': editoriales})
  #      print("holaaaaaaaaaaaaaa")
   

    def _obtener_author(self):
      authores=""
      for author in self.x_autor:
        authores += author.name+", "
      self.x_authores=authores


    x_edit = fields.Char(string='edit',
                          #store=True,
                          compute='_obtener_edit',
                          )

    x_authores=fields.Char(string='autor',
                          #store=True,
                          compute='_obtener_author',)


#    x_x=fields.Char(string='editoriales',)
#    u_u=fields.Char(string='Autores',)