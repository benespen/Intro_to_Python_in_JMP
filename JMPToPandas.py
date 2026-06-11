import jmp
import pandas as pd

dt = jmp.open(jmp.SAMPLE_DATA + "Big Class.jmp")
pandas_df = pd.api.interchange.from_dataframe(dt)
print(pandas_df)
#https://community.jmp.com/t5/JMPer-Cable/Going-further-with-Python-in-JMP-19/ba-p/898522