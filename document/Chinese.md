# BeeFly

Beefly是一个简洁高效的keras可视化训练库，能够在训练过程中动态可视化损失函数和评估指标的训练情况。

Beefly在Jupyter Notebook中运行，我们推荐且使用Jupyter Notebook作为beefly的开发环境。

# 安装
你可以通过pypi进行安装：
```Bash
pip install beefly 
```

# 功能
- 通用机器学习训练可视化
  - 支持自定义损失函数和度量指标名字 [example](/example/example1.py)
  - 支持同一指标训练集验证集在结果在一张图中显示 [example](/example/example2.py)
  - 支持设定训练最大迭代次数 [example](/example/example3.py)
  - 支持训练模式包括batch和epoch [example](/example/example4.py)
  - 支持可视化绘图排版 [example](/example/example5.py)
  - 支持每间隔固定周期batch和epoch可视化绘图 [example](/example/example6.py)

- keras后端
  - 支持epoch模式下自定义损失函数和度量指标名字 [example](/example/example7.py)
  - 支持epoch模式下自定义验证集名字 [example](/example/example8.py)
  - 支持epoch模式下同一指标训练集验证集在结果在一张图中显示 [example](/example/example8.py)
  - 支持epoch模式下设定训练最大迭代次数 [example](/example/example9.py)
  - 支持epoch模式下可视化绘图排版
  - 支持epoch模式下每间隔固定周期epoch可视化绘图
  - 支持batch模式下自定义损失函数和度量指标名字
  - 支持batch模式下自定义验证集名字
  - 支持batch模式下同一指标训练集验证集在结果在一张图中显示
  - 支持batch模式下设定训练最大迭代次数
  - 支持batch模式下可视化绘图排版
  - 支持batch模式下每间隔固定周期epoch可视化绘图
