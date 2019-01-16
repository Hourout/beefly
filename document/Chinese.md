# BeeFly

## 介绍

Beefly是一个简洁高效的keras可视化训练库，能够在训练过程中动态可视化损失函数和评估指标的训练情况。

Beefly在Jupyter Notebook中运行，我们推荐且使用Jupyter Notebook作为beefly的开发环境。

| [API文档](https://github.com/Hourout/beefly/blob/master/document/Chinese_API.md) |


## 安装
支持pip安装[beefly](https://pypi.org/project/beefly/):
```
pip install beefly 
```
也可以用git安装最新的开发版本
```
pip install git+git://github.com/Hourout/beefly.git
```


## 功能
- 通用机器学习训练可视化
  - 支持自定义损失函数和度量指标名字
  - 支持同一指标训练集验证集在结果在一张图中显示
  - 支持设定训练最大迭代次数
  - 支持训练模式包括batch和epoch
  - 支持可视化绘图排版
  - 支持每间隔固定周期batch和epoch可视化绘图

- keras后端
  - 支持epoch模式下自定义损失函数和度量指标名字
  - 支持epoch模式下自定义验证集名字
  - 支持epoch模式下同一指标训练集验证集在结果在一张图中显示
  - 支持epoch模式下设定训练最大迭代次数
  - 支持epoch模式下可视化绘图排版
  - 支持epoch模式下每间隔固定周期epoch可视化绘图
  - 支持batch模式下自定义损失函数和度量指标名字
  - 支持batch模式下自定义验证集名字
  - 支持batch模式下同一指标训练集验证集在结果在一张图中显示
  - 支持batch模式下设定训练最大迭代次数
  - 支持batch模式下可视化绘图排版
  - 支持batch模式下每间隔固定周期epoch可视化绘图


## Example
- [beefly.plot_metrics()](/example/plot_metrics.ipynb)
- [beefly.PlotMetricsOnBatch()](/example/PlotMetricsOnBatch.ipynb)
- [beefly.PlotMetricsOnEpoch()](/example/PlotMetricsOnEpoch.ipynb)


## 版本

Beefly 目前还在快速开发中，未来将支持更多的功能，欢迎keras以及tensorflow社区的同学们一起加入开发。

## 更多阅读
- [Keras工程实践 | BeeFly，全新开源keras实时动态可视化训练库](https://mp.weixin.qq.com/s/_qNSg_CC4MLDmAMoE9UCcA)

## 博客
欢迎关注keras中文社区博客，扫码关注微信公众号

![](https://github.com/Hourout/beefly/blob/master/image/keras_wechat.jpg)
