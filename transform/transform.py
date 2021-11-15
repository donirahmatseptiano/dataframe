def transform(data):    
    final_data = (data.groupby(['lokasi']).agg({'qty':'sum','sales':'sum'})
                    .reset_index()
                    .rename(columns={'qty':'total_quantity', 'sales':'total_sales'}))
    
    final_data.to_csv('data_sales.csv', index=False)

    print('export finished')

    return final_data