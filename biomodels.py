import zipfile
import requests
import io

error_log = open('error_log.txt', 'w')

def download_biomodels(model_id):
    url = f'https://www.ebi.ac.uk/biomodels/search/download?models={model_id}'
    response = requests.get(url, stream=True)
    extract = zipfile.ZipFile(io.BytesIO(response.content))
    filename = extract.namelist()[0]
    if filename.lower().endswith('.omex'):
        error_log.write(extract.namelist()[0] + '\n')
        error_log.write(f'{model_id} is omex\n')
        return
    extract.extractall('biomodels')
    extract.close()
    

if __name__ == '__main__':
    download_biomodels('MODEL9811206584')