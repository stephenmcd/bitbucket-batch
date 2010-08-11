from setuptools import setup
 
 
setup(
    name = "bitbucket-batch",
    version = __import__("bitbucket_batch").__version__,
    author = "Stephen McDonald",
    author_email = "stephen.mc@gmail.com",
    description = "A tool for bulk updating access to bitbucket.org repos.",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://bitbucket.org/stephenmcd/bitbucket-batch/",
    py_modules = ["bitbucket_batch",],
    entry_points = """
        [console_scripts]
        bitbucket-batch=bitbucket_batch:main
    """,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
    ]
)
