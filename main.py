# Using VS Code
# In the terminal >>
                    #pip install pandas
                    #pip install pandas-profiling


import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('RCOM.csv')
print(df)
# if DLL load failed error occurs>> inside terminal>>
                                #pip uninstall pandas
                                #pip install pandas==1.0.1


# >>>>>>>>>>>>>>>>     Generate a Report     >>>>>>>>>>>>>>>>>>>>>>>>>>>>
profile = ProfileReport(df)
# if the dataset is very large & you want to minimise the report, instead of the above line, use---->>
#profile = ProfileReport(df, minimal = True)

profile.to_file(output_file = 'RCOM_Report.html')
#Now the .html file will be created wait for some time and then view it with live server