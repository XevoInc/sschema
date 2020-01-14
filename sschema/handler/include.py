'''
A resolver that searches a list of include paths for YAML files matching the
given name. The include paths must be set prior to validation.
work.
'''

import functools
import pkg_resources
import os

import yaml


HANDLER_NAME = 'sschema'


def _handler(name, include_paths, uri):
    '''Handles an URI of form {name}://'''
    scheme = '{}://'.format(name)
    assert(uri.startswith(scheme))
    uri = uri[len(scheme):]

    for base in include_paths:
        path = os.path.join(base, uri)
        try:
            f = open(path, 'r')
        except FileNotFoundError:
            continue
        else:
            with f:
                return yaml.safe_load(f)
    raise FileNotFoundError('{} handler could not find path "{}" in any of {}'.format(name, uri, include_paths))


def make_handler(include_paths, name=HANDLER_NAME):
    '''Returns an include handler and name (for use with make_resolver) that
    uses the give include paths.'''
    return (functools.partial(_handler, name, include_paths), name)


def make_default_handler():
    '''Returns a default handler, which uses the common schemas defined in
    sschema as the include path.'''
    schema_path = pkg_resources.resource_filename('sschema', 'schema')
    return make_handler([schema_path])
