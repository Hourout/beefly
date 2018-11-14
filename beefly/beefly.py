import warnings

import matplotlib
import matplotlib.pyplot as plt
from collections import defaultdict
from IPython.display import clear_output



class plot_metrics():
    def __init__(self, columns=2, iter_num=None, mode=1, wait_num=1, figsize=None, cell_size=(6, 4), valid_fmt="val_{}"):
        self.columns = columns
        self.iter_num = iter_num
        self.mode = mode
        self.wait_num = wait_num
        self.figsize = figsize
        self.cell_size = cell_size
        self.valid_fmt = valid_fmt
        self.logs = defaultdict(list)
        self.xlabel = {0:'epoch', 1:'batch'}
        self.polt_num = 0

    def update(self, log):
        self.metrics = list(filter(lambda x: self.valid_fmt.split('_')[0] not in x.lower(), log))
        if self.figsize is None:
            self.figsize = (self.columns*self.cell_size[0], ((len(self.metrics)+1)//self.columns+1)*self.cell_size[1])
        for metric in log:
            self.logs[metric] += [log[metric]]
        self.polt_num += 1

    def draw(self):
        if self.polt_num%self.wait_num==0:
            clear_output(wait=True)
            plt.figure(figsize=self.figsize)
            for metric_id, metric in enumerate(self.metrics):
                plt.subplot((len(self.metrics)+1)//self.columns+1, self.columns, metric_id+1)
                if self.iter_num is not None:
                    plt.xlim(1, self.iter_num)
                plt.plot(range(1, len(self.logs[metric])+1), self.logs[metric], label="train")
                if self.valid_fmt.format(metric) in self.logs:
                    plt.plot(range(1, len(self.logs[metric])+1), self.logs[self.valid_fmt.format(metric)], label=self.valid_fmt.split('_')[0])
                plt.title(metric)
                plt.xlabel(self.xlabel[self.mode])
                plt.legend(loc='center right')
            plt.tight_layout()
            plt.show()
