import plotly.express as px
import requests
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import time
import js
import json
import plotly
from pyodide.http import pyfetch
import asyncio

API_URL = "https://p60frowj71.execute-api.eu-west-1.amazonaws.com/prd/interconnector"
response = await pyfetch(API_URL, method="GET")
output = f"GET request=> status:{response.status}, json:{await response.json()}"
print(response)


# def df_maker():
#     response = pyfetch(API_URL, method="GET")
#     df_json = response.json()
#     df = pd.DataFrame.from_dict(df_json["body"]["Responses"]["interconnector-data"])

#     df["datetime"] = df["datetime"].apply(
#         lambda x: datetime.strptime(str(x), "%Y%m%d%H%M%S")
#     )
#     df = df.sort_values(by=["datetime"])
#     return df


# df = df_maker()

# fig = go.FigureWidget()
# fig.add_scatter(x=df["datetime"], y=df["France"])
# fig.add_scatter(x=df["datetime"], y=df["Belgium"])
# fig.add_scatter(x=df["datetime"], y=df["Netherlands"])
# fig.add_scatter(x=df["datetime"], y=df["Norway"])


# def plot():
#     graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     js.plot(graphJSON, "chart1")


# plot()


# while True:
#     time.sleep(5)
#     with fig.batch_update():
#         df = df_maker()
#         df2 = pd.DataFrame.from_dict(
#             {
#                 "France": [10],
#                 "datetime": [
#                     datetime.strptime("2022-10-16 09:16:00", "%Y-%m-%d %H:%M:%S")
#                 ],
#                 "date": [20221016],
#                 "Belgium": [10],
#                 "Netherlands": [10],
#                 "Norway": [10],
#             }
#         )
#         df = df.append(df2)
#         fig.data[0].y = df["France"]
#         fig.data[0].x = df["datetime"]
#         fig.data[1].y = df["Belgium"]
#         fig.data[1].x = df["datetime"]
#         fig.data[2].y = df["Netherlands"]
#         fig.data[2].x = df["datetime"]
#         fig.data[3].y = df["Norway"]
#         fig.data[3].x = df["datetime"]
#         plot()
