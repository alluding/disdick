from typing import List, Dict, Optional

from setuptools import setup, find_packages
import re

version = '2.4.4'
if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    try:
        import subprocess

        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

readme: str = ''

try:
    with open('README.rst') as f:
        readme = f.read()
except: pass

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
        version=version,
        packages=[
            'discord',
            'discord.types',
            'discord.ui',
            'discord.webhook',
            'discord.app_commands',
            'discord.ext.commands',
            'discord.ext.tasks',
        ],
        license='MIT',
        description='A Python wrapper for the Discord API, forked from disdick - discord.py.',
        long_description=readme,
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
