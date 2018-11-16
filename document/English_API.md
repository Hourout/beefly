# Beefly API Document

```python
beefly.plot_metrics(columns=2, iter_num=None, mode=1, wait_num=1, figsize=None, cell_size=(6, 4), valid_fmt="val_{}")
```

# Parameter：
- columns：int，default 2，The number of sub graphs that the width of metrics visualiztion image to accommodate at most；
- iter_num：int，default None，Pre-specify the maximum value of x-axis in each sub-picture to indicate the maximum number of batch or epoch training;
- mode：int，default 1，1 means the x-axis name is 'batch', 0 means the x-axis name is 'epoch';
- wait_num：int，default 1，Indicates how many batches or epochs are drawn each time a graph is drawn;
- figsize：tuple，default None，Represents the customize image size;
- cell_size：tuple，default (6, 4)，Indicates the customize image size, which is used when figsize=None;
- valid_fmt：str，default "val_{}",The string preceding the underscore is used to instruction the training and validation is displayed together in the same sub graph. The training indicator is not required to have a prefix. The validation indicator prefix is ​​'val' in the "val_{}";

```python
beefly.PlotMetricsOnBatch(metrics_name, columns=2, iter_num=None, wait_num=1, figsize=None, cell_size=(6, 4), valid_fmt="val_{}", eval_batch_num=None)
```

# Parameter：
- metrics_name：list，Customized evaluation indicator name list, sequentially created according to loss function and measurement function;
- columns：int，default 2，The number of sub graphs that the width of metrics visualiztion image to accommodate at most;
- iter_num：int，default None，Pre-specify the maximum value of x-axis in each sub-picture to indicate the maximum number of batch training;
- wait_num：int，default 1，Indicates how many batches are drawn each time a graph is drawn;
- figsize：tuple，default None，Represents the customize image size;
- cell_size：tuple，default (6, 4)，Indicates the customize image size, which is used when figsize=None;
- valid_fmt：str，default "val_{}"，The string preceding the underscore is used to implement the validation set indicator naming;
- eval_batch_num：int，default None，Indicates how many batches are evaluated for each validation set;


```python
beefly.PlotMetricsOnEpoch(metrics_name, columns=2, iter_num=None, wait_num=1, figsize=None, cell_size=(6, 4), valid_fmt="val_{}")
```

# Parameter：
- metrics_name：list，Customized evaluation indicator name list, sequentially created according to loss function and measurement function;
- columns：int，default 2，The number of sub graphs that the width of metrics visualiztion image to accommodate at most;
- iter_num：int，default None，Pre-specify the maximum value of x-axis in each sub-picture to indicate the maximum number of epoch training;
- wait_num：int，default 1，Indicates how many epoch are drawn each time a graph is drawn;
- figsize：tuple，default None，Represents the customize image size;
- cell_size：tuple，default (6, 4)，Indicates the customize image size, which is used when figsize=None;
- valid_fmt：str，default "val_{}"，The string preceding the underscore is used to implement the validation set indicator naming;
