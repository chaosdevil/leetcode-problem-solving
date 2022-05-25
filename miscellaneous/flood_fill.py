from ast import literal_eval
from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    # change color of position sr and sc
    # image[sr][sc] = newColor

    m = len(image)
    n = len(image[0])

    # check 4 directions of sr and sc
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    # find all pixels that are connected
    queue = [(sr, sc)]
    visited = {(sr, sc)}
    found_pixels = []

    while queue:
        row, col = queue[0]
        queue = queue[1:]
        found_pixels.append((row, col))

        for d in directions:
            if row + d[0] < m and row + d[0] > -1:
                if col + d[1] < n and col + d[1] > -1:
                    if image[row+d[0]][col+d[1]] == image[row][col]:
                        if (row+d[0], col+d[1]) not in visited:
                            queue.append((row+d[0], col+d[1]))
                            visited.add((row+d[0], col+d[1]))

    # print(results)

    # update all found pixels with new color
    for p in found_pixels:
        image[p[0]][p[1]] = newColor

    return image


if __name__ == "__main__":
    image = literal_eval(input())
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    print(floodFill(image, sc, sc, newColor))
