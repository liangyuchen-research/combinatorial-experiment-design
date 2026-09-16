def calculate_max_width():
    # Start with the constant polynomial 1.
    # coefs[i] is the coefficient of x**i.
    coefs = [1]

    # Multiply once per dimension.
    dimensions = 6
    points_per_dim = 5  # Number of coordinate values per dimension.

    for _ in range(dimensions):
        # The maximum degree increases by points_per_dim - 1.
        new_len = len(coefs) + (points_per_dim - 1)
        new_coefs = [0] * new_len

        # Convolve the current coefficients with the next factor.
        # Multiply by 1 + x + ... + x**(points_per_dim - 1).
        for i, c in enumerate(coefs):
            for step in range(points_per_dim):
                new_coefs[i + step] += c

        coefs = new_coefs

    # Find the largest rank and its index.
    max_points = max(coefs)
    max_layer = coefs.index(max_points)

    return max_layer, max_points, coefs

if __name__ == "__main__":
    layer, count, distribution = calculate_max_width()
    
    print(f"Largest rank index: {layer}")
    print(f"Largest rank size (chain-cover lower bound): {count}")
