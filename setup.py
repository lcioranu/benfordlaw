import setuptools

REQUIRED_PACKAGES = [
    'flask',
    'flask-accept',
    'flask-expects-json',
    'pandas==1.3.3',
    'waitress'
]

MAJOR = '0'
MINOR = '1'
PATCH = '0.dev'

VERSION = ".".join((MAJOR, MINOR, PATCH))
setuptools.setup(
    name='benford-service',
    version=VERSION,
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_namespace_packages(include=['benfordlaw.*']),
    url='https://github.com/lcioranu/benford',
    author='Lucian Cioranu',
    author_email='lucian.cioranu@gmail.com',
    description='A test project',
    zip_safe=False
)