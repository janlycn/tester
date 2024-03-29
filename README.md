# tester

自动化集成测试项目，基于 python3

- [项目介绍](docs/introduction.md)
- [相关环境搭建](docs/environment.md)
- [关于 appium](docs/about-appium.md)
- [关于 pytest](docs/about-pytest.md)
- [Desired Capabilities 配置参考](docs/desired-capabilities.md)
- [应用元素定位方法](docs/check-elements.md)

## 使用

首先查看[项目介绍](docs/introduction.md)，环境搭建参考[相关环境搭建](docs/environment.md)

安装依赖

```shell
pip3 install -r requirements.txt
```

执行 bootstrap-android 目录下 run.py

```shell
python tester/bootstrap-android/run.py all
```

## 相关资源

[appium 文档](http://appium.io/docs/en/about-appium/getting-started/index.html#getting-started)

[appium 桌面服务器下载](https://github.com/appium/appium-desktop/releases)

[XCUITest 驱动程序（iOS 和 tvOS 应用程序）](http://appium.io/docs/en/drivers/ios-xcuitest/index.html)

[UiAutomator2 驱动程序（适用于 Android 应用）](http://appium.io/docs/en/drivers/android-uiautomator2/index.html)

[Windows 驱动程序（用于 Windows 桌面应用程序）](http://appium.io/docs/en/drivers/windows/index.html)

[Mac 驱动（适用于 Mac 的桌面应用程序）](http://appium.io/docs/en/drivers/mac/index.html)

[Espresso 驱动程序（适用于 Android 应用）](http://appium.io/docs/en/drivers/android-espresso/index.html)

[pytest文档](http://pytest.org/en/latest/contents.html)
