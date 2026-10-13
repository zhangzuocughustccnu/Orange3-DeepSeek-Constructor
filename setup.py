#!/usr/bin/env python
"""Orange3 add-on: DeepSeek Constructor.

Packaging metadata for the PyPI release of the DeepSeek Constructor widget.
"""
from setuptools import setup, find_packages

# ---------------------------------------------------------------------------
# Package metadata
# ---------------------------------------------------------------------------
NAME = "Orange3-DeepSeek-Constructor"
VERSION = "0.0.2"

AUTHOR = "Zuo Zhang and Yuxin Zhang"
AUTHOR_EMAIL = "zhangzuocug@163.com"

GITHUB_USER = "zhangzuocughustccnu"
GITHUB_URL = "https://github.com/%s/Orange3-DeepSeek-Constructor" % GITHUB_USER
URL = GITHUB_URL

DESCRIPTION = (
    "DeepSeek add-on for Orange3: construct a text field with the DeepSeek LLM."
)

LICENSE = "MIT"

KEYWORDS = [
    "orange3 add-on",
    "orange3",
    "deepseek",
    "llm",
    "text mining",
]

with open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

# Only classifiers that exist in the official PyPI classifier list.
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Environment :: Plugins",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]

PROJECT_URLS = {
    "Homepage": GITHUB_URL,
    "Source": GITHUB_URL,
    "Bug Tracker": GITHUB_URL + "/issues",
}

# ---------------------------------------------------------------------------
# Packaging
# ---------------------------------------------------------------------------
PACKAGES = find_packages()

PACKAGE_DATA = {
    "orangecontrib.deepseek.widgets": ["icons/*"],
}

INSTALL_REQUIRES = [
    "Orange3",
    "openai>=1.0",   # the DeepSeek API is called through the OpenAI SDK
]

ENTRY_POINTS = {
    # Declares this distribution as an Orange add-on, so that the Orange
    # add-on manager and the widget registry can discover it.
    "orange3.addon": (
        "deepseek = orangecontrib.deepseek",
    ),
    # Declares where the widgets live: 'category name = package path'
    "orange.widgets": (
        "DeepSeek = orangecontrib.deepseek.widgets",
    ),
}

# `orangecontrib` is shared by every Orange add-on.  The pkg_resources style
# namespace declaration keeps this add-on compatible with the others.
NAMESPACE_PACKAGES = ["orangecontrib"]


if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=URL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        license=LICENSE,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        include_package_data=True,
        install_requires=INSTALL_REQUIRES,
        entry_points=ENTRY_POINTS,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        project_urls=PROJECT_URLS,
        python_requires=">=3.8",
        namespace_packages=NAMESPACE_PACKAGES,
        zip_safe=False,
    )