# 使用 WZRY 子模块

## 预处理
```
git init
git add .gitignore README.md
git commit -m "init"
#
git add setup.py pypi.bat how_to_use_submodule.md build.ps1
git commit -m "public file"
```

## 添加子模块
子模块的文件名是将来的发布软件名字
```
git submodule add -b dev git@github.com:cndaqiang/WZRY.git autowzry
# 提交子模块的添加
git add .gitmodules autowzry
git commit -m "Add autowzry as a submodule"
```

## 初始化和更新子模块
- 初始化子模块: `git submodule init`
- 更新子模块到最新: `git submodule update --remote`

## 同步子模块配置
- 命令: `git submodule sync`

## 克隆时递归同步
- 命令: `git clone --recurse-submodules <main-repo-url>`
