# -*- coding: utf-8 -*-
# from odoo import http


# class HelloOdoo(http.Controller):
#     @http.route('/hello_odoo/hello_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hello_odoo/hello_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hello_odoo.listing', {
#             'root': '/hello_odoo/hello_odoo',
#             'objects': http.request.env['hello_odoo.hello_odoo'].search([]),
#         })

#     @http.route('/hello_odoo/hello_odoo/objects/<model("hello_odoo.hello_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hello_odoo.object', {
#             'object': obj
#         })

