# Summary.
project('sensor-schema', version: '0.1', license: 'proprietary')

install_subdir('data', install_dir: 'schema', strip_directory: true)

pkg = import('pkgconfig')
pkg.generate(
    name: 'sensor-schema',
    description: 'Common sensor schema data',
    variables: 'schemadir=${prefix}/schema',
    version: meson.project_version())
