"""Visualize three concentric cubic grids with 27 vertices each.

    python src/nested_lattices.py                 # interactive window
    python src/nested_lattices.py --output fig.png  # save instead of showing
"""

import argparse

import matplotlib.pyplot as plt
import numpy as np

def draw_all_vertices_cubes(output=None):
    """Display the grids with side lengths 3, 5, and 7, or save them to ``output``."""
    fig = plt.figure(figsize=(6, 6) if output else (12, 12))
    ax = fig.add_subplot(111, projection='3d')

    # Side lengths of the three nested layers.
    sizes = [3, 5, 7]

    # Color and opacity for each layer.
    layer_styles = [
        # Inner layer: dark red.
        {'color': '#A00000', 'alpha': 0.5, 'lw': 1.2},

        # Middle layer: steel blue.
        {'color': '#4682B4', 'alpha': 0.6, 'lw': 0.9},

        # Outer layer: gray.
        {'color': '#505050', 'alpha': 0.7, 'lw': 0.6},
    ]

    # Draw grid lines along each coordinate axis.
    def draw_grid_lines(ax, ticks, color, alpha, lw):
        # X direction.
        for y in ticks:
            for z in ticks:
                ax.plot([ticks[0], ticks[-1]], [y, y], [z, z],
                        color=color, alpha=alpha, linewidth=lw)
        # Y direction.
        for x in ticks:
            for z in ticks:
                ax.plot([x, x], [ticks[0], ticks[-1]], [z, z],
                        color=color, alpha=alpha, linewidth=lw)
        # Z direction.
        for x in ticks:
            for y in ticks:
                ax.plot([x, x], [y, y], [ticks[0], ticks[-1]],
                        color=color, alpha=alpha, linewidth=lw)

    # Draw each layer.
    for i, size in enumerate(sizes):
        style = layer_styles[i]

        # Generate three coordinate values per axis.
        ticks = np.linspace(-size/2, size/2, 3)

        # Draw grid lines.
        draw_grid_lines(ax, ticks, style['color'], style['alpha'], style['lw'])

        # Draw the vertices of every layer.
        # Generate all 27 coordinate triples.
        X, Y, Z = np.meshgrid(ticks, ticks, ticks)

        # Draw vertices.
        ax.scatter(X, Y, Z,
                   c=style['color'],    # Use the layer color.
                   s=50,                # Marker size.
                   alpha=max(style['alpha'], 0.5), # Keep vertices at least as opaque as the grid.
                   edgecolor='none',    # Omit marker outlines.
                   depthshade=False     # Disable depth shading.
                   )

    # Set the view and layout.
    ax.set_axis_off()
    ax.set_box_aspect([1,1,1])
    ax.view_init(elev=25, azim=-45)
    plt.tight_layout()
    if output:
        fig.savefig(output, dpi=200, bbox_inches="tight")
        print(f"wrote {output}")
    else:
        plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Draw three nested cubic grids.")
    parser.add_argument("--output", help="save the figure to this path instead of opening a window")
    draw_all_vertices_cubes(parser.parse_args().output)
