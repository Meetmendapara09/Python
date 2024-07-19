import numpy as np

# Creating NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("Array 1:")
print(arr1)
print("Array 2:")
print(arr2)

# Basic array attributes
print("Shape of arr1:", arr1.shape)
print("Shape of arr2:", arr2.shape)
print("Data type of arr1:", arr1.dtype)
print("Data type of arr2:", arr2.dtype)
print("Number of dimensions in arr1:", arr1.ndim)
print("Number of dimensions in arr2:", arr2.ndim)
print("Number of elements in arr1:", arr1.size)
print("Number of elements in arr2:", arr2.size)

# Reshaping arrays
arr3 = np.arange(12).reshape(3, 4)
print("\nArray 3 (reshaped from arange):")
print(arr3)

# Array indexing and slicing
print("\nElement at index (1, 2) in arr2:", arr2[1, 2])
print("First row of arr2:", arr2[0, :])
print("First column of arr2:", arr2[:, 0])
print("Last two columns of arr2:")
print(arr2[:, -2:])

# Array operations
print("\nSum of arr1 elements:", np.sum(arr1))
print("Mean of arr2 elements:", np.mean(arr2))
print("Max value in arr1:", np.max(arr1))
print("Min value in arr2:", np.min(arr2))

# Array arithmetic operations
arr4 = np.array([[1, 2], [3, 4]])
arr5 = np.array([[5, 6], [7, 8]])

print("\nElement-wise addition:")
print(arr4 + arr5)

print("Element-wise multiplication:")
print(arr4 * arr5)

# Matrix operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("\nMatrix multiplication:")
print(np.matmul(matrix1, matrix2))

# Random number generation
rand_array = np.random.rand(3, 3)
print("\nRandom 3x3 array:")
print(rand_array)

# Stacking arrays
stacked_array = np.hstack((matrix1, matrix2))
print("\nHorizontally stacked matrix1 and matrix2:")
print(stacked_array)

# Saving and loading arrays
np.save('saved_array.npy', arr1)
loaded_array = np.load('saved_array.npy')
print("\nLoaded array from file:")
print(loaded_array)

# Additional operations

# Broadcasting
print("\nBroadcasting example:")
a = np.array([1, 2, 3])
b = 2
print(a + b)

# Universal functions (ufunc)
print("\nUniversal functions (ufunc) example:")
print(np.exp(arr1))  # Exponential function
print(np.sqrt(arr1))  # Square root function

# Statistical functions
print("\nStatistical functions example:")
print("Standard deviation of arr2:", np.std(arr2))
print("Variance of arr2:", np.var(arr2))

# Concatenation
print("\nConcatenation example:")
arr6 = np.array([[7, 8, 9]])
print(np.concatenate((arr2, arr6), axis=0))  # Concatenate along rows

# Transpose
print("\nTranspose example:")
print(arr2.T)  # Transpose of arr2

# Indexing with boolean arrays
print("\nIndexing with boolean arrays example:")
bool_arr = arr1 > 3
print("Boolean array:", bool_arr)
print("Elements > 3 in arr1:", arr1[bool_arr])

# Reshaping and resizing
print("\nReshaping and resizing example:")
arr7 = np.arange(10)
print("Original array:", arr7)
print("Reshaped array (2x5):", arr7.reshape(2, 5))
arr7.resize(2, 5)
print("Resized array (in-place):")
print(arr7)

# Sorting
print("\nSorting example:")
arr8 = np.array([4, 2, 6, 1, 9])
print("Original array:", arr8)
print("Sorted array:", np.sort(arr8))

# Iterating over arrays
print("\nIterating over arrays example:")
for row in arr2:
    print(row)

# Finding unique elements
print("\nFinding unique elements example:")
arr9 = np.array([1, 2, 2, 3, 3, 3])
print("Original array:", arr9)
print("Unique elements:", np.unique(arr9))

# Linear algebra operations
print("\nLinear algebra operations example:")
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
x = np.linalg.solve(A, b)
print("Solution to linear equation Ax=b:", x)

# Generating sequence of numbers
print("\nGenerating sequence of numbers example:")
print(np.linspace(0, 10, num=5))  # Generate 5 numbers from 0 to 10

# Masked arrays (for handling missing or invalid data)
print("\nMasked arrays example:")
arr10 = np.ma.array([1, 2, 3], mask=[False, True, False])
print("Masked array:", arr10)
print("Mean of masked array (ignoring masked values):", arr10.mean())
