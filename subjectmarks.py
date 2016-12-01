from openerp.osv import orm, fields
# from OPAC import studentinfo
class mark_list(orm.Model):
    def onchange_gettotal_id(self, cr, uid, ids, internal, external):
        total = internal + external
        val = {
               'total':total
               }
        return {'value': val}
    def onchange_getgrade_id(self, cr, uid, ids, total):
        # , context=None
        if total > 90 and total <= 100:
            grade = 'A+'
        elif total > 80 and total <= 90:
            grade = 'A'
        elif total > 70 and total <= 80:
            grade = 'B'
        elif total > 60 and total <= 70:
            grade = 'C'
        elif total > 50 and total <= 60:
            grade = 'D'
        elif total > 40 and total <= 50:
            grade = 'E'
        elif total > 0 and total <= 40:
            grade = 'F'
        else:
            grade = 'invalid'
        print grade
        grad = {
               'grade':grade
               }
        return {'value': grad}
    _name = 'mark.list'
    _rec_name = 'name'
    
    _columns = {
        'name':fields.many2one('student.info', 'Student Name',domain=[('status','=',True)]),
        'subjectname':fields.many2one('subject.mark','Subject Name'),
        'internal':fields.integer('Internal Marks', size=3),
        'external':fields.integer('External Marks', size=3),
        'total':fields.integer('Total Marks'),
        'grade':fields.selection([('A+', '10'), ('A', '9'), ('B', '8'), ('C', '7'), ('D', '6'), ('E', '5'), ('F', '5<')], string='Grade'),
    }
    _defaults = {
                 # 'grade':'A'
        }
    def dummy(self, cr, uid, ids, context=None):
        pass
class subject_mark(orm.Model):
    _name = 'subject.mark'
    # _rec_name = 'total'
    _inherits = {'mark.list': 'total_marks'}
    # , 'student.info':'student_name'
    def _get_percentage(self, cr, uid, ids, args,):
        pass
    _columns = {
        'student_name':fields.many2one('student.info', 'Name'),
        'total_marks': fields.many2one('mark.list', 'Mark details', required=True, ondelete='cascade'),
        'subjects': fields.selection([('S1', 'Subject 1'), ('S2', 'Subject 2'), ('S3', 'Subject 3'), ('S4', 'Subject 4')], 'Subject'),
        # 'percentage':fields.function('_get_percentage', string='Calculate Percentage', type='string')
    }