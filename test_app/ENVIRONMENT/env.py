import os
import dotenv



file_path = os.path.join(os.getcwd(), ".env")
env = dotenv.dotenv_values("../test_app/ENVIRONMENT/.env")



class Env():
    
    def __init__(self, envr=env):
        self.envr = envr
        self.vars()
        
    def vars(self):
        for k, v in self.envr.items():
            self.__setattr__(k, v)
