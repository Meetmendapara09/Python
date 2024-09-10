# matplotlib.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import seaborn as sns

def create_sample_data():
    """Create a sample dataset."""
    data = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [2, 3, 5, 7, 11],
        'y_err': [0.5, 0.3, 0.4, 0.6, 0.5]  # Error data for error bars
    })
    return data

def line_plot(data):
    """Create and display a line plot."""
    plt.figure(figsize=(8, 6))
    plt.plot(data['x'], data['y'], marker='o', linestyle='-', color='b', label='Line', markersize=10, linewidth=2)
    plt.title('Line Plot', fontsize=16)
    plt.xlabel('x-axis', fontsize=14)
    plt.ylabel('y-axis', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

def scatter_plot(data):
    """Create and display a scatter plot."""
    plt.figure(figsize=(8, 6))
    plt.scatter(data['x'], data['y'], color='r', label='Scatter', s=100, alpha=0.7, edgecolor='k')
    plt.title('Scatter Plot', fontsize=16)
    plt.xlabel('x-axis', fontsize=14)
    plt.ylabel('y-axis', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

def bar_chart(data):
    """Create and display a bar chart."""
    plt.figure(figsize=(8, 6))
    plt.bar(data['x'], data['y'], color='g', label='Bar Chart', edgecolor='black')
    plt.title('Bar Chart', fontsize=16)
    plt.xlabel('x-axis', fontsize=14)
    plt.ylabel('y-axis', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

def histogram():
    """Create and display a histogram."""
    data = np.random.randn(1000)  # Random data
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=30, color='c', edgecolor='black', label='Histogram')
    plt.title('Histogram', fontsize=16)
    plt.xlabel('Value', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

def pie_chart():
    """Create and display a pie chart."""
    sizes = [20, 30, 10, 40]
    labels = ['A', 'B', 'C', 'D']
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Pie Chart', fontsize=16)
    plt.show()

def contour_plot():
    """Create and display a contour plot."""
    X, Y = np.meshgrid(np.arange(-5, 5, 0.1), np.arange(-5, 5, 0.1))
    Z = np.sin(np.sqrt(X**2 + Y**2))
    plt.figure(figsize=(8, 6))
    contour = plt.contour(X, Y, Z, cmap='viridis')
    plt.title('Contour Plot', fontsize=16)
    plt.colorbar(contour)
    plt.show()

def heatmap():
    """Create and display a heatmap."""
    data = np.random.rand(10, 10)
    plt.figure(figsize=(8, 6))
    sns.heatmap(data, cmap='coolwarm', annot=True, fmt='.1f', linewidths=0.5)
    plt.title('Heatmap', fontsize=16)
    plt.show()

def violin_plot():
    """Create and display a violin plot."""
    data = [np.random.normal(size=100) for _ in range(4)]
    plt.figure(figsize=(8, 6))
    sns.violinplot(data=data, palette='muted')
    plt.title('Violin Plot', fontsize=16)
    plt.show()

def subplots_example(data):
    """Create and display multiple plots in a single figure."""
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    axs[0, 0].plot(data['x'], data['y'], 'b-o')
    axs[0, 0].set_title('Line Plot')

    axs[0, 1].scatter(data['x'], data['y'], color='r')
    axs[0, 1].set_title('Scatter Plot')

    axs[1, 0].bar(data['x'], data['y'], color='g')
    axs[1, 0].set_title('Bar Chart')

    axs[1, 1].hist(np.random.randn(1000), bins=30, color='c', edgecolor='black')
    axs[1, 1].set_title('Histogram')

    for ax in axs.flat:
        ax.label_outer()

    plt.tight_layout()
    plt.show()

def animated_plot():
    """Create and display an animated plot."""
    fig, ax = plt.subplots(figsize=(8, 6))
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'r', animated=True)

    def init():
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-1, 1)
        return ln,

    def update(frame):
        xdata.append(frame)
        ydata.append(np.sin(frame))
        ln.set_data(xdata, ydata)
        return ln,

    ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 128),
                        init_func=init, blit=True)
    plt.title('Animated Plot', fontsize=16)
    plt.show()

def three_d_surface():
    """Create and display a 3D surface plot."""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    X = np.linspace(-5, 5, 100)
    Y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(X, Y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title('3D Surface Plot', fontsize=16)
    plt.show()

def three_d_scatter():
    """Create and display a 3D scatter plot."""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    x = np.random.rand(100) * 10
    y = np.random.rand(100) * 10
    z = np.random.rand(100) * 10

    ax.scatter(x, y, z, c='r', marker='o')
    ax.set_title('3D Scatter Plot', fontsize=16)
    plt.show()

def log_scale_plot():
    """Create and display a plot with logarithmic scales."""
    x = np.logspace(0.1, 2, 100)
    y = np.exp(x / 10)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'g-')
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Logarithmic Scale Plot', fontsize=16)
    plt.xlabel('Log x', fontsize=14)
    plt.ylabel('Log y', fontsize=14)
    plt.grid(True, which="both", ls="--")
    plt.show()

def error_bars(data):
    """Create and display a plot with error bars."""
    plt.figure(figsize=(8, 6))
    plt.errorbar(data['x'], data['y'], yerr=data['y_err'], fmt='o', color='b', ecolor='r', capsize=5, capthick=2)
    plt.title('Error Bars Plot', fontsize=16)
    plt.xlabel('x-axis', fontsize=14)
    plt.ylabel('y-axis', fontsize=14)
    plt.grid(True)
    plt.show()

def annotations_plot(data):
    """Create and display a plot with annotations."""
    plt.figure(figsize=(8, 6))
    plt.plot(data['x'], data['y'], marker='o', linestyle='-', color='b', label='Data Line')
    for i, txt in enumerate(data['y']):
        plt.annotate(txt, (data['x'][i], data['y'][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=12, color='black')
    plt.title('Plot with Annotations', fontsize=16)
    plt.xlabel('x-axis', fontsize=14)
    plt.ylabel('y-axis', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

def save_plot():
    """Create and save a plot to a file."""
    plt.figure(figsize=(8, 6))
    plt.plot([1, 2, 3], [4, 5, 6], 'b-')
    plt.title('Save Plot Example', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.grid(True)
    plt.savefig('saved_plot.png')
    print("Plot saved as 'saved_plot.png'")

def main():
    data = create_sample_data()
    line_plot(data)
    scatter_plot(data)
    bar_chart(data)
    histogram()
    pie_chart()
    contour_plot()
    heatmap()
    violin_plot()
    subplots_example(data)
    animated_plot()
    three_d_surface()
    three_d_scatter()
    log_scale_plot()
    error_bars(data)
    annotations_plot(data)
    save_plot()

if __name__ == "__main__":
    main()

