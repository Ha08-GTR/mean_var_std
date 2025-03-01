import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(lst).reshape(3, 3)
    
    mean = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean()]
    variance = [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var()]
    std_dev = [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std()]
    max_val = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max()]
    min_val = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min()]
    sum_val = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum()]
    
    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
    
    return result