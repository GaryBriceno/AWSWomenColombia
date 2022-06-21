FastAPI requiere un servidor ASGI, similar a:
- [Uvicorn](https://www.uvicorn.org/)

Ejecutar la aplicacion:
> uvicorn main:app --reload

Kill process in Mac:
> sudo kill -9  $(pgrep -- P $uvicorn_pid)
