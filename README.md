# BiomodelsStore

A repository that stores BioModels [https://www.ebi.ac.uk/biomodels/]. This repository used in conjunction with BiomodelsCache [https://github.com/sys-bio/BiomodelsCache] can be used to speed up the search and download of BioModels. Models can be retrieved from this repository using PyGithub (GitHub API), or any other Github API as per the use cases.

# Using the BioModelsStore

It is required that you have a BioModel ID of the model you are interested in. Currently we have a JavaScript client that makes the interaction straightforward. The file is at **`../searchClient/getBiomodels.js`**. Using this JavaScript client requires only one function call to get model information:
- `const model_text = await getModel(modelID);`

This takes a string corresponding to the model ID (ex: `"BIOMD0000000002"`) and returns the SBML model as a string. For other programming languages, support for a GitHub API is needed (OctoKit, PyGithub, etc). Look at the JavaScript Client for assistance in building your own client.

## Example usage
- A simple HTML/js webpage that uses the JavaScript client is here: [https://github.com/sys-bio/BiomodelsStore/tree/main/example]. See `example_usage.js` for the actual calls to the JavaScript client and BioModels cache.
- A more developed application is [MakeSBML](https://sys-bio.github.io/makesbml/) which can download a Biomodel and translates it from SBML to Antimony.
