from ShapeWarehouse import ShapeWarehouse


def main():
    """
    generate a hundred shapes, and then check their areas, perimeters and color count.
    """
    my_container = ShapeWarehouse()
    my_container.generate(100)
    print("Total area:", my_container.sum_areas())
    print("Total perimeter:", my_container.sum_perimeters())
    print("Colors:", my_container.count_colors())


if __name__ == "__main__":
    main()
