import numpy as np

class data_set_nn():
    def __init__(self,setX,set_y):
        self._dataX = setX
        self._dataY = set_y
        self._batch_index = 0
        self._dataX_length = len(setX)

    def get_next_batch(self,size=100):
        # _batch_start_index
        self._batch_index += size

        #batch_xs = []  # x_input_batch_return
        #batch_ys = []  # y_target_batch_return
        x_input_batch_return = []
        y_target_batch_return = []

        for i in range(self._batch_index, self._batch_index + size):
            array = [] # history x num_notes (24 x 88)
            for j in range(len(self._dataX[i%self._dataX_length])):
                for q in self._dataX[i%self._dataX_length][j]:
                    array.append(q)
            #batch_xs.append(array)
            x_input_batch_return.append(array)

        array = []
        for i in range(self._batch_index, self._batch_index+size):
            for j in self._dataY[i%self._dataX_length]:
                array.append(j)
            #batch_ys.append(array)
            y_target_batch_return.append(array)
            array=[]

        #batch_xs = np.asarray(batch_xs,dtype=np.float64)
        #batch_ys = np.asarray(batch_ys,dtype=np.float64)
        x_input_batch_return = np.asarray(x_input_batch_return, dtype=np.float64)
        y_target_batch_return = np.asarray(y_target_batch_return, dtype=np.float64)

        #return batch_xs, batch_ys
        return x_input_batch_return, y_target_batch_return