import logging
import uvicorn

# Optional: configure Python logging to file
logging.basicConfig(
    filename="django.log",
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(name)s: %(message)s'
)

# Ensure Uvicorn logs propagate to the root logger
logging.getLogger("uvicorn").propagate = True
logging.getLogger("uvicorn.access").propagate = True
logging.getLogger("uvicorn.error").propagate = True


if __name__ == "__main__":
    uvicorn.run(
        app="test_app.asgi:application",
        host="0.0.0.0",
        port=3001,
        workers=4,
        reload=True,
        log_config=None,
        # log_level="INFO"
    )