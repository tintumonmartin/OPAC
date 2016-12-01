from openerp.osv import orm, fields

class lecturer_detail(orm.Model):
    _name = 'lecturer.detail'
    _columns = {
                'name': fields.many2one('lecturer.info', 'Name'),
                'dept':fields.related('lecturer.info', 'name', 'dept', string='Department'),
                # 'dept' : fields.many2many('dept.list', 'dept_name_name_rel', 'dept_name', 'name', 'Department'),
                }
