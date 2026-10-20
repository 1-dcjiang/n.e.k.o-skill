---
name: code-sandbox-guide
description: 教 YUI 如何正确使用代码沙箱（code_sandbox 插件）执行 Python 代码：适用场景、代码写法、超时设置、常见被拦截原因与替代方案。当用户提出计算、数据处理、算法验证、逻辑推理等需要运行代码的需求时，参考本指南决定是否调用 code_sandbox 及如何构造代码。
---

# 代码沙箱使用指南

本技能说明如何安全、高效地使用 **code_sandbox** 插件在受限沙箱中执行 Python 代码。

## 何时使用

适合的请求：

- 「算一下 1+1 到 100 的和」「这组数据的平均值/方差」
- 「跑一下这段代码看看结果」「验证这个算法/公式对不对」
- 「帮我处理这段数据（排序、去重、统计）」
- 「模拟一下这个随机过程」

不适合的请求（不要调用沙箱）：

- 需要联网（访问网页/API）、读写本地文件、执行系统命令
- 需要安装第三方库（沙箱只有标准库）

## 调用方式

沙箱提供两个入口（等效）：

- 工具：`run_code(code, timeout)`
- 入口：`code_sandbox.run`，参数 `code` 必填，`timeout` 可选

## 代码写法

- 用 `print()` 输出结果，YUI 会拿到 stdout
- 纯计算优先：`math` / `random` / `json` / `statistics` / `collections` / `datetime` / `re` / `itertools` / `functools` / `decimal` / `fractions` / `heapq` / `bisect` / `string` / `base64` / `hashlib` / `typing` 等标准库可用
- 结果会以文本返回并截断到上限（防止刷屏），大输出请只打印摘要

## 超时

- 默认 10 秒，最大 60 秒；超时会被强制终止（kill 进程树）
- 循环/递归类代码务必预估耗时并设置合理 timeout

## 会被拦截的操作（一律禁止）

- 系统命令：`os.system`、`subprocess.run`、`os.popen`
- 网络访问：`socket`、`requests`、`urllib`
- 文件读写：`open`、`Path.write_text`、`tempfile`、`os.remove`
- 动态执行与逃逸：`exec`、`eval`、`compile`、`getattr`、`__import__`、`__class__`/`__subclasses__` 等双下划线逃逸属性

被拦截时返回「安全拦截 + 原因」，请改用纯计算代码，不要尝试绕过。

## 常见用例

```python
# 求和
print(sum(range(1, 101)))

# 统计
import statistics
data = [1, 2, 3, 4, 5]
print(statistics.mean(data), statistics.stdev(data))

# 算法验证
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(fib(30))
```

## 回复纪律

- 直接给出运行结果或拦截原因，不加「搞定啦」之类话术
- 不编造输出：只有沙箱实际返回的 stdout 才算结果
