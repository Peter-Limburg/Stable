from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/{source}")
async def receive_webhook(source: str, request: Request):
    payload = await request.body()
    print(f"Received webhook from: {source}, bytes: {len(payload)}")
    return {"status": "received", "source": source}
