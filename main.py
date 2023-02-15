from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        return self._change_colors(image, sr, sc, color)

    def _change_colors(self, image, sr, sc, color):
        # Prepare for constraints
        rows, cols = len(image), len(image[0])

        # Get initial color
        initial_color = image[sr][sc]

        # If the initial color is the same as new color, do nothing.
        if initial_color == color:
            return image

        # Initialize the stack
        stack = [(sr, sc)]

        # While stack is not empty
        while len(stack):
            r, c = stack.pop()

            # If outbound, continue to next item
            if not (0 <= r < rows and 0 <= c < cols):
                continue

            # Check if it's not the same color
            if image[r][c] != initial_color:
                continue

            # Passed all conditions? update the color.
            image[r][c] = color

            # Add the 4-directionally connected cells
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                stack.append((r + dr, c + dc))

        print(image)
        return image
