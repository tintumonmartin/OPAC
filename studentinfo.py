from openerp.osv import orm, fields
from datetime import datetime
from dateutil import parser
import re
from _smbc import Context
from dns.rdatatype import NULL

class student_info(orm.Model):
    _name = 'student.info'
    def _convert_capital(self, cr, uid, ids, field_names, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = ('%s %s' % (record.name or '', record.lname or '')).upper()
        return res
    def _inverse_capital(self, cr, uid, id, name, value, args, context=None):
        return self.write(cr, uid, [id], {'fullname': value and value.lower()}, context=context)
#     def _inverse_capital(self, cr, uid, ids, inverse_name, value, arg, context=None):
#         # value.title()
#         return self.write(cr, uid, [id], {'name': value and value.lower()}, context=context)
    def _convert_titlecapital(self, cr, uid, ids, name_convert, arg, context=None):
        value = {}
        for record in self.browse(cr, uid, ids, context=context):
            temp = '%s %s' % (record.name or '', record.lname or '')
            value[record.id] = temp.title() if temp else False
        return value
    def _search_capname(self, cr, uid, id, obj, args, context=None):
        operand = args[0][2]
        operator = args[0][1]
        values = operand.split('/')
        group_name = values[0]
        where = [('fullname', operator, group_name)]
        if len(values) > 1:
            application_name = values[0]
            group_name = values[1]
            where = ['|', ('category_id.fullname', operator, application_name)] + where
        return where
        # return [('id', 'in')]
        # return [('id', 'in', [1, 5])]
    def  validateemail(self, cr, uid, ids, email, context=None):
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
        else:
            raise orm.except_orm('Invalid Email', 'Please enter a valid email address')
    
    _rec_name = 'fullname' 
   
    _columns = {
        'name': fields.char('First Name', size=40),
        'lname': fields.char('Last Name', size=40),
        # Without search function, with store
        'fullname':fields.function(_convert_titlecapital, string='Student Name', type='char', store=True),
        # With search function,without store
        'capname': fields.function(_convert_capital, fnct_inv=_inverse_capital, fnct_search=_search_capname, string='Capital Name', type='char'),
                    # store={'student_info': (lambda self, cr, uid, ids, c={}: ids, ['capname'], 20),}),
        'dob' :  fields.date('Date Of Birth'),
        'gender' : fields.selection([('M', 'Male'), ('F', 'Female')], string='Gender'),
        'email': fields.char('E-mail', size=30),
        'contact': fields.char('Mobile Number', size=15),
        # 'contact': fields.integer('Mobile Number', size=15),#temporarychange
        # 'address': fields.html('Address', size=100),
        'street': fields.char('Street', size=128),
        'street2': fields.char('Street2', size=128),
        'zip': fields.char('Zip', change_default=True, size=24),
        'city': fields.char('City', size=128),
        'state_id': fields.many2one("res.country.state", 'State'),
        'country_id': fields.many2one('res.country', 'Country'),
        'country': fields.related('country_id', type='many2one', relation='res.country', string='Country',
                                  deprecated="This field will be removed as of OpenERP 7.1, use country_id instead"),
        'regno' : fields.char('Register No:'),
        # , required=True
        'status': fields.boolean('Status of Student'),
        'dept' : fields.many2one('dept.list', 'Department'),
        'doj' : fields.date('Date of Joining'),
        'docc':fields.date('Date of Completion'),
        'todate':fields.date('Today'),
        'age' : fields.integer('Age'),
        'image':fields.binary('Image'),
        'course_name':fields.many2one('course.detail', 'Course Name'),
    }
    _defaults = {
                 # 'regno': lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'reg_code'),
                 'status': 'True',
                 'todate': lambda *a: datetime.today().strftime('%Y-%m-%d'),
                 'capname':'',
                 'fullname':'',
                 }
    _sql_constraints = [('reg_uniq', 'unique(regno)', 'Please enter a New Register no. It must be Unique!'),
                        ('age_check', 'CHECK (age>15)', 'You\'re not elible to join in University. You must be above 15 Year old!'), ]
    def onchange_fullname(self, cr, uid, ids, name, lname, context=None):
        # value = {}
        # for record in self.browse(cr, uid, ids, context=context):
        fullname = '%s %s' % (name, lname)
            # fullname = '%s %s' % (record.name or '', record.lname or '')
            # It will add fname(First Name) and lname(Last Name)
        return {'value':{'fullname':fullname}}
    def onchange_getage_id(self, cr, uid, ids, dob, context=None):
        if dob:
            current_age = datetime.now().year - parser.parse(dob).year
            print current_age
            return {'value':{'age':current_age}}
        else:
            return {'value':{'age':0}}
        # return {'value':{'age':0}} if dob == False else {'value': {'age':current_age}}
        # return {'value':{}, 'warning':{'Your Age':'warning', 'message':'Your message'}}
    def copy(self, cr, uid, id, default=None, context=None):
        if default is None:
            default = {}
        copyname = self.read(cr, uid, [id], ['lname'], context)[0]['lname']
        print copyname
        default.update({'lname': ('%s (copy)') % copyname})
        default.update({'regno': ''})
        return super(student_info, self).copy(cr, uid, id, default, context)
    def dummy(self, cr, uid, ids, context=None):
        pass
