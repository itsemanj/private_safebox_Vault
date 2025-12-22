from setuptools import setup, find_packages

setup(
    name="self-vault",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "cryptography>=41.0.0",
    ],
    entry_points={
        "console_scripts": [
            "vault=vault.cli:main",
        ],
    },
    python_requires=">=3.9",
)

