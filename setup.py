from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="personal_assistant",
    version="1.0.5",
    author="group-8",
    author_email="pysankanataliia@gmail.com",
    description="Package to assist your contacts, notes and files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nataliia-pysanka/assistant",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=['pathlib==1.0.1'],
    entry_points={'console_scripts': [
        'assistant=app.main_menu:initial_main'
    ]}
)