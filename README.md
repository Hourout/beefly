# Beefly

![](https://github.com/Hourout/beefly/blob/master/image/1542382970(1).png)

![PyPI version](https://img.shields.io/pypi/pyversions/beefly.svg)
![Github license](https://img.shields.io/github/license/Hourout/beefly.svg)
[![PyPI](https://img.shields.io/pypi/v/beefly.svg)](https://pypi.python.org/pypi/beefly)
![PyPI format](https://img.shields.io/pypi/format/beefly.svg)

Beefly is efficient visualization training packages of Keras, enabling the live visualization of loss function and metrics during training process.

Beefly is process in the Jupyter Notebook, so we recommend Jupyter Notebook as Beefly's developing environment.

![](https://github.com/Hourout/beefly/blob/master/image/plot_metrics000.gif)

## [API Document](https://github.com/Hourout/beefly/blob/master/document/English_API.md)
## [API文档](https://github.com/Hourout/beefly/blob/master/document/Chinese_API.md)
## [中文介绍](https://github.com/Hourout/beefly/blob/master/document/Chinese.md)

## Installation

To install [this verson from PyPI](https://pypi.org/project/beefly/), type:

```
pip install beefly
```

To get the newest one from this repo (note that we are in the alpha stage, so there may be frequent updates), type:

```
pip install git+git://github.com/Hourout/beefly.git
```

## Feature
- Visualization of general machine learning training
  - Support customizing the name of loss function and metric 
  - Support customizing the name of validation set
  - Support displaying the result of training set and test set in the same plot
  - Support setting maximum training number of iterations
  - Support both batch way and epoch way to train
  - Support visual plotting
  - Support visual plotting in both batch way and epoch way periodically
  
- keras backend
  - Support customizing the name of loss function and metric in epoch way
  - Support customizing the name of validation set in epoch way
  - Support displaying the result of training set and test set in the same plot in epoch way
  - Support setting maximum training number of iterations in epoch way
  - Support visual plotting in epoch way
  - Support visual plotting in both batch way and epoch way periodically in epoch way
  - Support customizing the name of loss function and metric in batch way
  - Support customizing the name of validation set in batch way
  - Support displaying the result of training set and test set in the same plot in batch way
  - Support setting maximum training number of iterations in batch way
  - Support visual plotting in batch way
  - Support visual plotting in both batch way and epoch way periodically in batch way


## Example
- [beefly.plot_metrics()](https://github.com/Hourout/beefly/blob/master/example/plot_metrics.ipynb)
- [beefly.PlotMetricsOnBatch()](https://github.com/Hourout/beefly/blob/master/example/PlotMetricsOnBatch.ipynb)
- [beefly.PlotMetricsOnEpoch()](https://github.com/Hourout/beefly/blob/master/example/PlotMetricsOnEpoch.ipynb)
