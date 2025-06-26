from setuptools import setup, find_packages

setup(
    name = "styler",
    version = "1.0",
    
    description = "",
    long_description = "",
    long_description_content_type = "text/markdown",

    keywords = ["python", "color", "colors", "easy", "cmd", "app", "manage", "text", "colour", "ansi", "terminal", "gradient", "gradients", "bold", "italic", "underscore", "command", "commands"],

    packages = find_packages(),
    install_requires = ["typing", "dataclasses", "enum"],
                        
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)