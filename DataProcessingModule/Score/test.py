from score import Preprocessing
global preprocessor


preprocessor = Preprocessing()
df = preprocessor.load_excel('.//Test//titanic.xlsx')

import pdb
pdb.set_trace()



