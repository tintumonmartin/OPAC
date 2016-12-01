"""
:The login function is under
::    http://localhost:8069/xmlrpc/common
:For object retrieval use:
::    http://localhost:8069/xmlrpc/object
"""
import xmlrpclib
import pprint
 
user = 'admin'
pwd = 'test'
dbname = 'v7_sample'
model = 'student.info'
 
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
uid = sock.login(dbname , user , pwd)
#pprint uid
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
 
# # CREATE A PARTNER
# partner_data = {'name':'Tintumon', 'gender':'M', 'regno':'1999'}
# print partner_data
# partner_id = sock.execute(dbname, uid, pwd, model, 'create', partner_data)
# partner_data = {'name':'Sambath', 'gender':'M', 'regno':'199'}
# print partner_data
# partner_id = sock.execute(dbname, uid, pwd, model, 'create', partner_data)
  
# # The relation between res.partner and res.partner.category is of type many2many
# # To add  categories to a partner use the following format:
# partner_data = {'name':'Provider2', 'category_id': [(6,0,[3, 2, 1])]}
# # Where [3, 2, 1] are id fields of lines in res.partner.category
#  
# SEARCH PARTNERS
args = [('name', 'like', ' '),]
ids = sock.execute(dbname, uid, pwd, model, 'search', args)
print ids
#  
# READ PARTNER DATA
fields = ['name', 'active', 'vat', 'ref']
results = sock.execute(dbname, uid, pwd, model, 'read', ids, fields)
print results
#  
# # EDIT PARTNER DATA
# values = {'vat':'ZZ1ZZ'}
# results = sock.execute(dbname, uid, pwd, model, 'write', ids, values)
#  
# DELETE PARTNER DATA
results = sock.execute(dbname, uid, pwd, model, 'unlink', ids)