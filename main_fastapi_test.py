from fastapi import FastAPI
from dash import Dash, html
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

# Crie a aplicação FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criando a aplicação Dash
# OBS: requests_pathname_prefix='/dash/' -> Isso garante que os arquivos estáticos do Dash, como JavaScript e CSS,
# sejam carregados corretamente usando o caminho correto ao acessar o Dash via /dash.
dash_app = Dash(__name__, requests_pathname_prefix='/dash/')
dash_app.layout = html.Div("Olá do Dash com FastAPI")

# Adicionando o Dash à aplicação FastAPI
app.mount("/dash", WSGIMiddleware(dash_app.server))


@app.get("/home")
async def redirect_to_dash():
    # Redirecionando a rota raiz para o dashboard
    print("Teste")
    return RedirectResponse(url="/dash")


# Rodando o servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
