import setuptools

VERSION = "0.0.1"

setuptools.setup(
    name="MCTS Game",
    version=VERSION,
    author="Nathaniel Chavdarov",
    author_email="49632679+NathanielChavdarov@users.noreply.github.com",
    description="Monte Carlo tree search game",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/nathanielchavdarov/mcts-game",
    packages=setuptools.find_packages(),
    package_data={"game": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[],
    setup_requires=["wheel"],
    zip_safe=False,
)
