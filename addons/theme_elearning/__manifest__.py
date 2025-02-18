{
    'name': 'T4Tek Elearning',
    'version': '18.0.1.0.0',

    'category': 'Theme/Website',

    'summary': 'Theme Elearning',
    'description': '',


    'depends': ['website'],
    'data': [
        'views/theme_views.xml',
    #    'views/blocks/s_course.xml',
       'views/customs/header.xml',
       'views/customs/footer.xml',
    #    'views/snippet.xml',
    ],

    'assets': {
        'web.assets_frontend':[
            'theme_elearning/static/src/scss/main.scss',
            "web/static/src/libs/fontawesome/css/font-awesome.css",
        ],
        'point_of_sale._assets_pos': [
            'theme_elearning/static/src/**/*'
        ],

    },
    'license': 'LGPL-3',
}