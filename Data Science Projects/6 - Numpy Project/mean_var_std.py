import numpy as np
import builtins

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  else:
    work_array = np.array(list).reshape(3,3)
    
    mean_row = np.mean(work_array, axis=0)
    mean_col = np.mean(work_array, axis=1)
    mean_flat = np.mean(work_array)
    means = [builtins.list(mean_row), builtins.list(mean_col), mean_flat]

    var_row = np.var(work_array, axis=0)
    var_col = np.var(work_array, axis=1)
    var_flat = np.var(work_array)
    vars = [builtins.list(var_row), builtins.list(var_col), var_flat]

    stdev_row = np.std(work_array, axis=0)
    stdev_col = np.std(work_array, axis=1)
    stdev_flat = np.std(work_array)
    stdevs = [builtins.list(stdev_row), builtins.list(stdev_col), stdev_flat]

    max_row = np.max(work_array, axis=0)
    max_col = np.max(work_array, axis=1)
    max_flat = np.max(work_array)
    maxs = [builtins.list(max_row), builtins.list(max_col), max_flat]

    min_row = np.min(work_array, axis=0)
    min_col = np.min(work_array, axis=1)
    min_flat = np.min(work_array)
    mins = [builtins.list(min_row), builtins.list(min_col), min_flat]

    sum_row = np.sum(work_array, axis=0) 
    sum_col = np.sum(work_array, axis=1)
    sum_flat = np.sum(work_array)
    sums = [builtins.list(sum_row), builtins.list(sum_col), sum_flat]

    calculations = {'mean': means,
                    'variance': vars,
                    'standard deviation': stdevs,
                    'max': maxs,
                    'min': mins,
                    'sum': sums
                     }
    
    print(calculations)
  return calculations
