"""Subset-covering paths from a symmetric chain decomposition."""


def generate_covering_paths_scd():
    """Return 20 permutation paths whose prefixes cover all subsets of A-F."""
    elements = ['A', 'B', 'C', 'D', 'E', 'F']
    n = len(elements)

    # Recursive symmetric chain decomposition of a Boolean lattice.
    # Each chain follows subset inclusion; the middle rank gives a lower bound.

    # Construct chains for k elements.
    def get_chains(k):
        if k == 1:
            # Base case: the empty subset followed by the singleton subset.
            return [[0, 1]]

        # Construct the chains for k - 1 elements.
        prev_chains = get_chains(k - 1)
        new_chains = []

        # Extend the standard recursive symmetric-chain construction.
        # Bit k - 1 represents the new element.
        new_bit = 1 << (k - 1)

        for chain in prev_chains:
            # Extend each previous chain.
            # For a previous chain C = (x1, ..., xm):
            # Create C1 = (x1, ..., xm, xm | new_bit).
            # Retain the chain and append its top subset with the new element.
            c1 = list(chain)
            c1.append(chain[-1] | new_bit)
            new_chains.append(c1)

            # If the previous chain has multiple entries, create a second chain.
            #    C'' = (x1 | new_bit, ..., xm-1 | new_bit)
            # Add the new element to all entries except the old top subset.
            if len(chain) > 1:
                c2 = [x | new_bit for x in chain[:-1]]
                new_chains.append(c2)

        return new_chains

    # Construct chains represented as bit masks.
    # For six elements, this produces binomial(6, 3) = 20 chains.
    chains_mask = get_chains(n)

    formatted_paths = []

    # Extend each chain to a full permutation path.
    for chain in chains_mask:
        # Each chain supplies the middle segment of a maximal subset path.
        # Complete it to a permutation of A through F.

        # Prefix.
        # Add the elements already present in the initial subset.
        # Add these elements alphabetically.
        start_mask = chain[0]
        prefix = []
        for i in range(n):
            if (start_mask >> i) & 1:
                prefix.append(elements[i])
        prefix.sort() # Keep alphabetical order.

        # Middle segment.
        # Each chain step adds one element and defines the middle ordering.
        middle = []
        for i in range(len(chain) - 1):
            # Identify the newly added element.
            diff = chain[i+1] ^ chain[i]
            for b in range(n):
                if (diff >> b) & 1:
                    middle.append(elements[b])
                    break

        # Suffix.
        # Append elements missing from the final subset.
        # Add these elements alphabetically.
        end_mask = chain[-1]
        suffix = []
        # Mask of the full set.
        full_mask = (1 << n) - 1
        # Elements remaining to be appended.
        rem_mask = full_mask ^ end_mask
        for i in range(n):
            if (rem_mask >> i) & 1:
                suffix.append(elements[i])
        suffix.sort() # Keep alphabetical order.

        # Combine the full permutation.
        full_path = prefix + middle + suffix
        formatted_paths.append(full_path)

    # Format and sort the paths.
    # Format the paths as strings for sorting.
    display_lines = []
    for path in formatted_paths:
        display_lines.append(" -> ".join(path))

    # Sort alphabetically.
    display_lines.sort()

    return display_lines

# Run the example.
if __name__ == "__main__":
    final_paths = generate_covering_paths_scd()
    
    print(f"=== Subset-covering paths ({len(final_paths)} paths) ===\n")
    for i, line in enumerate(final_paths, 1):
        print(f"{i:02d}. {line}")
    
    print("\nThe prefixes cover all 2**6 = 64 subsets.")
