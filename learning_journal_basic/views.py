from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def static_view(filename):
    return lambda request: Response(open(os.path.join(HERE, filename)).read())


def includeme(config):
    config.add_view(static_view('templates/homepage.html'), route_name='home')
    config.add_view(static_view('templates/entry.html'), route_name='detail')
    config.add_view(static_view('templates/newentry.html'), route_name='create')
    config.add_view(static_view('templates/editentry.html'), route_name='edit')