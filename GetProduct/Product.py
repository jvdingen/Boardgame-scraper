from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    website: int
    product_name: str
    product_price_in_discount: bool
    product_price: float
    product_original_price: float
    product_in_stock: bool
    product_stock_amount: int