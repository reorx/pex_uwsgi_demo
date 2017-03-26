# coding: utf-8

import os
import sys


if sys.version_info[0] >= 3:
    from importlib import reload
else:
    from imp import reload


#try:
#    print 'try import amod'
#    import amod
#except ImportError:
#    print 'could not import amod at first'
#

def activate_pex():
    sys.stderr.write('[pex_uwsgi] bootstrapping..\n')

    entry_point = os.environ.get('PEX_ENTRY')
    if not entry_point:
        sys.stderr.write(
            '[pex_uwsgi] couldnt determine pex from PEX_ENTRY environment variable, bailing!\n'
        )
        sys.exit(1)

    sys.stderr.write('[pex_uwsgi] entry_point=%s\n' % entry_point)

    sys.path[0] = os.path.abspath(sys.path[0])
    sys.path.insert(0, entry_point)
    sys.path.insert(0, os.path.abspath(os.path.join(entry_point, '.bootstrap')))

    from _pex import pex_bootstrapper

    pex_bootstrapper.bootstrap_pex_env(entry_point)

    # import & reload in our newly bootstrapped environment
    import pkg_resources
    reload(pkg_resources)

    sys.stderr.write('[pex_uwsgi] sys.path=%s\n\n' % sys.path)
    return


activate_pex()

#print 'activated, import amod'
#import amod
