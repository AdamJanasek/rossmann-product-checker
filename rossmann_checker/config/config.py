import os
from typing import Tuple, Dict, Optional


class Config:
    city: Optional[str] = os.getenv('CITY')
    shop_id: Optional[str] = os.getenv('SHOP_ID')
    product_id: Optional[str] = os.getenv('PRODUCT_ID')
    email_from: Optional[str] = os.getenv('EMAIL_FROM')
    password: Optional[str] = os.getenv('PASSWORD')
    email_to: Optional[str] = os.getenv('EMAIL_TO')
    message: Dict[str, Optional[str]] = {
        'subject': os.getenv('SUBJECT'),
        'message': os.getenv('MESSAGE'),
    }

    def get_product_args(self) -> Tuple[Optional[str], ...]:
        return self.city, self.shop_id, self.product_id

    def get_email_args(self) -> Tuple[
        Optional[str],
        Optional[str],
        Optional[str],
        Dict[str, Optional[str]]
    ]:
        return self.email_from, self.password, self.email_to, self.message
