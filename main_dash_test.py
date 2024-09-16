from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd


app = Dash(__name__)

# df = pd.DataFrame({
#     "Fruit": ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
# })

df = pd.read_excel('Vendas.xlsx')


fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append('Todas as Lojas')


app.layout = html.Div(children=[
    html.H1(children='First Dashboard'),  # -> Componente HTML.

    html.Div(children='''
    Dash Application Framework'''),  # -> Componente HTML.

    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas'),  # -> Componente do dcc (data core component).

    dcc.Graph(id='grafico_quantidade_vendas', figure=fig)  # -> Componente do dcc (data core component).
])


@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_graph(data):
    # data recebe o valor de value do Input.
    if data == 'Todas as Lojas':
        fig_function = px.bar(df, x='Produto', y='Quantidade', color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == data]
        fig_function = px.bar(tabela_filtrada, x='Produto', y='Quantidade', color="ID Loja", barmode="group")
    return fig_function


if __name__ == '__main__':
    app.run_server(debug=True)
