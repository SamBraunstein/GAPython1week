import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.title = 'Deloitte Dash'

app.layout = html.Div(children=[
    html.H1('Tech startups raising more private capital'),
    dcc.Graph(
        id='this_is_an_id',
        figure={
            'data': [
                {'x': ['2016', '2017', '2018'], 'y': [16, 12, 28], 'type': 'bar', 'name': '100MM+ Capital'},
                {'x': ['2016', '2017', '2018'], 'y': [3, 6, 5], 'type': 'bar', 'name': 'IPO Capital'},
            ],
            'layout': {
                'title': "$100MM+ US VC Rounds versus US VC IPOs",
                'xaxis':{'title':'Choice of data visualization'},
                'yaxis':{'title':'Approval rating by average data scientist'},
            }
        }
    )]
)

if __name__ == '__main__':
    app.run_server()
