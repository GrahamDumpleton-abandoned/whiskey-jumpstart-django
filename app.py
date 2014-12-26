import mod_wsgi.openshift

mod_wsgi.openshift.start('--working-directory', 'example',
        '--url-alias', '/static', 'example/htdocs',
        '--application-type', 'module', 'example.wsgi')
