from setuptools import setup, find_packages


def get_requirements(path):

    with open(path) as my_file:

        requirement = my_file.readlines()
        reqmnt = [req.replace('/n', '') for req in requirement]

        if "-e ." in reqmnt:
            reqmnt.remove("-e .")
    return reqmnt


setup(name="simp_lin_reg",
      version="0.0.1",
      author="Mahesh",
      author_email="xyz@gmail.com",
      install_requires=get_requirements("requirements.txt"),
      packages=find_packages())
