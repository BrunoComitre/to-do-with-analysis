from logging import Logger
import uvicorn
from app.main import app, gunicorn_logger, logging


if __name__ == "__main__":
    Logger.setLevel(gunicorn_logger.level)
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, log_level="info")
else:
    Logger.setLevel(logging.DEBUG)
