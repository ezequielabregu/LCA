import numpy as np
import matplotlib.pyplot as plt

def rule30(cells):
    """Applies Rule 30 to the input cells."""
    new_cells = np.zeros_like(cells)
    extended_cells = np.concatenate(([cells[-1]], cells, [cells[0]]))  # Apply periodic boundary conditions
    for i in range(1, len(extended_cells) - 1):
        neighborhood = extended_cells[i-1:i+2]
        if np.array_equal(neighborhood, [1, 1, 1]) or np.array_equal(neighborhood, [1, 1, 0]) or \
           np.array_equal(neighborhood, [1, 0, 1]) or np.array_equal(neighborhood, [0, 0, 0]):
            new_cells[i-1] = 0
        else:
            new_cells[i-1] = 1
    return new_cells

def main():
    # Initialize the cells
    cells = np.zeros(100)
    cells[50] = 1  # Start with one cell in the middle

    # Apply Rule 30 for 100 steps
    history = [cells]
    for i in range(100):
        cells = rule30(cells)
        history.append(cells)

    # Display the history as an image
    plt.imshow(history, cmap='binary')
    plt.show()

if __name__ == "__main__":
    main()