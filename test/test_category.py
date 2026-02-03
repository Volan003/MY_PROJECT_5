def test_category_init(first_category, second_category):
    assert first_category.name == "яблоко"
    assert first_category.description == "фрукт"
    assert len(first_category.products) == 2

    assert first_category.category_count == 3
    assert second_category.category_count == 3

    assert first_category.product_count == 8
    assert second_category.product_count == 8

def test_category_init_ (category):
    assert category.name == "помидор"
    assert category.description == "овощи"
    assert category.products == []