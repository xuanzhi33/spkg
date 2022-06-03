# SPKG

Language: [English](https://github.com/xuanzhi33/spkg/blob/master/README.md) |
[中文文档](https://github.com/xuanzhi33/spkg/blob/master/README_cn.md)


## 介绍

SPKG (Simple Packager) - 一个简单的命令行工具，用于快速的打包和上传python包到pypi。

## 安装

```
pip3 install spkg
```

## 使用方法

cd到包的目录，执行以下命令：

```
spkg [命令]
```

### 命令说明

- `help`, `-h`: 显示帮助信息并退出
- `upload`, `-u`: 上传这个包到pypi (相当于 'twine upload dist/*')
- `setup`, `-s`: 打包 (相当于 'python3 setup.py sdist')

- `clear`, `-c`: 删除folder下所有的.tar.gz文件，用于清理dist文件夹
- `pkg`, `-p`: 相当于运行`clear`、`setup`和`upload`
- `info`, `-in`: 显示包信息
- `setver`, `-sv`: 设置包版本
- `install`, `-i`: 从pypi安装包，相当于 `pip3 install --upgrade [package]`

以下的命令可以快速的修改包版本并执行`pkg`命令：
(这会编辑setup.py文件中的`version`值)
- `patch`, `-pa`: 用于发布补丁更新 (e.g. 1.0.1 -> 1.0.2)
- `minor`, `-mi` : 用于发布小型更新 (e.g. 1.0.3 -> 1.1.0)
- `major`, `-ma`: 用于发布大型更新 (e.g. 1.1.1 -> 2.0.0)

### 举例

- 上传dist文件夹里的所有文件到pypi:


```
spkg upload
```


- 如果你的包版本为1.4.2，你可以运行下述命令将其setup.py中的版本号修改为1.4.3并打包上传至pypi。


```
spkg patch
```

- 安装一个pypi上的包

```
spkg install [package]
```
