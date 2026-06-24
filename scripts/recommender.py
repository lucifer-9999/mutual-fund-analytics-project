import pandas as pd

df=pd.read_csv(

"data/processed/scheme_performance_cleaned.csv"

)

risk=input(

"Risk Appetite (Low/Moderate/High): "

)

rec=df[

df["risk_grade"]

.str.contains(

risk,

case=False

)

]

rec=rec.sort_values(

"sharpe_ratio",

ascending=False

).head(3)

print(rec[
[
"scheme_name",

"risk_grade",

"sharpe_ratio"

]
])