# -*- coding: utf-8 -*-
{
    'name': "comics_add_fields website",

    'summary': """add_fields
    """,

    'description': """
        Modulo para  agregar 2 campos en website , informacion general autor y editorial
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
        'contacts',
        ],

	'data': [
    'views/add_fields_sitioweb_inventario.xml',
  

    ],
	'demo':[

	],
    'installable':True,
}
