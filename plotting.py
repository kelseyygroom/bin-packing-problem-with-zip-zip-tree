import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_best_fit(data_frames):
    for algorithm in ['best_fit', 'best_fit_decreasing']:
        df = data_frames[algorithm]
        
        # Plot each permutation type for the algorithm
        log_sizes = np.log2(df['size'])
        log_waste = np.log2(df['waste'])
        
        # Fit a line to determine the asymptotic slope
        m, b = np.polyfit(log_sizes, log_waste, 1)
        
        # Plot the runtime with label including slope and permutation type
        
        plt.loglog(df['size'], df['waste'], marker='o', 
                    label=f'{algorithm} ~ {m:.2f} logN + {b:.2f}')
    
    plt.xscale('log', base=2)
    plt.yscale('log', base=2)
    plt.xlabel('log N')
    plt.ylabel('Log T(N) (waste)')
    plt.title('Best Fit and Best Fit Decreasing Waste Comparison')
    plt.legend()
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.show()

def plot_next_fit(data_frames): 
    for algorithm in ['next_fit']:
        df = data_frames['next_fit']
        
        # Plot each permutation type for the algorithm
        log_sizes = np.log2(df['size'])
        log_waste = np.log2(df['waste'])
        
        # Fit a line to determine the asymptotic slope
        m, b = np.polyfit(log_sizes, log_waste, 1)
        
        # Plot the runtime with label including slope and permutation type
        
        plt.loglog(df['size'], df['waste'], marker='o', 
                    label=f'next_fit ~ {m:.2f} logN + {b:.2f}')
    
    plt.xscale('log', base=2)
    plt.yscale('log', base=2)
    plt.xlabel('log N')
    plt.ylabel('Log T(N) (waste)')
    plt.title('Next Fit Waste Comparison')
    plt.legend()
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.show()

def plot_first_fit(data_frames):
    for algorithm in ['first_fit', 'first_fit_decreasing']:
        df = data_frames[algorithm]
        
        # Plot each permutation type for the algorithm
        log_sizes = np.log2(df['size'])
        log_waste = np.log2(df['waste'])
        
        # Fit a line to determine the asymptotic slope
        m, b = np.polyfit(log_sizes, log_waste, 1)
        
        # Plot the runtime with label including slope and permutation type
        
        plt.loglog(df['size'], df['waste'], marker='o', 
                    label=f'{algorithm} ~ {m:.2f} logN + {b:.2f}')
    
    plt.xscale('log', base=2)
    plt.yscale('log', base=2)
    plt.xlabel('log N')
    plt.ylabel('Log T(N) (waste)')
    plt.title('First Fit and First Fit Decreasing Waste Comparison')
    plt.legend()
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.show()


if __name__ == "__main__":
    # call the plotting function for each sorting algorithm.
    file_paths = {
    'best_fit': "best_fit.csv",
    'best_fit_decreasing': "best_fit_decreasing.csv",
    'next_fit': "next_fit.csv",
    'first_fit': "first_fit.csv",
    'first_fit_decreasing': "first_fit_decreasing.csv"
}
    data_frames = {}
    for algorithm, file_path in file_paths.items():
        data_frames[algorithm] = pd.read_csv(file_path, sep=',')
    plot_best_fit(data_frames)
    plot_next_fit(data_frames)
    plot_first_fit(data_frames)