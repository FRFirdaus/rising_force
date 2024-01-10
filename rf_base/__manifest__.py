{
    'name': "rf_base",
    'summary': """
         RF Base Customize
         """,

    'description': """
         RF Base Customize
    """,
    'author': "Rehan | Fahmi Roihanul Firdaus",
    'website': "https://www.frayhands.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'mail'
    ],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        # 'views/partner_views.xml',
        'views/member_views.xml',
        'views/menu_views.xml'
    ]
}