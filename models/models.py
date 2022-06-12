from odoo import models, fields, api

class centro_comercial(models.Model):
    _name = 'odoo_9modelos.cc'
    _description = 'Define las caracteristicas de un centro comercial'

    name = fields.Char('Direccion', required=True)

    emp_cenc_ids = fields.One2many('odoo_9modelos.emp_c','cc_id',string='Empleados C.C.')
    tiendas_ids = fields.One2many('odoo_9modelos.tie','cc_id',string='Tiendas')
    oficinas_ids = fields.One2many('odoo_9modelos.ofi','cc_id',string='Oficinas')
    socios_ids = fields.One2many('odoo_9modelos.soc','cc_id',string='Socios')

class empleado_cc(models.Model):
    _name = 'odoo_9modelos.emp_c'
    _description = 'Define las caracteristicas de un empleado del centro comercial'
    _order = 'fecha'
    
    dni = fields.Char(string='DNI',required=True, size=9)
    nom = fields.Char(string= 'Nombre')
    ape = fields.Char(string= 'Apellidos')
    fecha = fields.Date(string='Fecha de incorporación')
    anios = fields.Integer(string='Años', default=18)
    tipo = fields.Selection(string='Tipo trabajo', selection=[('s','Seguridad'),('g','Gerente'),('l','Limpieza')],default = 'l')

    cc_id = fields.Many2one('odoo_9modelos.cc',string='Centro Comercial')

class tienda(models.Model):
    _name = 'odoo_9modelos.tie'
    _description = 'Nombre de la tienda y su tipo'

    name = fields.Char('Nombre', required=True)
    tipo = fields.Char('Tipo tienda', required = True)

    cc_id = fields.Many2one('odoo_9modelos.cc',string='Centro Comercial')

    emp_tie_ids = fields.One2many('odoo_9modelos.emp_t','tie_id',string='Empleados T.')
    productos_ids = fields.One2many('odoo_9modelos.prod','tie_id',string='Productos')

class empleado_tie(models.Model):
    _name = 'odoo_9modelos.emp_t'
    _description = 'Define las caracteristicas de un empleado de tienda'
    _order = 'fecha'
    
    dni = fields.Char(string='DNI',required=True, size=9)
    nom = fields.Char(string= 'Nombre')
    ape = fields.Char(string= 'Apellidos')
    fecha = fields.Date(string='Fecha de incorporación')
    anios = fields.Integer(string='Años', default=18)
    tipo = fields.Selection(string='Tipo trabajo', selection=[('d','Dependiente'),('g','Gerente')],default = 'd')

    tie_id = fields.Many2one('odoo_9modelos.tie',string='Tienda')

class producto(models.Model):
    _name = 'odoo_9modelos.prod'
    _description = 'Define los caracteristicas de los productos'

    nom = fields.Char(string= 'Nombre',required=True)
    coste = fields.Float('Coste',(3,2), default=0.0)

    proveedores_ids = fields.One2many('odoo_9modelos.prov','prod_id',string='Proveedores')

    tie_id = fields.Many2one('odoo_9modelos.tie',string='Tienda')

class proveedor(models.Model):
    _name = 'odoo_9modelos.prov'
    _description = 'Define los caracteristicas de los proveedores'

    dni = fields.Char(string='DNI',required=True, size=9)
    nom = fields.Char(string= 'Nombre')
    ape = fields.Char(string= 'Apellidos')
    coste = fields.Float('Coste',(3,2), default=0.0)

    prod_id = fields.Many2one('odoo_9modelos.prod',string='Productos')

class oficina(models.Model):
    _name = 'odoo_9modelos.ofi'
    _description = 'Nombre de la oficina'

    name = fields.Char('Nombre', required=True)

    cc_id = fields.Many2one('odoo_9modelos.cc',string='Centro Comercial')

    emp_ofi_ids = fields.One2many('odoo_9modelos.emp_o','ofi_id',string='Empleados O.')

class empleado_ofi(models.Model):
    _name = 'odoo_9modelos.emp_o'
    _description = 'Define las caracteristicas de un empleado de oficina'
    _order = 'fecha'
    
    dni = fields.Char(string='DNI',required=True, size=9)
    nom = fields.Char(string= 'Nombre')
    ape = fields.Char(string= 'Apellidos')
    fecha = fields.Date(string='Fecha de incorporación')
    anios = fields.Integer(string='Años', default=18)
    tipo = fields.Selection(string='Tipo trabajo', selection=[('m','Marketing'),('g','Gerente'),('v','Ventas')],default = 'v')

    ofi_id = fields.Many2one('odoo_9modelos.ofi',string='Oficina')

class socios(models.Model):
    _name = 'odoo_9modelos.soc'
    _description = 'Define las caracteristicas de un socio del C.C.'
    _order = 'fecha'
    
    dni = fields.Char(string='DNI',required=True, size=9)
    nom = fields.Char(string= 'Nombre')
    ape = fields.Char(string= 'Apellidos')
    fecha = fields.Date(string='Fecha de incorporación')
    anios = fields.Integer(string='Años', default=18)
    descuento = fields.Integer(string='Descuento', default=5)

    cc_id = fields.Many2one('odoo_9modelos.cc',string='Centro Comercial')
