import requests
from requests import Response


def check_product(city: str, shop_id: int, product_id: int) -> bool:
    rossmann_response: Response = requests.get(
        f'https://www.rossmann.pl/shopping/api/shops/{shop_id}/products/{product_id}/availability'  # noqa: E501
    )
    data_json: dict = rossmann_response.json()

    for shop in data_json.get('data', {}).get('shops'):
        shop_string: str = str(shop)
        if 'NoAvailable' not in shop_string and city in shop_string:
            return True

    return False
