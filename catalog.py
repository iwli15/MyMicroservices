from fastapi import FastAPI

app = FastAPI()

menu = {
    "1": {"name": "Burger", "price": 5.99},
    "2": {"name": "Pizza", "price": 8.99},
    "3": {"name": "Salad", "price": 4.50}
}

@app.get("/menu/{item_id}")
def get_menu_item(item_id: str):
    return menu.get(item_id, {"error": "Item not found"})