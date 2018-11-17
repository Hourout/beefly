import tensorflow as tf
import matplotlib.pyplot as plt
from collections import defaultdict
from IPython.display import clear_output


def draw(metrics, logs, epoch, columns, iter_num, wait_num, figsize, cell_size, valid_fmt):
    if epoch%wait_num==0:
        clear_output(wait=True)
        plt.figure(figsize=figsize)
        for metric_id, metric in enumerate(metrics):
            plt.subplot((len(metrics)+1)//columns+1, columns, metric_id+1)
            if iter_num is not None:
                plt.xlim(1, iter_num)
            plt.plot(range(1, len(logs[metric])+1), logs[metric], label="train")
            if valid_fmt.format(metric) in logs:
                plt.plot(range(1, len(logs[metric])+1), logs[valid_fmt.format(metric)], label=valid_fmt.split('_')[0])
            plt.title(metric)
            plt.xlabel('epoch')
            plt.legend(loc='center right')
        plt.tight_layout()
        plt.show()

class PlotMetricsOnEpoch(tf.keras.callbacks.Callback):
    def __init__(self, metrics_name, columns=2, iter_num=None, wait_num=1, figsize=None,
                 cell_size=(6, 4), valid_fmt="val_{}"):
        """
        Arguments:
            metrics_name：list, Customized evaluation indicator name list,
                          sequentially created according to loss function and measurement function;
            columns：int, default 2，The number of sub graphs that the width of metrics
                     visualiztion image to accommodate at most;
            iter_num：int, default None，Pre-specify the maximum value of x-axis in each
                      sub-picture to indicate the maximum number of epoch training;
            wait_num：int, default 1, Indicates how many epoch are drawn each time a graph is drawn;
            figsize：tuple, default None, Represents the customize image size;
            cell_size：tuple, default (6, 4), Indicates the customize image size, which is used when figsize=None;
            valid_fmt：str, default "val_{}", The string preceding the underscore is used to
                       implement the validation set indicator naming;
        """
        tf.logging.set_verbosity(tf.logging.ERROR)
        self.metrics_name = metrics_name
        self.columns = columns
        self.iter_num = iter_num
        self.wait_num = wait_num
        self.figsize = figsize
        self.cell_size = cell_size
        self.valid_fmt = valid_fmt
        self.epoch_logs = defaultdict(list)

    def on_epoch_end(self, epoch, logs=None):
        if len(self.validation_data)==0:
            old_all_name = self.model.metrics_names
            new_all_name = self.metrics_name
        else:
            old_all_name = self.model.metrics_names+['val_'+i for i in self.model.metrics_names]
            new_all_name = self.metrics_name+[self.valid_fmt.split('_')[0]+'_'+i for i in self.metrics_name]
        for old_name, new_name in zip(old_all_name, new_all_name):
            logs[new_name] = logs.pop(old_name)
        self.metrics = list(filter(lambda x: self.valid_fmt.split('_')[0] not in x.lower(), logs))
        if self.figsize is None:
            self.figsize = (self.columns*self.cell_size[0], ((len(self.metrics)+1)//self.columns+1)*self.cell_size[1])
        for metric in logs:
            self.epoch_logs[metric] += [logs[metric]]
        draw(metrics=self.metrics, logs=self.epoch_logs, epoch=epoch, columns=self.columns,
             iter_num=self.iter_num, wait_num=self.wait_num,
             figsize=self.figsize, cell_size=self.cell_size, valid_fmt=self.valid_fmt)

    def on_train_end(self, logs=None):
        draw(metrics=self.metrics, logs=self.epoch_logs, epoch=self.wait_num, columns=self.columns,
             iter_num=self.iter_num, wait_num=self.wait_num,
             figsize=self.figsize, cell_size=self.cell_size, valid_fmt=self.valid_fmt)
