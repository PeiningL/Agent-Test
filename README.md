# Agent-Test
Technical test 

- Technologies used

  Python2.7

  Compile with python 2.7 or python 2.x
  Execute by using command "python2.7(or python) main.py" in terminal to compile and launch the program.
  Or Execute by using IDE.

  necessary modules：
  xlrd, xlwt, numpy, matplotlib, PIL, PIL.ImageTk,  matplotlib
  
  Remark:
  matplotlib.use('Agg') matplotlib.pyplot as plt is necessary for Mac OS to avoid error about matplotlib during compiling
  

- Description
  
  I chose language Python who is easy for data handling to accomplish the test. For importing data original, we can convert a XLSX file to CSV file or load a CSV file directly by the small program. Accroding to algorithm below, the program is going to update the data automatically and to show 2 figures(pie and bar) for displaying statistic of data output. These figures will be saved as PNG file automatically with name in the format: pie(or bar)_nbYears_BrandFactor in the folder auto-created with the same name of original data file. We are able to export the new data as a CSV file.

  Input: Brand Factor between 0.1 and 2.9

  Algorithm:

  Run for 15 Years        
      Every Year: Increment Age   
      If Auto Renew - Maintain Breed  
      Else No Auto-Renew: 
          Affinity =  Payment_at_Purchase/Attribute_Price + (2 * Attribute_Promotions * Inertia_for_Switch)
          If Breed_C  Switch to Breed_NC if Affinity < (Social_Grade * Attribute_Brand)
          If Breed_NC Switch to Breed_C if Affinity < (Social_Grade * Attribute_Brand * Brand_Factor)

  Output: 

  Breed_C Lost (Switched to Breed_NC) 
  Breed_C Gained (Switch from Breed_NC)   
  Breed_C Regained (Switched to NC, then back to C)
  
  It's evident that value of Affinity unchange for every year and there are only 2 types of Agent_Breed. So I introduced
  an attribute for counting times of change:
  In the case auto_renew = 0:
  - If agent whose Breed_original == Breed_C 
      If times_change is impair then nbLost++
      Else times_change is pair then nbRegained++
    Else 
      If times_change is impair then nbGained++
