from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware
# from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from dash_functions import create_dash

# Criando a aplicação FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dash_app = create_dash()

# Adicionando o Dash à aplicação FastAPI
app.mount("/dash", WSGIMiddleware(dash_app.server))


# @app.get("/")
# async def redirect_to_dash():
#     # Redirecionando a rota raiz para o dashboard
#     # return RedirectResponse(url="/dash")


"""
Sobre as mensagens de retorno das requisições:

Mensagens de Retorno:

INFO:     127.0.0.1:56963 - "GET /dash/ HTTP/1.1" 200 OK
INFO:     127.0.0.1:56964 - "GET /dash/_dash-dependencies HTTP/1.1" 200 OK
INFO:     127.0.0.1:56963 - "GET /dash/_dash-layout HTTP/1.1" 200 OK
INFO:     127.0.0.1:56964 - "GET /dash/_favicon.ico?v=2.18.1 HTTP/1.1" 200 OK
INFO:     127.0.0.1:56964 - "GET /dash/_dash-component-suites/dash/dcc/async-dropdown.js HTTP/1.1" 304 Not Modified
INFO:     127.0.0.1:56963 - "GET /dash/_dash-component-suites/dash/dcc/async-graph.js HTTP/1.1" 304 Not Modified
INFO:     127.0.0.1:56964 - "POST /dash/_dash-update-component HTTP/1.1" 200 OK
INFO:     127.0.0.1:56963 - "GET /dash/_dash-component-suites/plotly/package_data/plotly.min.js HTTP/1.1" 304 Not Modified


Informações:

Nada deu errado nessas requisições. Tudo está funcionando corretamente. 
As mensagens de 200 OK indicam que as requisições foram processadas com sucesso, e os 304 Not Modified indicam que 
certos recursos foram carregados do cache do navegador, o que melhora o desempenho. Essas são mensagens comuns em 
qualquer servidor web que esteja servindo conteúdo dinâmico como gráficos e layouts.
"""

# Rodando o servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
