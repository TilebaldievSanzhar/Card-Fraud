import pickle

PATH_TO_PREPROCESSING = 'preprocessing/'
filename = 'preprocessing_pipeline.pkl'

pipeline_preprocessing = PATH_TO_PREPROCESSING + filename

def load_preprocessing():
    loaded_preprocessing = pickle.load(open(pipeline_preprocessing, 'rb'))
    return loaded_preprocessing