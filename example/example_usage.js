// Example Javascript code showing how to use BiomodelsStore repo to download a BioModels SBML model.
// Used by example_usage.html
import {getModel} from "../searchClient/getBiomodels.js" // location of download client

const lookUpBtn = document.getElementById("DownloadBtn");

window.onload = function() {
	lookUpBtn.addEventListener("click", (_) => downloadSBMLModel());
}

async function downloadSBMLModel() {

	getBioModel("BIOMD0000000002")  // <-- hard coded
}

async function getBioModel(modelID) {
	const model_text = await getModel(modelID); //  <-- getModel Call ***************
	const model_strTextArea = document.getElementById("model_text")
	model_strTextArea.value = model_text;
	
	
}