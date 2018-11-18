from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt
from collections import defaultdict
from IPython.display import clear_output


class plot_metrics():
    def __init__(self, columns=2, iter_num=None, mode=1, wait_num=1, figsize=None,
                 cell_size=(6, 4), valid_fmt="val_{}"):
        """
        Arguments:
            columns：int，default 2, The number of sub graphs that the width of metrics
                     visualiztion image to accommodate at most；
            iter_num：int, default None, Pre-specify the maximum value of x-axis in each
                      sub-picture to indicate the maximum number of batch or epoch training;
            mode：int，default 1, 1 means the x-axis name is 'batch', 0 means the x-axis name is 'epoch';
            wait_num：int, default 1, Indicates how many batches or epochs are drawn
                      each time a graph is drawn;
            figsize：tuple, default None，Represents the customize image size;
            cell_size：tuple, default (6, 4), Indicates the customize image size,
                       which is used when figsize=None;
            valid_fmt：str, default "val_{}",The string preceding the underscore is used to
                       instruction the training and validation is displayed together in the
                       same sub graph. The training indicator is not required to have a prefix.
                       The validation indicator prefix is 'val' in the "val_{}";
        """
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

    def draw(self, save_image=False, save_image_path=None, save_gif=False, save_gif_path=None):
        if self.polt_num%self.wait_num==0:
            clear_output(wait=True)
            figure = plt.figure(figsize=self.figsize)
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
            if save_image:
                if save_image_path is not None:
                    plt.savefig(save_image_path, bbox_inches='tight')
            if save_gif_path is not None:
                if not tf.gfile.Exists('./gif_temp_dirs'): tf.gfile.MakeDirs('./gif_temp_dirs')
                plt.savefig('./gif_temp_dirs/'+str(self.polt_num)+'.png', bbox_inches='tight')
                if save_gif:
                    imgs = []
                    image_path_list = sorted(tf.gfile.Glob('./gif_temp_dirs/*.png'), key = lambda i:int(i[16:-4]))
                    for k, image_path in enumerate(image_path_list):
                        if k==0:
                            img=Image.open(image_path)
                        else:
                            imgs.append(Image.open(image_path))
                    img.save(save_gif_path, save_all=True, append_images=imgs, duration=1)
                    tf.gfile.DeleteRecursively('./gif_temp_dirs')
            plt.show()
