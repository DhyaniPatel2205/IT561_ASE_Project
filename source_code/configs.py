# -*- coding: utf-8 -*-
#pylint: skip-file
import os 

class CommonConfigs(object):
    def __init__(self, d_type):
        self.ROOT_PATH = os.getcwd() + "/"
        self.TRAINING_DATA_PATH = "/content/drive/MyDrive/dhyani_code2que_new/source_code/so/train_set/"
        self.VALIDATE_DATA_PATH = "/content/drive/MyDrive/dhyani_code2que_new/source_code/so/validate_set/"
        self.TESTING_DATA_PATH = "/content/drive/MyDrive/dhyani_code2que_new/source_code/so/test_set/"
        self.RESULT_PATH = "/content/drive/MyDrive/dhyani_code2que_new/source_code/so/result/"
        self.MODEL_PATH = "/content/drive/MyDrive/dhyani_code2que_new/source_code/so/models_py/"
        self.BEAM_SUMM_PATH = "/content/drive/MyDrive/dhyani_code2que_new/source_code/so/result/beam_summary/"
        self.BEAM_GT_PATH = "/content/drive/MyDrive/dhyani_code2que_new/source_code/so/result/beam_ground_truth/"
        self.GROUND_TRUTH_PATH = "/content/drive/MyDrive/dhyani_code2que_new/source_code/so/result/ground_truth/"
        self.SUMM_PATH = "/content/drive/MyDrive/dhyani_code2que_new/source_code/so/result/summary/"
        self.TMP_PATH = "/content/drive/MyDrive/dhyani_code2que_new/source_code/so/tmp/"


class DeepmindTraining(object):
    IS_UNICODE = False
    REMOVES_PUNCTION = False
    HAS_Y = True
    BATCH_SIZE = 16 

class DeepmindTesting(object):
    IS_UNICODE = False
    HAS_Y = True
    BATCH_SIZE = 100
    MIN_LEN_PREDICT = 35
    MAX_LEN_PREDICT = 120
    MAX_BYTE_PREDICT = None
    PRINT_SIZE = 500
    REMOVES_PUNCTION = False


class DeepmindConfigs():
    
    cc = CommonConfigs("so")
   
    CELL = "gru" # "lstm" # gru or lstm
    CUDA = True
    COPY = True
    COVERAGE = True
    BI_RNN = True
    BEAM_SEARCH = True
    BEAM_SIZE = 4
    # AVG_NLL = True
    AVG_NLL = False
    NORM_CLIP = 2
    if not AVG_NLL:
        NORM_CLIP = 5
    LR = 0.15 

    DIM_X = 100 
    DIM_Y = DIM_X

    MIN_LEN_X = 16
    MIN_LEN_Y = 4 
    MAX_LEN_X = 128 
    MAX_LEN_Y = 64 
    MIN_NUM_X = 1
    MAX_NUM_X = 1
    MAX_NUM_Y = None

    NUM_Y = 1
    HIDDEN_SIZE = 256 

    UNI_LOW_FREQ_THRESHOLD = 10

    PG_DICT_SIZE = 60000 # dict for acl17 paper: pointer-generator
    
    W_UNK = "<unk>"
    W_BOS = "<bos>"
    W_EOS = "<eos>"
    W_PAD = "<pad>"
    W_LS = "<s>"
    W_RS = "</s>"

class SOConfigs():
    
    cc = CommonConfigs("so")
   
    CELL = "gru" # "lstm" # gru or lstm
    CUDA = True
    COPY = True
    COVERAGE = True
    BI_RNN = True
    BEAM_SEARCH = True
    BEAM_SIZE = 5 
    # AVG_NLL = True
    AVG_NLL = False
    NORM_CLIP = 2
    if not AVG_NLL:
        NORM_CLIP = 5
    LR = 0.15 

    DIM_X = 100 
    DIM_Y = DIM_X

    MIN_LEN_X = 16
    MIN_LEN_Y = 4 
    MAX_LEN_X = 128 
    MAX_LEN_Y = 64 
    MIN_NUM_X = 1
    MAX_NUM_X = 1
    MAX_NUM_Y = None

    NUM_Y = 1
    HIDDEN_SIZE = 256 

    UNI_LOW_FREQ_THRESHOLD = 10

    PG_DICT_SIZE = 50000 # dict for acl17 paper: pointer-generator
    
    W_UNK = "<unk>"
    W_BOS = "<bos>"
    W_EOS = "<eos>"
    W_PAD = "<pad>"
    W_LS = "<s>"
    W_RS = "</s>"


