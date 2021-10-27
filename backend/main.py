from fastapi import FastAPI

app = FastAPI()


@app.get('/board')
def get_board():
    return {'board': {}}
