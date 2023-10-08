

import numpy as np
from typing import Optional

np.set_printoptions(suppress=True)


class Environment:
    def __init__(self,
                 size_of_env = None,
                 destination: Optional[int] = None,
                 add_obstacle: Optional[bool] = False,

        ):
        self._size_of_env_ = size_of_env
        self.maze = np.zeros((self._size_of_env_,self._size_of_env_))
        self._robot_position = (0,0)
        if destination is None:
            self._destination_ = (self._size_of_env_-1,self._size_of_env_-1)
        else:
            if destination >= size_of_env:
                raise ValueError("The destination should be within the environment size")
            else:
                self._destination_ = (destination-1,destination-1)

        self.maze[self._robot_position[0],self._robot_position[1]] = 2
        self.maze[self._destination_[0],self._destination_[1]] = -99999999



    @property
    def show_environment(self):
        return self.maze


    def reached_destination(self):
        if self._robot_position_ == self._destination_:
            return True
        else:
            return False
        

    def give_reward(self):
        if self.reached_destination() == True:
            return 1
        else:
            return 0
        
        
    

    



ff = Environment(size_of_env=9)
x = ff.show_environment
print(x)





