class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products = None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
category = Category("помидор", "овощи", ["японский","китайский", "европейский"] )

if __name__ == "__main__":
    print(category.name)
    print(category.description)
    print(category.products)
    print(Category.category_count)
    print(Category.product_count)