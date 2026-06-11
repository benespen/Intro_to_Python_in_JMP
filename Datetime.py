import jmp
from datetime import datetime
dt = jmp.open(jmp.SAMPLE_DATA + "Big Class.jmp")
dt.new_column('birthday', jmp.DataType.Numeric)
dt['birthday'].format = "m/d/y h:m:s"
dt['birthday'][2] = datetime.now()
#https://community.jmp.com/t5/JMPer-Cable/Going-further-with-Python-in-JMP-19/ba-p/898522