from ingestion import csv_ingestion, excel_ingestion, json_ingestion, parquet_ingestion
from transform import transform

if __name__ == "__main__":
    #file = your_path
    file = "conf.txt"

    csv = csv_ingestion.import_data('csv', file)
    excel = excel_ingestion.import_data('xlsx', file)
    json = json_ingestion.import_data('json', file)
    parquet = parquet_ingestion.import_data('parquet', file)
         
    data = csv.append(excel).append(json).append(parquet)

    final_data = transform.transform(data)

    


    