import pandas as pd
columns = ['check_id', 'Purchaser', 'OwnerID', 'DocNumber', 'DocDate', 'DocAmount', 'DivisionOrder', 'ProductCode', 'ProdYY', 'ProdMM', 'InterestType', 'InterestPercent', 'GrossVolume', 'GrossValue', 'OwnerGrossValue', 'State', 'County', 'TransactionCode', 'GrossDeduction', 'OwnerDeduction', 'id']

check = {
        "keys": {
            "DocDate": "06/20/2022",
            "OwnerID": "1010184227",
            "DocAmount": "$961.02",
            "DocNumber": "0005203119",
            "Purchaser": "MERITENERGYCOMPANY",
        },
        "vendor": "MERITENERGYCOMPANY",
        "batch_id": "20230706.000022",
        "check_id": "20230706.000022.10",
        "line_items": [
            {
                "id": "10f2617d-8536-48ea-9bf0-9c43758e7118",
                "None": "",
                "Price": "5.49",
                "State": "AR",
                "County": "CRAWFORD",
                "ProdMM": "04",
                "ProdYY": "2022",
                "GrossNet": "221.10",
                "GrossTax": "1597",
                "OwnerTax": "0.23",
                "GrossValue": "1.21166",
                "PlaceHolder": "95.10 0.01445300",
                "ProductCode": "A",
                "InterestType": "B",
                "DivisionOrder": "00123562 00001",
                "OwnerNetValue": "15.94",
                "OwnerDeduction": "1.37",
                "GrossDeduction": "95.10",
                "OwnerGrossValue": "17.54",
                "InterestPercent": "0.01445300",
                "TransactionCode": 'AB',
                "GrossVolume": "123.45"
            },
            {
                "id": "789f63b4-f812-4b82-aa4f-5ba1c75b4bc9",
                "None": "",
                "Price": "5.49",
                "State": "AR",
                "County": "CRAWFORD",
                "ProdMM": "04",
                "ProdYY": "2022",
                "GrossNet": "420.62",
                "GrossTax": "30.39",
                "OwnerTax": "043",
                "GrossValue": "2.308.91",
                "PlaceHolder": "180.92 0.01445300",
                "ProductCode": "G",
                "InterestType": "A",
                "DivisionOrder": "00123566 00001",
                "OwnerNetValue": "30.32",
                "OwnerDeduction": "2.62",
                "GrossDeduction": "180.92",
                "OwnerGrossValue": "33.37",
                "InterestPercent": "0.01445300",
                "TransactionCode": 'AB',
                "GrossVolume": "123.45"                
            },
            {
                "id": "4a762a81-9edb-469c-bfec-26626d70e7ec",
                "None": "",
                "Price": "5.49",
                "State": "AR",
                "County": "CRAWFORD",
                "ProdMM": "04",
                "ProdYY": "2022",
                "GrossNet": "2.969.86",
                "GrossTax": "214.59",
                "OwnerTax": "926",
                "GrossValue": "16306.38",
                "PlaceHolder": "1.277.35 0.04319300",
                "ProductCode": "G",
                "InterestType": "B",
                "DivisionOrder": "00123738 00001",
                "OwnerNetValue": "639.89",
                "OwnerDeduction": "55.17",
                "GrossDeduction": "1.277.35",
                "OwnerGrossValue": "704.32",
                "InterestPercent": "0.04319300",
                "TransactionCode": 'AB',
                "GrossVolume": "123.45"                
            },
            {
                "id": "f07cf776-57df-4dda-b213-92a083130e57",
                "None": "",
                "Price": "5.49",
                "State": "AR",
                "County": "CRAWFORD",
                "ProdMM": "04",
                "ProdYY": "2022",
                "GrossNet": "1870.33",
                "GrossTax": "135.11",
                "OwnerTax": "2.11",
                "GrossValue": "1026676",
                "PlaceHolder": "804.48 0.01562500",
                "ProductCode": "G",
                "InterestType": "B",
                "DivisionOrder": "00124387 00001",
                "OwnerNetValue": "145.74",
                "OwnerDeduction": "12.57",
                "GrossDeduction": "804.48",
                "OwnerGrossValue": "160.42",
                "InterestPercent": "0.01562500",
                "TransactionCode": 'AB',
                "GrossVolume": "123.45"                
            },
            {
                "id": "97fcad68-9995-4b40-9ab2-4bd8370a7c5b",
                "None": "",
                "Price": "5.49",
                "State": "AR",
                "County": "CRAWFORD",                
                "ProdMM": "04",
                "ProdYY": "2022",
                "GrossNet": "1.08191",
                "GrossTax": "78.31",
                "OwnerTax": "1.22",
                "GrossValue": "5.94988",
                "PlaceHolder": "466.22 0.01562500",
                "ProductCode": "G",
                "InterestType": "B",
                "DivisionOrder": "00124388 00001",
                "OwnerNetValue": "84.47",
                "OwnerDeduction": "7.28",
                "GrossDeduction": "466.22",
                "OwnerGrossValue": "92.97",
                "InterestPercent": "0.01562500",
                "TransactionCode": 'AB',
                "GrossVolume": "123.45"
            },
            {
                "id": "a487b636-c645-4a54-b9dc-c5596226610b",
                "None": "",
                "Price": "5.49",
                "State": "AR",
                "County": "CRAWFORD",
                "None_1": "",
                "ProdMM": "04",
                "ProdYY": "2022",
                "GrossNet": "573.00",
                "GrossTax": "41.41",
                "OwnerTax": "0.65",
                "GrossValue": "3146.12",
                "PlaceHolder": "246.45 0.01562500",
                "ProductCode": "G",
                "InterestType": "B",
                "DivisionOrder": "00124389 00001",
                "OwnerNetValue": "4466",
                "OwnerDeduction": "3.85",
                "GrossDeduction": "246.45",
                "OwnerGrossValue": "49.16",
                "InterestPercent": "0.01562500",
                "TransactionCode": 'AB',
                "GrossVolume": "123.45"                
            }
        ]
    }

df = pd.DataFrame(check["line_items"])
if 'keys' in check.keys():
    key_items = check['keys']
    for k,v in key_items.items():
        df.insert(0,k,v)
    
    df.insert(0, 'check_id', '20230706.000022.10')

file_path = f'C:/Users/ttrang/Downloads/test.csv'
df.to_csv(file_path, index=False,columns=columns,  header=True, sep=',')

print(df)