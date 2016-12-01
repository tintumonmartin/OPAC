{
    'name' : 'OPAC PU',
    'summary': """Online Public Access Catalogue""",
    'version' : '1.1',
    'author' : 'Tintumon. M - Sodexis',
    'sequence' : 1,
    'category' : 'Generic Modules/Others',
    'website' : 'http://www.sodexis.com',
        'description': """
        A sample module for managing Online Public Access Catalogue:
            - Students, Research scholars and Lecturers individual 
            - Library Book's and journal's information.
            - Maintaining Book/journals stock list.
            - Lending of Book.
            - Student details about lending book, due amount.
            - etc.,
    """,
    'depends' : ['base'],
    'data' : ['security/opac_security.xml',
              'security/ir.model.access.csv',
              'wizard/lecturer_info_wizard_view.xml',
              'opac_view.xml',
              'studentinfo_view.xml',
              'lecturerinfo_view.xml',
              'deptlist_view.xml',
              # 'coursedetail_view.xml',
              'bookstock_view.xml',
              # 'bookreserve_view.xml',
              'studentinherit_view.xml',
              'lecturerinherit_view.xml',
              'subjectmarks_view.xml',
              'lecturerdetail_view.xml',
              'sequence.xml',
              'bookreserve_workflow.xml',
              
              ],
    'active': True,
    'installable': True
}
