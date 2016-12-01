from openerp.osv import orm, fields

class dept_list(orm.Model):
    _name = 'dept.list'
    _rec_name = 'dept_name'
    _columns = {
                'dept_name':fields.char('Department Name', size=30),
                # 'dept_name':fields.many2one('dept.list', 'Department Number', size=10),
    }
    _sql_constraints = [
                        ('dept_uniq', 'unique(dept_name)', 'Name already exists! \n Please enter a New Department Name.')
                        ]
    

class course_detail(orm.Model):
    _name = 'course.detail'
    _rec_name = 'course_name'
    _columns = {
                'course_code':fields.integer('Course Code', size=4),
                'course_name':fields.char('Course Name', size=30),
                'dept_name':fields.many2one('dept.list','Department Name'),
    }
    _sql_constraints = [
        ('course_code_uniq', 'unique(course_code)', 'Course Code already exists! \n Please enter a New Course Code.'),
        ('course_name_uniq', 'unique(course_name)', 'Course Name already exists! \n Please enter a New Course Name.'),
    ]