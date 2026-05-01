# 参考

- [wren.io](https://wren.io/)

# Wren Cheatsheet

## 快速启动

### 运行命令
```console
$ wren main.wren
```
### 程序入口
```wren
没有固定入口函数，整个文件自上而下执行
```
### 注释语法
```wren
// 单行注释
/*
 * 多行
 * 注释
 */
```

## 基础语法

### 数据类型
Bool,Class,Fiber,Fn,List,Map,Null,Num,String
### 变量
```wren
// Bool
var a = true
var b = false

// Class
class Foo { /* methods */ }
var a = Foo.new()

// Fiber
var a = Fiber.new { /* statements */ }
var b = Fiber.new {|param| /* statements */ }
var c = Fiber.new {|param1, param2| /* statements */ }

// Fn
var a = Fn.new { /* statements */ }
var b = Fn.new {|param| /* statements */ }
var c = Fn.new {|param1, param2| /* statements */ }

// List
var a = []
var b = [1]
var c = [1, 2]

// Map
var a = {}
var b = { "k": "v" }
var c = { "k1": "v1", "k2": "v2" }

// Null
var a = null

// Num
var a = 1
var b = 1.3
var c = 3.14e+2   // 3.14x100
var d = 3.14e-2   // 3.14/100
var e = 0x1234

// String
var a = "hello"
var b = """hello\nworld""" // 原始字符串，不会转义
var c = "\x48"        // 0x48 (1)
var d = "\u0041"      // 0x0041 (2)
var e = "\U0001F64A"  // 0x0001f64a (4)
```
### 常量
无
### 运算符
- 算术: +,-,*,/,%
- 逻辑: <<,>>,&,|,^,&&,||,~,!
- 比较: ==,!=,<,<=,>,>=
- 其他: ?:,..,...,is

## 流程控制

### 分支判断
```wren
var n = 100
if (n < 50) {
  ...
}

if (n < 50) {
  ...
} else {
  ...
}

if (n < 50) {
  ...
} else if (n < 70) {
  ...
} else {
  ...
}
```
### 循环结构
```wren
var n = 0
while (n < 100) {
  ...
}

for (i in 1..4) {
  // i包括4
  ...
}
for (i in 1...4) {
  // i不包括4
  ...
}
for (i in [1, 2, 3, 4]) {
  ...
}
```
### 跳转语句
```wren
for (i in 1..5) {
  if (i == 4) break
  System.print(i)
}

for (i in 1..5) {
  if (i == 4) continue
  System.print(i)
}
```

## 数据结构

### 数组/列表
- 增删查改
```wren
var list = [1, 2, 3, "true", true]
// 增
list.add(10)
list.insert(0, "head")
list = list + ["a", "b"]
// 删
list.remove("true")
list.removeAt(2)
list.clear()
// 查
var length = list.count
var slice = list[1..-1]
// 改
list[0] = "first"
```
- 遍历方式
```wren
var list = [1, 2, 3]
for (i in list) {
  ...
}
```
### 字典/映射
- 增删查改
```wren
var map = {}
// 增
map["k"] = "v"
// 删
map.remove("k")
map.clear()
// 查
var value = map["k"]
var exist = map.containsKey("k")
var length = map.count
// 改
map["k"] = "new_v"
```
- 遍历方式
```wren
var birds = {
  "Arizona": "Cactus wren",
  "Hawaii": "Nēnē",
  "Ohio": "Northern Cardinal"
}
// 遍历条目
for (bird in birds) {
  var key = bird.key
  var val = bird.value
  ...
}
// 遍历键
for (state in birds.keys) {
  var value = birds[state]
  ...
}
```

## 函数

- 函数定义 & 调用
```wren
var f = Fn.new { return "hello" }
f.call()
var f1 = Fn.new {|param| return param}
f1.call("h")
var f2 = Fn.new {|param1, param2| return param1 + param2}
f2.call("a", "b")
```

## 字符串

- 增删查改
```wren
var s = " abc "
// 增
var new_s = s + "hello"
var new_s = s * 10
var new_s = String.fromByte(100)
// 删
var new_s = s.replace(" ", "") // 删掉所有空格
// 查
var ch = s[2]
var index = s.indexOf("a")
var index = s.indexOf("a", 2) // 从索引2开始查找
var exist = s.contains("abc")
var length = s.count
var substring = s[1..-1]
var byte = s.bytes[1]
var nwe_s = s.trim()
var nwe_s = s.trimStart()
var nwe_s = s.trimEnd()
var check = (s == new_s)
var check = s.endsWith("suffix")
var check = s.startsWith("prefix")
// 改
var new_s = s.replace("a", "b") // 将所有a替换成b
var list = s.split(" ") // 按照空格分割
```
- 遍历方式
```wren
for (ch in string) {
  ...
}
```
- 字符串插值
```wren
var msg = "world"
System.print("hello, %(msg)")
```

## 输入输出

### 终端 IO
- 输出
```wren
System.print("hello, world") // 带有换行
System.write("hello, world") // 不带有换行
```
- 输入
无
### 文件 IO
无

## 错误处理
```wren
Fiber.abort("bad thing")

var f = Fiber.new { ... } // 和创建函数一样
f.try()
System.print(f.error)

var f1 = Fiber.new {|param| ... } // 和创建函数一样
f.try(param)
System.print(f.error)

// 只支持一个参数
```

## 面向对象

### 类与实例
```wren
class Foo {
  // 构造函数
  construct new() {
    ...
  }
  construct new(param) {
    ...
  }
}
var foo = Foo.new()
var foo1 = Foo.new(param)
```
### 属性
```wren
class Foo {
  // 成员属性默认私有，必须以_开头
  // 静态成员属性必须以__开头
  construct new(param1, param2) {
    _m1 = param1
    _m2 = param2
    __m3 = 10
  }
}
```
### 方法
```wren
class Foo {
  // getter
  name { _name }
  // 静态getter
  static name { __name }
  // setter
  name=(value) { _name = value }
  // 静态setter
  static name=(value) { __name = value }
  // 普通方法
  method(param1, param2) { ... }
  // 静态方法
  static method1(param1, param2) { ... }
}
```

## 常用代码片段
