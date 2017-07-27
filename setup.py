from setuptools import setup

setup(
        name='cdcinfo',
        version='2.0',
        url='http://github.com/zorroblue/cdcinfo',
        author='Rameshwar Bhaskaran',
        author_email='rameshwar.zorro@gmail.com',
        license='MIT',
        entry_points = {
            'console_scripts':['cdcinfo=cdcinfo.cdcparser:main'],
            },
        packages=['cdcinfo'],
        zip_safe=False)
