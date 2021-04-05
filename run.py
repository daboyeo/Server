from app import create_app
from const import RUN_SETTINGS


app = create_app("develop")
app.run(**RUN_SETTINGS)