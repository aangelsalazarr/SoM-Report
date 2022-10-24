import matplotlib.pyplot as plt
import seaborn as sns

def visual_maker(list):

    # setting up params for our visuals
    sns.set(font_scale=0.5)
    sns.set_style('dark')

    # will be used to name the title of each figure
    count = 0

    for item in list:
        fig, axes = plt.subplots(2, 3)
        fig.suptitle(list[count])

        sns.lineplot(ax=axes[0, 0], data=item, x='Date', y='Close',
                     linewidth=0.5, color='maroon')
        sns.lineplot(ax=axes[0, 1], data=item, x='Date', y='Volume',
                     linewidth=0.5, color='maroon')
        sns.lineplot(ax=axes[0, 2], data=item, x='Date', y='volumeDelta',
                     linewidth=0.5, color='maroon')
        sns.lineplot(ax=axes[1, 0], data=item, x='Date', y='high_low_delta',
                     linewidth=0.5, color='maroon')
        sns.lineplot(ax=axes[1, 1], data=item, x='Date', y='end_day_delta',
                     linewidth=0.5, color='maroon')
        sns.lineplot(ax=axes[1, 2], data=item, x='Date', y='Delta',
                     linewidth=0.5, color='maroon')

        # rotating period access
        for ax in fig.axes:
            ax.tick_params(labelrotation=90, axis='x')
            ax.set(xlabel=None)

        count += 1
