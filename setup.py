from setuptools import setup

setup(
    name="pytest-ipdb-cls",
    packages=["pytest_ipdb_cls"],
    version="0.1",
    description="A py.test helper to enable drop to ipdb debugger on test failure or when pytest.set_trace is used.",
    author="Joseph Kahn",
    author_email="josephbkahn@gmail.com",
    url="https://github.com/JBKahn/pytest-ipdb-cls",
    classifiers=[
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Testing",
    ],
    install_requires=[
        'pytest>=3.1.0',
        'ipdb',
    ],
)
