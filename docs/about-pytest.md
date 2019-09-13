# pytest 介绍

pytest 是一个非常成熟的全功能的 Python 测试框架，主要特点有以下几点：

1. 简单灵活，容易上手，文档丰富；
2. 支持参数化，可以细粒度地控制要测试的测试用例；
3. 能够支持简单的单元测试和复杂的功能测试，还可以用来做 selenium/appnium 等自动化测试、接口自动化测试（pytest+requests）;
4. pytest 具有很多第三方插件，并且可以自定义扩展，比较好用的如 pytest-selenium（集成 selenium）、pytest-html（完美 html 测试报告生成）、pytest-rerunfailures（失败 case 重复执行）、pytest-xdist（多 CPU 分发）等；
5. 测试用例的 skip 和 xfail 处理；
6. 可以很好的和 CI 工具结合，例如 jenkins

## 安装

```shell
pip install pytest
```

## 编写规则

1. 测试文件以 test\_开头（以\_test 结尾也可以）
2. 测试类以 Test 开头，并且不能带有 init 方法
3. 测试函数以 test\_开头
4. 断言使用基本的 assert 即可

## fixture 的 scope 参数

scope 参数有四种，分别是'function','module','class','session'，默认为 function。

1. function：每个 test 都运行，默认是 function 的 scope
2. class：每个 class 的所有 test 只运行一次
3. module：每个 module 的所有 test 只运行一次
4. session：每个 session 只运行一次

setup，在测试函数或类之前执行，完成准备工作，例如数据库链接、测试数据、打开文件等

teardown，在测试函数或类之后执行，完成收尾工作，例如断开数据库链接、回收内存资源等

ps：也可以通过在 fixture 函数中通过 yield 实现 setup 和 teardown 功能
