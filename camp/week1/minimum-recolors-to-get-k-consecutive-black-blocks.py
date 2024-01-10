class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_recolors = float('inf')
        white_count = 0
        left = 0

        # Count the initial number of white blocks within the first k blocks
        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1

        # Update the minimum recolors if necessary
        if white_count < min_recolors:
            min_recolors = white_count

        # Slide the window and update the white count
        for right in range(k, n):
            if blocks[right] == 'W':
                white_count += 1

            if blocks[left] == 'W':
                white_count -= 1

            # Update the minimum recolors if necessary
            if white_count < min_recolors:
                min_recolors = white_count

            left += 1

        return min_recolors