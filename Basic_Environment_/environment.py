

import numpy as np
from typing import Optional




class Environment:
    def __init__(self,
                 size_of_env: Optional[int] = None,

        ):
        self._size_of_env_ = size_of_env

        self.maze = np.zeros(())