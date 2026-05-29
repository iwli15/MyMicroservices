from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/order/{item_id}")
async def place_order(item_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://127.0.0.1:8000/menu/{item_id}")
        item_data = response.json()

        if "error" in item_data:
            return {"status": "Failed", "message": "Item not found in menu"}

        return {
            "status": "Order Placed Successfully",
            "order_details": item_data
        }