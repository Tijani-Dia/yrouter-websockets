from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    "yrouter",
    "websockets",
]

test_requires = [
    "black",
    "isort",
    "flake8",
    "pytest",
    "pytest-asyncio",
]

build_requires = [
    "twine",
    "check-wheel-contents",
]

setup(
    name="yrouter-websockets",
    version="0.2",
    description="URL routing for the websockets library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tidiane Dia",
    author_email="tidiane.dia@therookiecoder.com",
    url="https://github.com/tijani-dia/yrouter-websockets/",
    project_urls={
        "Source": "https://github.com/tijani-dia/yrouter-websockets/",
        "Issue tracker": "https://github.com/tijani-dia/yrouter-websockets/issues/",
    },
    install_requires=install_requires,
    tests_require=test_requires,
    extras_require={
        "test": test_requires,
        "build": build_requires,
    },
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    zip_safe=False,
    license="BSD-3-Clause",
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
