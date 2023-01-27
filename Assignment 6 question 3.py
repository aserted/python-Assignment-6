def pascal_triangle(n):
    # create an empty list to store the rows
    triangle = []
    for i in range(n):
        # create a new row with i+1 elements
        row = [1] * (i + 1)
        # calculate the values of the elements in the row
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        # add the row to the triangle
        triangle.append(row)
    # print the triangle
    for row in triangle:
        print(row)

pascal_triangle(5)
