import pickle
import os
from Project_siskar.settings import DATAMODELS_DIR

class modelsloader:
    def loadmodels(inputan):
        models_folder = DATAMODELS_DIR
        filepath = os.path.join(models_folder, os.path.basename('nbmodels_81.sav'))
        pickle_in = open(filepath, "rb")
        model = pickle.load(pickle_in)
        prediksi = model.predict([inputan])
        return prediksi
