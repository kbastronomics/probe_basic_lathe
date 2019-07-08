from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="probe_basic_lathe",
    version="0.0.1",
    author="Chris Polanski",
    author_email="",
    description="Probe Basic Lathe - A QtPyVCP based Virtual Control Panel for LinuxCNC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kbastronomics/probe_basic_lathe",
    download_url="https://github.com/kbastronomics/probe_basic_lathe/tarball/master",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'probe_basic_lathe=probe_basic_lathe:main',
        ],
        'qtpyvcp.vcp': [
            'probe_basic_lathe=probe_basic_lathe',
        ],
    },
    install_requires=[
       # 'qtpyvcp',
       # 'docopt',
    ],
    # dependency_links=[
    #     'https://github.com/kcjengr/qtpyvcp/tarball/master#egg=qtpyvcp-0.0.1'
    # ]
)
