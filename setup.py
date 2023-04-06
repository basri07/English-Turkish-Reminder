from distutils.core import setup
import py2exe

options = {
    'py2exe': {
        'includes': ['win10toast'],
    }
}

setup(
    options=options,
    console=['random_english.py']
)