import modal
from main import app as fastapi_app

image = modal.Image.debian_slim().poetry_install_from_file("pyproject.toml").pip_install("llama-index-callbacks-arize-phoenix")

app = modal.App("pillpoe", image=image)



@app.function(mounts=[modal.Mount.from_local_file(".env", remote_path="/root/.env")])
@modal.asgi_app()
def go():
    return fastapi_app