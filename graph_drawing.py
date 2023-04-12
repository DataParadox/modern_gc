import matplotlib.pyplot as plt 
import pandas as pd
import plotly.io as pio
from plotly.io import write_image
import plotly.express as px
import os
import logging

logger = logging.getLogger(__name__)



def main(args):

    df = pd.read_csv(args.csv)
    df.fillna(0)
    df.rename(columns = {args.gc:'group'}, inplace = True)
    
    for col in df.columns[df.columns.get_loc(args.gc)+1:]:
      fig = px.bar(df, x=args.benchmark, y=col,
                 color='group', barmode='group',text=col,
                 height=400)
      fig_name = col
      write_image(fig,args.csv+col+"_fig.png")
      fig.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--csv", type=str, help="CSV file name")
    parser.add_argument("--gc", type=str, help="GC column name")
    parser.add_argument("--benchmark", type=str, help="Benchmark column name")
    args, _ = parser.parse_known_args()
    main(args)