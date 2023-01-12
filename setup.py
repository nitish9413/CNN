import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "CNN"
AUTHOR_USER_NAME = "NITISH KATKADE"
SRC_REPO = "deepClassifier"
AUTHOR_EMAIL = "nitishkatkade94@gmail.com"


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="CNN for image classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

