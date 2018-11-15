import tensorflow as tf
import matplotlib.pyplot as plt
from collections import defaultdict
from IPython.display import clear_output


def draw(metrics, logs, epoch, columns, iter_num, mode, wait_num, xlabel, figsize, cell_size, valid_fmt):
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
            plt.xlabel(xlabel[mode])
            plt.legend(loc='center right')
        plt.tight_layout()
        plt.show()

class PlotMetrics(tf.keras.callbacks.Callback):
    def __init__(self, metrics_name, columns=2, iter_num=None, mode=1, wait_num=1, figsize=None, cell_size=(6, 4),
                 valid_fmt="val_{}"):
        assert (mode==1)|(mode==0), 'please mode input 0 or 1'
        tf.logging.set_verbosity(tf.logging.ERROR)
        self.metrics_name = metrics_name
        self.columns = columns
        self.iter_num = iter_num
        self.mode = mode
        self.wait_num = wait_num
        self.figsize = figsize
        self.cell_size = cell_size
        self.valid_fmt = valid_fmt
        self.epoch_logs = defaultdict(list)
        self.batch_logs = defaultdict(list)
        self.xlabel = {0:'epoch', 1:'batch'}
        self.batch_num = 1
        
    def on_epoch_begin(self, epoch, logs=None):
        pass

    def on_epoch_end(self, epoch, logs=None):
        if self.mode==0:
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
                 iter_num=self.iter_num, mode=self.mode, wait_num=self.wait_num, xlabel=self.xlabel,
                 figsize=self.figsize, cell_size=self.cell_size, valid_fmt=self.valid_fmt)
    
    def on_batch_begin(self, batch, logs=None):
        pass

    def on_batch_end(self, batch, logs=None):
        if self.mode==1:
            loss = self.model.test_on_batch(self.validation_data[0], self.validation_data[1])
            [self.valid_fmt.split('_')[0]+'_'+i for i in self.metrics_names]
#             logs['']
            self.metrics = list(filter(lambda x: x not in ['batch', 'size'], logs))
            if self.figsize is None:
                self.figsize = (self.columns*self.cell_size[0], ((len(self.metrics)+1)//self.columns+1)*self.cell_size[1])
            for metric in self.metrics:
                self.batch_logs[metric] += [logs[metric]]
            self.batch_num += batch
            draw(metrics=self.metrics, logs=self.batch_logs, epoch=self.batch_num, columns=self.columns,
                 iter_num=self.iter_num, mode=self.mode, wait_num=self.wait_num, xlabel=self.xlabel,
                 figsize=self.figsize, cell_size=self.cell_size, valid_fmt=self.valid_fmt)

    def on_train_begin(self, logs=None):
        pass

    def on_train_end(self, logs=None):
        if self.mode==0:
            draw(metrics=self.metrics, logs=self.epoch_logs, epoch=self.wait_num, columns=self.columns,
                 iter_num=self.iter_num, mode=self.mode, wait_num=self.wait_num, xlabel=self.xlabel,
                 figsize=self.figsize, cell_size=self.cell_size, valid_fmt=self.valid_fmt)
        else:
            draw(metrics=self.metrics, logs=self.batch_logs, epoch=self.wait_num, columns=self.columns,
                 iter_num=self.iter_num, mode=self.mode, wait_num=self.wait_num, xlabel=self.xlabel,
                 figsize=self.figsize, cell_size=self.cell_size, valid_fmt=self.valid_fmt)
