from openerp.osv import orm, fields
class student_Ginfo_student(orm.Model):
   _name = "student.ginfo.student"
   _rec_name = "student_id"
   _inherits = {"student.info.student":"student_id"}
   
   def _calculate_volume(self, cr, uid, ids, field_names, arg, context=None):
       res = {}
       for record in self.browse(cr, uid, ids, context=context):
           if record.id not in res:
               res.update({record.id: {}})
           res[record.id]['volume'] = int(record.height) * int(record.weight) * 100
           res[record.id]['area'] = int(record.height) * int(record.weight)
       return res
   
   def _convert_capital(self, cr, uid, ids, field_names, arg, context=None):
       res = {}
       for record in self.browse(cr, uid, ids, context=context):
           res[record.id] = record.sname and record.sname.upper()
       return res
   def _inverse_capital(self, cr, uid, id, name, value, args, context=None):
#         record = self.browse(cr, uid, id, context=context)
       return self.write(cr, uid, [id], {'sname': value and value.lower()}, context=context)
   def _search_volume(self, cr, uid, obj, name, args, context=None):
       return [('id', 'in', [1, 2])]
   _columns = {
       'student_id':fields.many2one("student.info.student", "Student Name", required=True, ondelete="casacde"),
       'height':fields.char("Height"),
       'weight':fields.char("Weight"),
       'volume': fields.function(_calculate_volume, string='Volume', fnct_search=_search_volume, multi='calculate_height_weight'),
       'area': fields.function(_calculate_volume, string='Area', fnct_search=_search_volume, multi='calculate_height_weight'),
       'sname': fields.char('Name'),
       'cname': fields.function(_convert_capital, fnct_inv=_inverse_capital, type='char', string='Capital Name',
           store={
                  'student.ginfo.student': (lambda self, cr, uid, ids, c={}: ids, ['sname'], 20),
                  }),
       'active': fields.boolean('Active'),
   }
   _defaults = {
       'height': 20,
       'active': True,
   }
   def default_get(self, cr, uid, fields, context=None):
       res = super(student_Ginfo_student, self).default_get(cr, uid, fields, context=context)
       res['weight'] = 30
       return res
   def _search_volume(self, cr, uid, obj, name, args, context=None):
       argoptr = args[0][1]
       argopnd = str(args[0][2])
       cr.execute('select id from student_ginfo_student where maths+chem+physics' + argoptr + '' + argopnd)
       res = cr.fetchall()
       print res, args
       return [('id', 'in', [x[0] for x in res])]