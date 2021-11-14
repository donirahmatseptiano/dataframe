def product(dataframe):
    df = (dataframe.groupby(['lokasi']).agg({'qty':'sum','sales':'sum'})
    .reset_index())
    
    return df