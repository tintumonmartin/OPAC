from openerp.osv import fields, orm

class opac(orm.Model):
    _name = 'opac'
    _columns = {}
    def show_studentinfo(self, cr, uid, ids, context=None):
        return {
            'name': ('Student Info'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'student.info',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target':'new'
        }
    def show_lecturerinfo(self, cr, uid, ids, context=None):
        return {
            'name': ('Lecturers Info'),
            'view_type': 'tree',
            'view_mode': 'tree',
            'res_model': 'lecturer.info',
            'view_id': False,
            'type': 'ir.actions.act_window',
        }
    def show_bookreserve(self, cr, uid, ids, context=None):
        return {
            'name': ('Lecturers Info'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'book.reserve',
            'view_id': False,
            'type': 'ir.actions.act_window',
        }
    def show_coursedetail(self, cr, uid, ids, context=None):
        return {
            'name': ('Lecturers Info'),
            'view_type': 'tree',
            'view_mode': 'tree',
            'res_model': 'course.detail',
            'view_id': False,
            'type': 'ir.actions.act_window',
        }