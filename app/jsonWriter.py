#Así se abre un json:
with open('rango.json') as fp:
    js_param = json.load(fp)

#Así se obtienen los valores de una row. 
for row in js_param: 
    
    #Valores generales:
    #Si el archivo se automatiza, la última revisión cada vez sería a las 00:00. 
    all_last_time = row['all_last_time'] #La última vez que se corrió el programa y que se actualizaron estos valores.
    adstotals_last_cell = row['adstotals_last_cell'] #La última celda revisada de Adwords Totales.
    adscampaigns_last_cell = row['adscampaigns_last_cell'] #La última celda revisada de Adwords por campaña.
    ads_spent = row['ads_spent']

#Así se editan las celdas de una row: 
for row in js_param:
    
    print("Estos serán los nuevos valores a guardar: ")
    row['all_win'] = all_win
    row['all_last_time'] = timeTag
    row['adstotals_last_cell'] = new_adstotals_last_cell
    row['adscampaigns_last_cell'] = new_adscampaigns_last_cell
    row['paypal_last_cell'] = new_paypal_last_cell
    row['ads_spent'] = costo_ads
    row['paypal_total'] = suma


#Escribe 
    with open('rango.json', 'w', encoding='utf-8') as jsonf: 
        jsonf.write(json.dumps(js_param, indent=0)) 