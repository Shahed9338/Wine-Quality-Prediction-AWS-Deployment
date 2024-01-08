import setuptools

# Read the README file to use as the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package version
__version__ = "0.0.0"

# Repository and author information
REPO_NAME = "Wine-Quality-Prediction-AWS-Deployment"
AUTHOR_USER_NAME = "Shahed9338"
SRC_REPO = "wineQuality"
AUTHOR_EMAIL = "shahediqbal93@gmail.com"

# Set up the package using setuptools
setuptools.setup(
    name=SRC_REPO,  # Package name
    version=__version__,  # Package version
    author=AUTHOR_USER_NAME,  # Author's username
    author_email=AUTHOR_EMAIL,  # Author's email
    description="Wine Quality(in the scale 1-10)",  # Package description
    long_description=long_description,  # Long description from README
    long_description_content="text/markdown",  # Specify that the long description is in Markdown format
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL to the repository
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # URL to the bug tracker
    },
    package_dir={"": "src"},  # Specify the package directory
    packages=setuptools.find_packages(where="src")  # Automatically find and include packages in the 'src' directory
)