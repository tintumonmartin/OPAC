from openerp.osv import fields, orm
from datetime import datetime
from dateutil import parser
# from lxml import etree

class lecturer_info_wizard(orm.TransientModel):
    _name = 'lecturer.info.wizard'
    _description = 'Wizard to get year of experience to lecturers info'
    _columns = {
            'startyear':fields.date('Starting Date'),
            'endyear':fields.date('Ending Date'),
            'experience':fields.integer('Year of Experience'),
            }
    _defaults = {
            # 'startyear':datetime.now(),
            # 'endyear': datetime.now(),
        }
    def onchange_getexperience(self, cr, uid, ids, startyear, endyear, context=None):
        
        if startyear and endyear:
            experienc = parser.parse(startyear).year - parser.parse(endyear).year
            experienc = abs(experienc)
            print "End year is TRUE"
            if endyear < startyear:
                print "Invalid: Starting year must be before Ending year"
                return {'warning':{'title':'Invalid Input', 'message':'"Starting year" must be before "Ending year"'}}
            return {'value':{'experience':experienc}}
        else:
            print "end year is FALSE"
            return {'value':{'experience':0}}
        # return {'value':{'experience':0}} if startyear or endyear == False else {'value': {'experience':experienc}}
        # return {'value':{'experience':experienc}}
    def update_experience(self, cr, uid, ids, context):
        experience_obj = self.pool.get('lecturer.info')
        for wizard in self.browse(cr, uid, ids, context=None):
            # experience_year = experience_obj.search(cr, uid, [('order_id', '=', context.get('order_id')), ('experience', '=', wizard.experience.id)])
            # experience_obj.write(cr, uid, experience_year[0], {'experience' : wizard.experience})
            experience_obj.write(cr, uid, context.get('active_id', []), {'experience' : wizard.experience})
        return True
    def this_year(self, cr, uid, ids, context):
        endyr = datetime.today().year
        print endyr
        mod_obj = self.pool.get('ir.model.data')
        view_id = mod_obj.get_object_reference(cr, uid, 'OPAC', 'lecturer_info_wizard')
        return {
            'name': "Lecturer Year of Experience" ,
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': view_id and view_id[1] or False,
            'res_model': 'lecturer.info.wizard',
            'src_model': 'lecturer.info.wizard',
            'type': 'ir.actions.act_window',
            'context': context,
            'target': 'new',
            }
        print "Ending year" + endyr
        endyr = abs(endyr)
        return {'value':{'endyear':endyr}}
