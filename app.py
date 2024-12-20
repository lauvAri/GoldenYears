from typing import Union
from fastapi import FastAPI



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/test")
def test_run():
    import test
    return test.test_run()

@app.get("/main_en_auto")
def main_en_auto_run():
    import main_en_auto
    main_en_auto.client_main()
    return {"running": "main_en_auto"}

@app.get("/get_device")
def get_device_run():
    import get_device
    return get_device.DeviceName

