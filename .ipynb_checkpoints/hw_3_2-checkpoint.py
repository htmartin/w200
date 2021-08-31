# ### 3-2. Matrix Inverter (20 points)

# One place where the usage of tuples is convenient is in the representation of matrices.  The values in a 2x2 matrix are labeled as follows:
# $$
# \begin{bmatrix}
#     a       & b  \\
#     c       & d
# \end{bmatrix}
# $$

# Write code that asks the user for a text string including the four **numbers**, a, b, c, and d, separated by spaces.  You can use the `split()` method on the string to create a list of the four values in order.

# Create a tuple that represents each row, then create a tuple that contains those two tuples.  It should have the form `((a, b), (c, d))`.  **Print this representation.**

# The inverse of the matrix above is given by the formula:

# $$
# \frac{1}{ad-bc} \begin{bmatrix}
#     d       & -b  \\
#     -c       & a
# \end{bmatrix}
# $$

# Recall that multiplying a matrix by a number effectively multiplies each element of the matrix by that number.

# Compute the inverse of the given matrix, again represented as nested tuples, use fstring formatting to show each number to **4** decimal places and **print this representation**. Use the example below to make sure you understand the equation correctly:

# An example on fstring formatting:

# `print(f'matrix: (({a:.4f}, {b:.4f}), ({c:.4f}, {d:.4f}))')"`

# ```
# Please enter four numbers separated by spaces: 1 2 3 4

# matrix: ((1.0000, 2.0000), (3.0000, 4.0000))
# inverse: ((-2.0000, 1.0000), (1.5000, -0.5000))
# ```