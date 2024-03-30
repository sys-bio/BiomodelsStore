import os
import shutil
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
    model_files_info = bmservices.get_model_files_info(model_id)
    # Check if there are files associated with the model_id
    if model_files_info is None:
        print(f'Error in downloading {model_id}')
        error_log.write(f'Error in downloading {model_id}\n')
        error_log.write('\n')
        return
    
    if ":" in model_files_info["main"][0]["name"]:
        model_files_info["main"][0]["name"] = "_".join(model_files_info["main"][0]["name"].split(":"))
    
    # Check if the model is an SBML file
    if not model_files_info["main"][0]["name"].lower().endswith('.xml') and not model_files_info["main"][0]["name"].lower().endswith('.sbml'):
        print(f'{model_id} is not an SBML file')
        error_log.write(f'{model_id} is not an SBML file\n')
        error_log.write('\n')
        return
    
    # Download the model file into the 'biomodels' directory
    os.chdir("biomodels")
    bmservices.download(model_id, model_files_info["main"][0]["name"])
    os.chdir("..")
    print(f'{model_id} downloaded successfully')

if __name__ == '__main__':
    model_ids = bmservices.get_model_identifiers()

    # Download all the models from BioModels database using the model_id
    for model_id in model_ids["models"]:
        try:
            if "BIOMD" not in model_id:
                break
            # Check if the model is already downloaded
            elif model_id in os.listdir("biomodels") and len(os.listdir(f"biomodels/{model_id}")) == 1:
                print(f'{model_id} already downloaded')
                continue
            model_files = bmservices.get_model_files_info(model_id)
            # Get the main model file
            model = model_files["main"][0]["name"]
            if ":" in model:
                model = "_".join(model.split(":"))
            download_biomodel(model_id)
            # If it is an SBML file, move it to the directory corresponding to the model_id
            os.makedirs(f"biomodels/{model_id}", exist_ok=True)
            shutil.move(f"biomodels/{model}", f"biomodels/{model_id}/{model}")
            print(f'{model_id}/{model} moved successfully')
        except Exception as e:
            error_log.write(model_id + '\n')
            error_log.write(str(e) + '\n')
            error_log.write('\n')
            continue
