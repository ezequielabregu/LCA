import numpy as np
import matplotlib.pyplot as plt

def rule30(cells):
    """Applies Rule 30 to the input cells."""
    new_cells = np.zeros_like(cells)
    for i in range(1, len(cells) - 1):
        if cells[i-1] == cells[i+1]:
            new_cells[i] = 0
        else:
            new_cells[i] = 1
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