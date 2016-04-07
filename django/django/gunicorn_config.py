    command = '/webapps/django/bin/gunicorn'
    pythonpath = '/webapps/django/project-name'
    bind = '127.0.0.1:8001'
    workers = 3
    user = nobody