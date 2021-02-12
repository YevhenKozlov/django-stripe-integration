from setuptools import setup

setup(
    name='django-stripe-integration',
    install_requires=[
        'Django>=2.0',
        'dj-stripe>=2.4.3',
        'stripe>=2.55.1'
    ]
)
