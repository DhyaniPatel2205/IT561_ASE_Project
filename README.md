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
Note: Use *deactivate* to deactivate the virtual environment

Step 3: Install Requirements
- python -m pip install -r req.txt

Step 4: Edit Files
- cd source_code
- Change 2 paths in *bleu.py*  
&nbsp;&nbsp;&nbsp;&nbsp;- bleu("/content/drive/MyDrive/dhyani_code2que_new/source_code/so/result/ground_truth/", "/content/drive/MyDrive/dhyani_code2que_new/source_code/so/result/summary/", smooth=True)
- Change all the paths and batch size (as per need) in *configs.py*
- Change 4 data paths in *data_prepare.py*  
&nbsp;&nbsp;&nbsp;&nbsp;- *src_path* (train)  
&nbsp;&nbsp;&nbsp;&nbsp;- *tgt_path* (train)  
&nbsp;&nbsp;&nbsp;&nbsp;- *src_path* (test)  
&nbsp;&nbsp;&nbsp;&nbsp;- *tgt_path* (test)  
*Note: You can also uncomment data validation part*  
- Change 4 paths in *evaluation.py*  
&nbsp;&nbsp;&nbsp;&nbsp;- open file path in *write_review* function  
&nbsp;&nbsp;&nbsp;&nbsp;- *hypo_path* in *main* function  
&nbsp;&nbsp;&nbsp;&nbsp;- *ref_path* in *main* function  
&nbsp;&nbsp;&nbsp;&nbsp;- *eval_path* in *main* function  
- Change True/False and epochs (as per need) in main.py  
&nbsp;&nbsp;&nbsp;&nbsp;- For training:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- options["is_debugging"] = False  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- options["is_predicting"] = False  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- options["model_selection"] = False  
&nbsp;&nbsp;&nbsp;&nbsp;- For testing:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- options["is_debugging"] = False  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- options["is_predicting"] = True  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- options["model_selection"] = True  
&nbsp;&nbsp;&nbsp;&nbsp;- For testing:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- options["is_debugging"] = False  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- options["is_predicting"] = True  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- options["model_selection"] = False  

Step 6: Run Code  
(1) Training
- Initially: options["is_debugging"] = False, options["is_predicting"] = False, options["model_selection"] = False
- python data_prepare.py
- python3 main.py    
(2) Tuning
- Modify: Initially: options["is_debugging"] = False, options["is_predicting"] = True, options["model_selection"] = True
- bash tuning.sh    
(3) Testing
- Modify: options["is_debugging"] = False, options["is_predicting"] = True, options["model_selection"] = False
- python main.py *your-best-model-name* (say cnndm.s2s.gpu4.epoch7.1)
- cd so/result
- run ROUGE myROUGE_Config.xml C