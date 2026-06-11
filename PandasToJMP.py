import jmp
import pandas as pd
import numpy as np

pandas_df = pd.DataFrame(
	{
		"A": 1.0,
		"B": pd.Timestamp("20130102"),
		"C": np.array([3] *4, dtype="int32"),
		"D": pd.Categorical(["test", "train", "test", "train"]),
		"E": "foo"
	}
)

print(pandas_df)

dt = jmp.from_dataframe(pandas_df)
print(dt)

#https://community.jmp.com/t5/JMPer-Cable/Going-further-with-Python-in-JMP-19/ba-p/898522