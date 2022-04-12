from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-lira",
    version="0.0.1",
    author="Rodrigo_lira",
    author_email="rodrigorevestrex@hotmail.com",
    description="Image processing package to resize and analize images and histogram",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Talicatwolf/processar-imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)