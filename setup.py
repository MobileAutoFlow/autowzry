from setuptools import setup, find_packages

setup(
    name='autowzry',
    version='2.3.0.a8',
    # 版本号后缀说明：
    # - a1：早期测试版（Alpha 版本）
    # - b1：功能较完整但可能有问题的测试版（Beta 版本）
    # - rc1：接近最终稳定版的发布候选版本（Release Candidate）
    # - dev1：开发中版本（未完成，内部测试）
    # - post1：正式版发布后的补丁版本
    # 示例：'2.3.0a1' 表示 2.3.0 的第 1 个 Alpha 测试版
    author='cndaqiang',
    author_email='who@cndaqiang.ac.cn',
    description='王者荣耀·自动化农活脚本',
    long_description=open('autowzry/README.md', encoding='utf-8').read(),  # 从 autowzry/README.md 读取 long description
    long_description_content_type='text/markdown',
    packages=find_packages(),  # 自动查找所有子包
    # 需要在AutoWZRY下面创建__init__.[y]
    package_data={             # 指定需要包含的额外文件
        'autowzry': [
            'assets/*',         # 包括 autowzry/assets 下的所有文件
            'README.md',         # 包括 autowzry/assets 下的所有文件
            'LICENSE',         # 包括 autowzry/assets 下的所有文件
        ],
    },
    include_package_data=True,  # 自动包含 package_data 中指定的文件
    url='https://github.com/cndaqiang/WZRY',
    install_requires=[
        'airtest-mobileauto>=2.1.3',
    ],
    entry_points={
        'console_scripts': [
            'autowzyd=autowzry.wzyd:main',  # 直接引用脚本文件
            'autowzry=autowzry.wzry:main',  # 直接引用脚本文件
            'autotiyanfu=autowzry.tiyanfu:main',  # 直接引用脚本文件
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
    python_requires='>=3.6',
)