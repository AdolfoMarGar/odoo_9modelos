# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo9modelos(http.Controller):
#     @http.route('/odoo_9modelos/odoo_9modelos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_9modelos/odoo_9modelos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_9modelos.listing', {
#             'root': '/odoo_9modelos/odoo_9modelos',
#             'objects': http.request.env['odoo_9modelos.odoo_9modelos'].search([]),
#         })

#     @http.route('/odoo_9modelos/odoo_9modelos/objects/<model("odoo_9modelos.odoo_9modelos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_9modelos.object', {
#             'object': obj
#         })
