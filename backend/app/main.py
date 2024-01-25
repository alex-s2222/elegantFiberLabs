from fastapi import FastAPI
import uvicorn 

from routes import user, auth



def create_app():

    app = FastAPI(
        title='Elegant Fiber Labs'
    )

    return app


app = create_app()

app.include_router(user.router, tags=['User'], prefix='/api/user')
app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')


@app.get("/", description='hello')
async def test():
    return {'test':'good'}




if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)