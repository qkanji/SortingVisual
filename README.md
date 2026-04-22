# Sorting Algorithm Visualizer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pygame](https://img.shields.io/badge/Pygame-4BB83B?style=for-the-badge)

A multi-threaded graphical visualizer comparing eight different sorting algorithms running concurrently.

[Insert Demo GIF / Screenshot Here]

## Features & Architecture

- **Concurrency:** Implements Python's `threading` module to execute eight sorting functions concurrently, mapping each algorithm's operational state to an individual UI quadrant.
- **Algorithm Implementations:** In-place modifications to Pygame surface arrays.
- **Operation Throttling:** Custom ticking logic enforces a uniform frame/operation delay (`time.sleep`) across all threads to expose algorithmic behavior that would normally execute in milliseconds.
- **Component-Based UI:** The `SortingVisualizer` class isolates instances to distinct coordinate quadrants on a primary screen surface for standardized performance monitoring.

## Supported Algorithms

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Radix Sort
- Counting Sort
- Heap Sort

## Tech Stack

- **Language:** Python 3.x
- **Core Library:** Pygame
- **Standard Libraries:** `threading`, `time`, `random`

## Use Case & Limitations

This tool acts as an educational diagnostic designed to provide visual insight into sorting techniques. Because the program enforces a 1-tick delay per operational step to make modifications visible to the human eye, algorithmic execution times do not strictly map to real-world Big-O time complexity. It visually demonstrates _how_ memory segments are reordered, rather than evaluating strict benchmarking environments.

## Local Setup

1. Verify Python 3.x is installed.
2. Install Pygame via pip:
   ```bash
   pip install pygame
   ```
3. Execute the root file:
   ```bash
   python main.py
   ```
4. A Pygame window will initialize. **Press Enter** to begin the visualization threads. Press `q` to quit the process.
