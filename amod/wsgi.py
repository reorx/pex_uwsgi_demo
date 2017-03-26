# coding: utf-8


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello from amod']


if __name__ == '__main__':
    print 'amod wsgi'
