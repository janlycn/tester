# 项目说明

该项目不是框架，确切来说是一个测试项目 bootstrap
该项目的目的一是学习如何使用 appium 测试移动应用，二是藉此写一个集成测试项目模型，以便在项目中可以快速应用

## 技术架构

python3

appium

pytest 或者 unittest(pytest 支持执行 unittest)

## 如何使用

新开项目的时候直接拷贝对应 bootstrap 目录，比如测试安卓项目，就拷贝 bootstrap-android，直接使用

比如有一个 demo 安卓应用：

1. 拷贝 bootstrap-android 重命名为 demo
2. 在对应目录编写代码
3. 配置 settings.py
4. 执行 run.py 开始用例测试
5. 在 reports 里查看测试报告

## 引导项目结构介绍

### actions 文件夹

应用页面动作流程的集合，小的动作比如输入、点击，大的动作集合比如 注册、登录等等，推荐约定以页面维度为一个 python 文件

### pages 文件夹

应用页面元素集合，推荐约定以页面维度为一个 python 文件

### reports

输出的测试报告

### suites

如果要使用 unittest，该目录存放测试套件（test suite），如果单纯使用 pytest，该目录可以删除

### tests

项目的所有测试用例，用例文件约定以 test\_ 开头

### run.py

用例运行文件，配合 settings.py 下 TEST_COLLECTION 配置使用，比如有如下配置

```python
TEST_COLLECTION = {
    'home': {
       "pattern": 'test_page_home.py',
       "report": 'test_page_home.html'
    },
    'home_method': 'test_page_home.py::TestPageHome::test_click_home_content'
}
```

则可以通过执行 run.py 并且传入想要运行的 key 执行测试用例；如果传入 all 则执行 tests 下所有用例

```shell
python tester/bootstrap-android/run.py home

python tester/bootstrap-android/run.py all
```

更多细节请查看代码

## 设想

1. 初期项目只集成 appium 和 pytest 和 unittest
2. 后期加入 selenium 或者 pyppeteer 测试 web 端
3. docker 部署
4. jenkins+allure+pytest 持续集成
