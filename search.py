from openerp.osv import orm, fields

class opac_search(orm.Model):
    _name = 'opac.search'
    _columns = {
        'name': fields.char('Name', size=40),
        'department': fields.one2many('dept.name', '', 'Lines'),
    }