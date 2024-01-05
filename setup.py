from setuptools import setup, find_packages

setup(
    name='HealthAnalytics',
    version='0.1',
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for health data analysis and visualization.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'geopandas',
        'matplotlib',
        'plotly',
        'scikit-learn',
        'tensorflow',
        'keras',
        'jupyter',
        'ipykernel'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)