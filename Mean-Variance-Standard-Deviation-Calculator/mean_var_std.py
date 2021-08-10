import numpy as np

def calculate(list):
    if (len(list) != 9):
      raise ValueError("List must contain nine numbers.")
    ls = np.array(list)

    # axis 1 = rows && axis2 = columns && flattened = full matrix
    
    maxis1 = [ls[[0,3,6]].mean(),ls[[1,4,7]].mean(),ls[[2,5,8]].mean()]
    maxis2 = [ls[[0,1,2]].mean(),ls[[3,4,5]].mean(),ls[[6,7,8]].mean()]
    mflattened = ls.mean()

    vaxis1 = [ls[[0,3,6]].var(),ls[[1,4,7]].var(),ls[[2,5,8]].var()]
    vaxis2 = [ls[[0,1,2]].var(),ls[[3,4,5]].var(),ls[[6,7,8]].var()]
    vflattened = ls.var()

    stdaxis1 = [ls[[0,3,6]].std(),ls[[1,4,7]].std(),ls[[2,5,8]].std()]
    stdaxis2 = [ls[[0,1,2]].std(),ls[[3,4,5]].std(),ls[[6,7,8]].std()]
    stdflattened = ls.std()

    MAaxis1 = [ls[[0,3,6]].max(),ls[[1,4,7]].max(),ls[[2,5,8]].max()]
    MAaxis2 = [ls[[0,1,2]].max(),ls[[3,4,5]].max(),ls[[6,7,8]].max()]
    MAflattened = ls.max()
    
    MNaxis1 = [ls[[0,3,6]].min(),ls[[1,4,7]].min(),ls[[2,5,8]].min()]
    MNaxis2 = [ls[[0,1,2]].min(),ls[[3,4,5]].min(),ls[[6,7,8]].min()]
    MNflattened = ls.min()

    SUMaxis1 = [ls[[0,3,6]].sum(),ls[[1,4,7]].sum(),ls[[2,5,8]].sum()]
    SUMaxis2 = [ls[[0,1,2]].sum(),ls[[3,4,5]].sum(),ls[[6,7,8]].sum()]
    SUMflattened = ls.sum()
    
    calculations =  {
  'mean': [maxis1, maxis2, mflattened],
  'variance': [vaxis1, vaxis2, vflattened],
  'standard deviation': [stdaxis1, stdaxis2, stdflattened],
  'max': [MAaxis1, MAaxis2, MAflattened],
  'min': [MNaxis1, MNaxis2, MNflattened],
  'sum': [SUMaxis1, SUMaxis2, SUMflattened]
}


    return calculations