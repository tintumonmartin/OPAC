from openerp.osv import orm, fields

class book_stock(orm.Model):
    _name = 'book.stock'
    _rec_name = 'book_name'
    _columns = {
            'book_id':fields.char('Book ID'),
            'book_name':fields.char('Book Name', size=100),
            # 'book_name':fields.many2one('book.reserve', 'Book Name', ondelete='restrict'),
            # , select=True
            'image':fields.binary('Image'),
            'book_author':fields.char('Author Name', size=50),
            'book_description':fields.text("Book Description", size=200),
            'book_count':fields.integer('Stock', size=2),
            'book_status':fields.boolean('Status'),
            'book_state':fields.selection([('Available', 'Available'), ('Unavailable', 'Unavailable')], 'State', required=True),
            }
    def create(self, cr, uid, vals, context=None):
        print vals
        if not vals:
            vals = {}
        if context is None:
            context = {}
        vals['book_id'] = self.pool.get('ir.sequence').get(cr, uid, 'book.code')
        print vals
        return super(book_stock, self).create(cr, uid, vals, context=context)
     
    _defaults = {
                 'book_count': lambda *a: 8,  # Set 8 as the default value for the field "book_count".
                 # For book_id sequence no. It will generate when form loads. and even if we discard it then next number will generate instead of discarded no.
                 # to over come we overwrite create method and generated sequence in that method.
                 # 'book_id': lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'book.code'),
                 'book_status':True,
     }

import netsvc

class book_reserve(orm.Model):
    _name = 'book.reserve'
    _columns = {
                'name':fields.many2one('student.info', 'Student Name', domain=[('status', '=', 'True')], ondelete='cascade'),
                # required=True,
                # 'reserved_book':fields.one2many('book.stock', 'book_name', 'Book Name'),
                'lend_book':fields.many2many('book.stock', 'book_id_name_rel', 'book_id', 'name', string='Lend Book', domain=[('book_status', '=', 'True')], ondelete='cascade'),
                'track_state':fields.selection([
                                    ('a', 'Available'),
                                    ('r', 'Reserved'),
                                    ('t', 'Taken'),
                                    ('l', 'Lost'), ], 'Status')
                }
    _defaults = {
                 'track_state':'a'
        }
    def button_reserved(self, cr, uid, ids, context=None):
        # if ids == None:
        #    return{}
        print "reserved"
        return self.write(cr, uid, ids, {'track_state':'r'}, context=context)
    def button_taken(self, cr, uid, ids, context=None):
        # if ids == None:
        #    return{}
        print "taken"
        return self.write(cr, uid, ids, {'track_state':'t'}, context=context)
    def button_return_cancel(self, cr, uid, ids, context=None):
        # netsvc.LocalService("workflow").trg_create(uid, 'bookreserve_wkf', ids[0], cr)
        # if context is None:
        #    context = {}
        print "return + cancel"
        return self.write(cr, uid, ids, {'track_state':'a'}, context=context)
    
    def button_lost(self, cr, uid, ids, context=None):
        print "return + cancel"
        return self.write(cr, uid, ids, {'track_state':'l'}, context=context)
    
    _sql_constraints = [('name', 'unique(name)', 'He has already taken Book! \n So,Please go to his own record to add books')]
#     def onchange_getbooklist(self, cr, uid, ids, name, context=None):
#         res = {}
#         if name:
#             obj = self.pool.get('book_id_name_rel').browse(cr, uid, name)
#             res['lend_book'] = obj.lend_book
#             
#             # res['field2'] = obj.field2
#             # value accordingly, its just to prove you that values are filled on onchange.
#         return {'value': res}
