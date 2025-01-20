## Edge Pixel Counter

In image processing, edge detection is a fundamental operation. This problem focuses on identifying edge pixels in a binary image.

### Concept
A binary image is represented as a 2D matrix where:
- 0 represents background pixels
- 1 represents foreground pixels

An edge pixel is defined as any foreground pixel (1) that has at least one background pixel (0) in its 8-connected neighborhood.

### 8-Connected Neighborhood
For a pixel at position (i,j), its 8 neighbors are:
```
(i-1,j-1)  (i-1,j)  (i-1,j+1)
(i,j-1)    (i,j)    (i,j+1)
(i+1,j-1)  (i+1,j)  (i+1,j+1)
```

### Example
Input image:
```python
[
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
```

Edge pixels (marked with *):
```
1* 1* 1*
1* 0  1*
1* 1* 1*
```

Output: 8 (all outer pixels are edge pixels)

### Things to Note
- All pixel values must be binary (0 or 1)
- The matrix must be well-formed (all rows same length)
- Empty or invalid images return -1
- Edge pixels include those on the image boundary
- Only foreground pixels (1s) can be edge pixels