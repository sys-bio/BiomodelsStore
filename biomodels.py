import os
import zipfile
import requests
import io
from biomodels_restful_api_client import services as bmservices

"""
This script is used to download all the models from BioModels database.
The models are downloaded in the 'biomodels' directory.
The error log is written to 'error_log.txt' file.
"""

error_log = open('error_log.txt', 'w')

# Download the SBML model from BioModels database using the model_id
def download_biomodel(model_id):
    url = f'https://www.ebi.ac.uk/biomodels/search/download?models={model_id}'
    response = requests.get(url, stream=True)
    extract = zipfile.ZipFile(io.BytesIO(response.content))
    while extract.namelist()[0].endswith('.zip'):
        extract = zipfile.ZipFile(io.BytesIO(extract.read(extract.namelist()[0])))
    print(extract.namelist())
    filename = extract.namelist()[0]
    if not filename.lower().endswith('.xml') and not filename.lower().endswith('.sbml'):
        print(f'{model_id} is not an SBML file')
        error_log.write(f'{model_id} is not an SBML file\n')
        error_log.write('\n')
        return
    extract.extractall('biomodels')
    print(f'{model_id} downloaded successfully')
    extract.close()


if __name__ == '__main__':
    model_ids = bmservices.get_model_identifiers()

    # Download all the models from BioModels database using the model_id
    for model_id in model_ids["models"]:
        try:
            if f"{model_id}.xml" in os.listdir("biomodels") or "BIOMD" not in model_id:
                print(f'{model_id} already downloaded')
                continue
            download_biomodel(model_id)
        except Exception as e:
            error_log.write(model_id + '\n')
            error_log.write(str(e) + '\n')
            error_log.write('\n')
            continue
