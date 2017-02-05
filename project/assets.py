import os

from django.conf import settings
from django_assets import Bundle, register

main_js = [
    'js/jquery.min.js',
    'js/bootstrap.min.js',
    'js/jquery.timeago.js',
    'js/jquery.timeago.ru.js',
    'js/jquery.toaster.js',
    'js/xbbcode.js',
    'js/angular.min.js',
    'js/angular-route.min.js',
    'js/angular-resource.min.js',
    'js/angular-cookies.min.js',
    'js/ngprogress-lite.min.js',
    'js/app/app.js',
]

configs = ['js/app/config.js']
controllers = ['js/app/controller.js']
factories = ['js/app/factory.js']
filters = ['js/app/filter.js']
directives = []


def import_js():
    for app in settings.INSTALLED_APPS:
        if app.find('project.apps.', 0, 13) == -1:
            continue

        app_name = app[13:]
        app_dir = '%s/project/apps/%s/static/js/' % (settings.BASE_DIR, app_name)

        try:
            files = os.listdir(app_dir)
        except FileNotFoundError:
            continue

        for file in files:
            file_dir = app_dir + file
            if file == app_name + '.config.js':
                configs.append(file_dir)
            if file == app_name + '.controller.js':
                controllers.append(file_dir)
            if file == app_name + '.factory.js':
                factories.append(file_dir)
            if file == app_name + '.filter.js':
                filters.append(file_dir)
            if file == app_name + '.directive.js':
                directives.append(file_dir)


import_js()

js = Bundle(
    *main_js,
    *configs,
    *factories,
    *directives,
    *controllers,
    *filters,
    output='bundle/all_js.js'
)

css = Bundle(
    'css/bootstrap.min.css',
    'css/index.css',
    output='bundle/all_css.css'
)

register('all_js', js)
register('all_css', css)

# Create all_html
# for app in settings.INSTALLED_APPS:
#     if app.find('project.apps.', 0, 13) == -1:
#         continue
#
#     app_name = app[13:]
#     app_dir = '%s/project/apps/%s/static/html/' % (settings.BASE_DIR, app_name)
#
#     try:
#         files = os.listdir(app_dir)
#     except FileNotFoundError:
#         continue
#
#     for file in files:
#         file_dir = app_dir + file
#         app_name