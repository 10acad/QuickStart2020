import os, sys
#import pandas as pd
#import numpy as np
from datetime import datetime


class tv1():
    def __init__(self):
        self.gen_dirs()
    
    def gen_dirs(self):
        os.makedirs('doc',exist_ok=True)
        os.makedirs('data',exist_ok=True)
        os.makedirs('script',exist_ok=True)
        os.makedirs('notebook',exist_ok=True)

    def gen_readme(self):
        r = f'''        
        #Week Number: {self.week_number} 

        #Focus Area:
         * The focus area of this week is {self.week_topic}
        '''
        
if __name__ == '__main__':
    _ = tv1()

