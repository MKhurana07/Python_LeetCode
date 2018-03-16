def rotate_image(image):
    image[:] = map(lambda x: list(x),zip(*image[::-1]))
    return image

print(rotate_image([[1,2,3],[4,5,6],[7,8,9]]))
