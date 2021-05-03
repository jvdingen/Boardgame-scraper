from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    website: str
    product_name: str
    product_price_in_discount: bool
    product_price: float
    product_original_price: float
    product_in_stock: bool