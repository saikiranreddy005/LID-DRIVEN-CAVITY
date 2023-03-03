from IPython import get_ipython
ipython = get_ipython()
ipython.magic("pylab")
ipython.magic("load_ext autoreload")
ipython.magic("autoreload 2")