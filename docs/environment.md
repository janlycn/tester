# 环境安装

## java 运行环境

到官网下载 jre，配置 JAVA_HOME 等环境变量即可

## Windows - Android 环境 (作参考流程，还没试验)

到[官网](https://developer.android.com/studio)安装 sdk-tool-windows

配置 ANDROID_HOME 环境变量

安装 platform-tools 配置 adb 环境变量

```shell
# 显示当前链接的 devices
adb devices
```

安装 build-tools 并把 aapt 拷贝到 platform-tools 文件夹

## MacOS - Android 环境

参考[文章](https://gist.github.com/Erichain/0ac3a6aaca0c28ad6551)

```shell
brew cask install android-sdk
```

然后.bash_prodile 就要改成 export ANDROID_HOME=/usr/local/share/android-sdk

安装 platform-tools，配置 adb 命令到全局

```shell
sdkmanager platform-tools

ln -s /usr/local/share/android-sdk/platform-tools/adb /usr/local/bin

# 连接夜神模拟器，或直接使用夜神里面的adb
adb connect 127.0.0.1:62001

# 显示当前链接的 devices, 显示 127.0.0.1:62001 device 表示OK
adb devices

# 安装 build-tools 并把 aapt 拷贝到 platform-tools 文件夹
sdkmanager "build-tools;29.0.2"
cp /usr/local/share/android-sdk/build-tools/29.0.2/aapt /usr/local/share/android-sdk/platform-tools/
```

## Android 模拟器

[夜神模拟器](https://www.yeshen.com/)，设备连接：127.0.0.1:62001

## 验证

```shell
appium-doctor --android
```
