# Functions to generate plots
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_matrix(correlation_matrix, title='Correlation Matrix'):
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title(title)
    plt.show()
