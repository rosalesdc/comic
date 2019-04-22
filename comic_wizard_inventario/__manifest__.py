# -*- coding: utf-8 -*-
{
    'name': "Wizard para agregar autor editorial",

    'summary': """Ejercicios
    """,

    'description': """
        Modulos funcionales para poner en descripcion autor y editorial asi permitiendo la bsuqueda por editorial y autor
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'stock',
        'product',  

    ],

    # always loaded
	'data': [
	'views/wizard_add.xml',
        
    ],
	'demo':[

	],
    'installable':True,
}
