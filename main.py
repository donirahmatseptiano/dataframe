from ingestion import csv_ingestion, excel_ingestion, json_ingestion, parquet_ingestion
from transform import csv_transform, excel_transform, json_transform, parquet_transform

if __name__ == "__main__":
    #file = your_path
    file = "conf.txt"

    csv = csv_ingestion.import_data('csv', file)
    csv = csv_transform.product(csv)

    excel = excel_ingestion.import_data('xlsx', file)
    excel = excel_transform.product(excel)

    json = json_ingestion.import_data('json', file)
    json = json_transform.product(json)

    parquet = parquet_ingestion.import_data('parquet', file)
    parquet = parquet_transform.product(parquet)
    
    data = csv.append(excel).append(json).append(parquet)

    final_data = (data.groupby(['lokasi']).agg({'qty':'sum','sales':'sum'})
                .reset_index()
                .rename(columns={'qty':'total_quantity', 'sales':'total_sales'}))

    final_data.to_csv('data_sales.csv', index=False)


    