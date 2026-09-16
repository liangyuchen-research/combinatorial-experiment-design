import sys
import math
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from product_lattice_width import calculate_max_width
from boolean_subset_paths import generate_covering_paths_scd


class CombinatorialInvariants(unittest.TestCase):
    def test_product_lattice_rank_counts(self):
        rank, width, counts = calculate_max_width()
        self.assertEqual(sum(counts), 5**6)
        self.assertEqual(counts, list(reversed(counts)))
        self.assertEqual(rank, 12)
        self.assertEqual(width, max(counts))

    def test_boolean_subset_cover(self):
        paths = generate_covering_paths_scd()
        self.assertEqual(len(paths), math.comb(6, 3))
        covered = {frozenset()}
        for line in paths:
            nodes = line.split(" -> ")
            self.assertEqual(sorted(nodes), list("ABCDEF"))
            covered.update(frozenset(nodes[:n]) for n in range(7))
        self.assertEqual(len(covered), 2**6)


if __name__ == "__main__":
    unittest.main()
