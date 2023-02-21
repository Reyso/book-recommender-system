from setuptools import setup

with open('README.md','r', encoding='utf-8') as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = 'Machine-Learning-for-Books-Recomender-System'
AUTHOR_USER_NAME = 'Reyso'
SCR_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit','numpy','scikit-learn']

setup(
    name = SCR_REPO,
    version='0.0.1',
    author= AUTHOR_USER_NAME,
    description = 'A small project for Book Recomender System',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = f'http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    author_email = 'reyso.ct@gmail.com',
    packages = [SCR_REPO],
    python_requires = '>=3.8',
    install_requires = LIST_OF_REQUIREMENTS

)