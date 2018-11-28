# Beefly API Document

```python
beefly.plot_metrics(columns=2, iter_num=None, mode=1, wait_num=1, figsize=None, cell_size=(6, 4), valid_fmt="val_{}")
```

参数：
- columns：int，默认为2，指标可视化图像的宽最多容纳的子图数量；
- iter_num：int，默认为None，预先指定每个子图的x轴最大值，用来表示训练最大的batch或epoch数；
- mode：int，默认为1，1表示x轴名字为'batch'，0表示x轴名字为'epoch'；
- wait_num：int，默认为1，表示每经过多少个batch或epoch画一次图；
- figsize：tuple，默认为None，表示自定义图像大小；
- cell_size：tuple，默认为(6, 4)，表示自定义图像大小，当figsize=None时该参数起作用；
- valid_fmt：str，默认为"val_{}"，下划线前面的字符串用来实现训练验证相同指标在同一子图中共同显示，要求训练指标不含有前缀，验证指标前缀为"val_{}"中的'val'；

方法
```python
beefly.plot_metrics.draw(save_image=False, save_image_path=None, save_gif=False, save_gif_path=None)
```

参数：
- save_image：bool，默认False，是否保存训练指标图片；
- save_image_path：str，默认None，当save_image=True时，图片保存的路径地址；
- save_gif：bool，默认False，是否保存训练指标gif图片；
- save_gif_path：str，默认None，当save_gif=True时，gif图片保存的路径地址；

```python
beefly.PlotMetricsOnBatch(metrics_name, columns=2, iter_num=None, wait_num=1, figsize=None, cell_size=(6, 4), valid_fmt="val_{}", eval_batch_num=None)
```

参数：
- metrics_name：list，自定义的评估指标名字列表，顺序按照损失函数、度量函数依次创建
- columns：int，默认为2，指标可视化图像的宽最多容纳的子图数量；
- iter_num：int，默认为None，预先指定每个子图的x轴最大值，用来表示训练最大的batch数；
- wait_num：int，默认为1，表示每经过多少个batch画一次图；
- figsize：tuple，默认为None，表示自定义图像大小；
- cell_size：tuple，默认为(6, 4)，表示自定义图像大小，当figsize=None时该参数起作用；
- valid_fmt：str，默认为"val_{}"，下划线前面的字符串用来实现验证集指标命名；
- eval_batch_num：int，默认为None，表示每经过多少个batch对验证集进行一次评估；


```python
beefly.PlotMetricsOnEpoch(metrics_name, columns=2, iter_num=None, wait_num=1, figsize=None, cell_size=(6, 4), valid_fmt="val_{}")
```

参数：
- metrics_name：list，自定义的评估指标名字列表，顺序按照损失函数、度量函数依次创建
- columns：int，默认为2，指标可视化图像的宽最多容纳的子图数量；
- iter_num：int，默认为None，预先指定每个子图的x轴最大值，用来表示训练最大的batch数；
- wait_num：int，默认为1，表示每经过多少个batch画一次图；
- figsize：tuple，默认为None，表示自定义图像大小；
- cell_size：tuple，默认为(6, 4)，表示自定义图像大小，当figsize=None时该参数起作用；
- valid_fmt：str，默认为"val_{}"，下划线前面的字符串用来实现训练验证相同指标在同一子图中共同显示，要求训练指标不含有前缀，验证指标前缀为"val_{}"中的'val'；
