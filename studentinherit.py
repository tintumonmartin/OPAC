from openerp.osv import orm, fields

class student_inherit(orm.Model):
    _name = 'student.inherit' 
    _inherit = 'student.info' 
    #Do not touch _name it must be same as _inherit
    #_name = 'student.info'
    _columns = {
            'admissionstatus':fields.boolean('Admission Status'),
            'reason':fields.html('Reason for rejection of admission')
            }