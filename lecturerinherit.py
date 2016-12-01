from openerp.osv import orm, fields
from datetime import datetime
from dateutil import parser

class lecturer_info(orm.Model):
    _name = 'lecturer.info'
    _inherit = 'lecturer.info' 
    _columns = {
            'design' : fields.selection([('P', 'Professor'), ('L', 'Lecturer'), ('G', 'Guest Faculty'), ('R', 'Research Scholar')], string='Designation', required='True'),
            'eligible':fields.boolean('Eligibility'),
            'experience':fields.integer('Year of Experience'),
            'endyear':fields.integer('Ending Date'),
                    }
    def onchange_getage(self, cr, uid, ids, dob, age, context=None):
        print age
        res = super(lecturer_info, self).onchange_getage(cr, uid, ids, dob, context=context)
        age = res.get('value').get('age')
        print age
        res['value'].update({'eligible':True}) if age >= 23 else res['value'].update({'eligible':False})
        return res
    def action_desig(self, cr, uid, ids, context=None):
        mod_obj = self.pool.get('ir.model.data')
        view_id = mod_obj.get_object_reference(cr, uid, 'OPAC', 'lecturer_info_wizard')
        return {
            'name': "Lecturer Year of Experience" ,
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': view_id and view_id[1] or False,
            'res_model': 'lecturer.info.wizard',
            'src_model': 'lecturer.info',
            'type': 'ir.actions.act_window',
            'context': context,
            'target': 'new',
            }
    def this_year(self, cr, uid, ids, context):
        endyr = datetime.today().year
        print endyr        
        return {'value':{'endyear':endyr}}