import polars as pl
from plotnine import ggplot, geom_point, aes

def main():
    df = pl.read_csv("datos/penguins.csv")
    grafico = ggplot(df) + geom_point(aes(x="bill_length_mm", y="bill_depth_mm"))
    grafico.save("plot.png")


if __name__ == "__main__":
    main()
