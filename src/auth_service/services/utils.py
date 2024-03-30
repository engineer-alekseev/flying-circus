from fastapi import Request, HTTPException, status


def get_telegram_id(request: Request):
    id = request.headers.get("X-Telegram-ID")
    
    print("Telegram ID:", id)

    if id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Invalid Auth Header "X-Telegram-ID"',
        )

    return id
