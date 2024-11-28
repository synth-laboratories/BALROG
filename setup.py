import setuptools
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    # Information
    name="balrog",
    description="Benchmark for In Context Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.1.0",
    url="https://github.com/DavidePaglieri/BALROG/",
    author="Davide Paglieri",
    license="MIT",
    keywords="reinforcement learning ai nlp llm",
    project_urls={
        "website": "https://www.balrogai.com/",
    },
    install_requires=[
        "minihack @ file:///opt/balrog/wheels/minihack-0.1.6+3ecb6da-py3-none-any.whl",
        "balrog-textworld @ file:///opt/balrog/wheels/balrog_textworld-1.6.2rc1-cp310-cp310-linux_aarch64.whl",
        "minigrid @ file:///opt/balrog/wheels/minigrid-2.3.1-py3-none-any.whl",
        "baba @ file:///opt/balrog/wheels/baba-0.0.1-py3-none-any.whl",
        "balrog-nle",
    ],
    entry_points={
        "console_scripts": [
            "balrog-post-install=post_install:main",
        ],
    },
    extras_require={
        "dev": [
            "black",
            "isort>=5.12",
            "pytest<8.0",
            "flake8",
            "pre-commit",
            "twine",
        ]
    },
    package_dir={"": "./"},
    packages=setuptools.find_packages(where="./", include=["balrog*"]),
    include_package_data=True,
    python_requires=">=3.8",
)

# Wheels are built with the following commands since building them in the docker container is TIME CONSUMING
# Build wheels for each package
# pip wheel git+https://github.com/balrog-ai/minihack.git
# pip wheel git+https://github.com/balrog-ai/TextWorld.git
# pip wheel git+https://github.com/BartekCupial/Minigrid.git
# pip wheel git+https://github.com/nacloos/baba-is-ai.git
