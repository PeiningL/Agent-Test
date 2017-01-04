# Agent-Test
Technical test 

- Technologies 

  Python2.7

  Compile with python 2.7 or python 2.x
  Execute by using command "python2.7(or python) main.py" in terminal to compile and launch the program.
  Or Execute by using IDE.

  necessary modules：
  xlrd, xlwt, numpy, matplotlib, PIL, PIL.ImageTk,  matplotlib
  
  Remark:
  matplotlib.use('Agg') matplotlib.pyplot as plt is necessary for Mac OS to avoid error about matplotlib during compiling
  

- Description

  Input: Brand Factor between 0.1 and 2.9

  Algorithme:

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
