from setuptools import setup


from google_maps_reviews import VERSION


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='google-maps-reviews',
    version=VERSION,
    description='Google Maps Reviews API SDK',
    long_description=readme(),
    classifiers = ['Programming Language :: Python',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: OS Independent',
                    'Intended Audience :: Developers',
                    'Topic :: Utilities',
    ],
    keywords='google maps reviews api sdk scraper parser',
    url='https://github.com/outscraper/google-maps-reviews-python',
    author='Outscraper',
    author_email='developers@outscraper.com',
    license='MIT',
    packages=['google_maps_reviews'],
    install_requires=['requests'],
    include_package_data=True,
    zip_safe=False,
    long_description_content_type='text/x-rst',
)
