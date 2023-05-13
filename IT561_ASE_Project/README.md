# IT561_ASE_Project
# Team Members: Dhwani Upadhyay (202211045) and Dhyani Patel (202211056)

Step 1: Setup Data
- Download the train and test data from "https://drive.google.com/drive/folders/1RmdCW2pRTpfGvDf8DmvYfz88exXtX5sP?usp=share_link"
- The file structure should look like:

data_sample (folder)  
&nbsp;&nbsp;&nbsp;&nbsp;⤷ csharpdata (sub-folder 1)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⤷ all the 6 .txt files  
&nbsp;&nbsp;&nbsp;&nbsp;⤷ javadata (sub-folder 2)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⤷ all the 6 .txt files  
&nbsp;&nbsp;&nbsp;&nbsp;⤷ jsdata (sub-folder 3)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⤷ all the 6 .txt files  
&nbsp;&nbsp;&nbsp;&nbsp;⤷ pydata (sub-folder 4)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⤷ all the 6 .txt files  
&nbsp;&nbsp;&nbsp;&nbsp;⤷ sqldata (sub-folder 5)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⤷ all the 6 .txt files  

Step 2: Create Virtual Environment (steps given for Windows)
- python -m venv *name_of_virtual_environment*
- *name_of_virtual_environment*/Scripts/avtivate

Step 3: Install Requirements
- python -m pip install -r req.txt

Step 4: Edit Files
- Change 2 paths in *bleu.py*
-- bleu("/content/drive/MyDrive/dhyani_code2que_new/source_code/so/result/ground_truth/", "/content/drive/MyDrive/dhyani_code2que_new/source_code/so/result/summary/", smooth=True)
- Change all the paths and batch size (as per need) in *configs.py*
- Change 4 data paths in *data_prepare.py*
-- *src_path* (train)
-- *tgt_path* (train)
-- *src_path* (test)
-- *tgt_path* (test)  
*Note: You can also uncomment data validation part*
- Change 4 paths in *evaluation.py*
-- open file path in *write_review* function
-- *hypo_path* in *main* function
-- *ref_path* in *main* function
-- *eval_path* in *main* function
- Change True/False and epochs (as per need) in main.py
-- For training:
--- options["is_debugging"] = False
--- options["is_predicting"] = False
--- options["model_selection"] = False
-- For testing:
--- options["is_debugging"] = False
--- options["is_predicting"] = True
--- options["model_selection"] = True
-- For testing:
--- options["is_debugging"] = False
--- options["is_predicting"] = True
--- options["model_selection"] = False