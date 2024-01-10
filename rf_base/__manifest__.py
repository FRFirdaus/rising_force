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
        'views/member_views.xml',
        'views/base_views.xml',
        'views/race_views.xml',
        'views/pit_boss_views.xml',
        'views/reward_views.xml',
        'views/menu_views.xml'
    ]
}