from ydata_profiling import ProfileReport
import pandas as pd
df=pd.read_csv("HRdata.csv")
Pf=ProfileReport(df,title="EDA report",explorative=True)
Pf.to_file("EDA report.html") 






