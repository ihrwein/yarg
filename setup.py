from setuptools import setup, find_packages

setup(
    name="YARG",
    version="1.0",
    install_requires=['PyYAML',],
    scripts=['runner.py'],
    packages = find_packages(),
    #packages=['yarg'],
    #package_data={'yarg': ['resource/*']},
    data_files=[('resource', ['yarg/resource/main.qml'])],
    entry_points={
        'gui_scripts': [
            'yarg = runner:main'
        ]
    }
)
