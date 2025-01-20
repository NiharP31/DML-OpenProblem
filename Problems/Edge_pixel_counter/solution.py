def count_edge_pixels(
    img: list[list[int]]
) -> int:
    # Check if image is empty
    if not img or not img[0]:
        return -1
        
    rows, cols = len(img), len(img[0])
    
    # Validate dimensions and binary values
    for row in img:
        if len(row) != cols:
            return -1
        for pixel in row:
            if pixel not in [0, 1]:
                return -1
    
    # Count edge pixels
    edge_count = 0
    
    # Define 8-connected neighborhood directions
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    for i in range(rows):
        for j in range(cols):
            # Only check neighborhoods of 1-valued pixels
            if img[i][j] == 1:
                # Check all 8 neighbors
                for di, dj in neighbors:
                    ni, nj = i + di, j + dj
                    # If neighbor is outside image or has value 0
                    if (ni < 0 or ni >= rows or 
                        nj < 0 or nj >= cols or 
                        img[ni][nj] == 0):
                        edge_count += 1
                        break
    
    return edge_count


def test_count_edge_pixels() -> None:
    # Test empty image
    assert count_edge_pixels([]) == -1
    
    # Test invalid values
    assert count_edge_pixels([[2]]) == -1
    
    # Test uneven rows
    assert count_edge_pixels([[1,1], [1]]) == -1
    
    # Test single pixel
    assert count_edge_pixels([[1]]) == 1
    
    # Test all ones 3x3 (only outer pixels are edges)
    img1 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert count_edge_pixels(img1) == 8
    
    # Test checkerboard pattern
    img2 = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    assert count_edge_pixels(img2) == 5
    
    # Test isolated pixels
    img3 = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 0]
    ]
    assert count_edge_pixels(img3) == 2

if __name__ == "__main__":
    test_count_edge_pixels()
    print("All tests passed.")