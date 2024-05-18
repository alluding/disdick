from typing import List, Dict, Optional

from setuptools import setup, find_packages
import subprocess
import re

def get_version() -> str:
    version: str = '2.4.4'
    if not version:
        raise RuntimeError('version is not set')

    if version.endswith(('a', 'b', 'rc')):
        try:
            commit_count = subprocess.check_output(['git', 'rev-list', '--count', 'HEAD']).decode('utf-8').strip()
            version += commit_count
            commit_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('utf-8').strip()
            version += '+g' + commit_hash
        except subprocess.CalledProcessError:
    return version

def read_readme() -> str:
    try:
        with open('README.rst', 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return ''

extras_require: Dict[str, List[str]] = {
    'voice': ['PyNaCl>=1.3.0,<1.6'],
    'docs': [
        'sphinx==4.4.0',
        'sphinxcontrib_trio==1.1.2',
        'sphinxcontrib-websupport',
        'typing_extensions>=4.3,<5',
    ],
    'speed': [
        'orjson>=3.5.4',
        'aiodns>=1.1',
        'Brotli',
        f'cchardet==2.1.7; python_version < "3.10"',
    ],
    'test': [
        'coverage[toml]',
        'pytest',
        'pytest-asyncio',
        'pytest-cov',
        'pytest-mock',
        'typing_extensions>=4.3,<5',
    ],
}

def setup_package() -> None:
    setup(
        name='alluding',
        author='cop-discord',
        url='https://github.com/alluding/disdick',
        project_urls={
            'Documentation': 'https://discordpy.readthedocs.io/en/latest/',
            'Issue tracker': 'https://github.com/alluding/disdick/issues',
        },
        version=get_version(),
        packages=find_packages(),
        license='MIT',
        description='A Python wrapper for the Discord API, forked from disdick - discord.py.',
        long_description=read_readme(),
        long_description_content_type='text/x-rst',
        include_package_data=True,
        install_requires=[
            'aiohttp', 'aiodns', 'orjson', 'typing_extensions', 'psutil', 'durations_nlp', 'fast_string_match'
        ],
        extras_require=extras_require,
        python_requires='>=3.8.0',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: MIT License',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Topic :: Internet',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities',
            'Typing :: Typed',
        ],
    )

setup_package()
