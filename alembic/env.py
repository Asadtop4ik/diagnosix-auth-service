from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from app.config import settings

# Alembic Config object
config = context.config
fileConfig(config.config_file_name)


config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

