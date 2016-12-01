from openerp.osv import orm, fields
from datetime import datetime
from dateutil import parser

class lecturer_info(orm.Model):
    _name = 'lecturer.info'
    _columns = {
        'name': fields.char('Name', size=40),
        'dob' :  fields.date('Date Of Birth'),
        'age':fields.integer('Age'),
        'gender' : fields.selection([('M', 'Male'), ('F', 'Female')], string='Gender'),
        'email': fields.char('E-mail', size=30),
        'contact': fields.char('Mobile Number', size=15),
        'address': fields.text('Address', size=200),
        'dept' : fields.many2many('dept.list', 'dept_name_name_rel', 'dept_name', 'name', 'Department'),
    }
    def onchange_getage(self, cr, uid, ids, dob, context=None):
        if dob:
            current_age = datetime.now().year - parser.parse(dob).year            
            return {'value':{'age':current_age}}  
        else:
            return {'value':{'age':0}}
        # return {'value':{'age':current_age}} if dob else {'value':{'age':0}}
    def _check_age_eligible(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            age = record.age
            valreturn = False if age < 15 else True
            return valreturn
    _sql_constraints = [('mobno_uniq', 'unique(contact)', 'Please enter a Your own Mobile no. It must be Unique and personnel!'),
                        ('email_uniq', 'unique(email)', 'Please enter a Your own email id. It must be Unique and personnel!')]
    _constraints = [
                    (_check_age_eligible, 'You\'re too young to became Lecturer/Professor?etc..', ['age']),
                    ]