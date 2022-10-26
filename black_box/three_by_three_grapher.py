from itertools import permutations, chain
import seaborn as sns
import matplotlib.pyplot as plt

def visualizer(list, tickerlist, y_axis, fig_title):

    # setting up the parameters for our data_visuals
    sns.set(font_scale=0.5)
    fig, axes = plt.subplots(3, 3)
    fig.suptitle(str(fig_title))

    # can think of set lists of #'s we want to find permutations for
    gridnums = [[0, 1, 2], [0, 1, 2]]

    # here we calculate all permutations of gridnums
    gridnums_p = sorted(i[:2] for i in set(permutations(chain.from_iterable(gridnums))))

    # purpose is to remove any redundant arrays within gridnums_p
    gridlocs = [i for n, i in enumerate(gridnums_p) if i not in gridnums_p[:n]]

    # used for the purpose is iterating through elements in our lists
    count = 0

    for item in list:
        sns.lineplot(ax=axes[gridlocs[count]],
                     data=item, x='Date', y=str(y_axis),
                     linewidth=0.7, ci=None).set(title=tickerlist[count])

        count += 1

    # some stylistic changes
    for ax in fig.axes:
        ax.tick_params(labelrotation=90, axis='x')
        ax.set(xlabel=None)