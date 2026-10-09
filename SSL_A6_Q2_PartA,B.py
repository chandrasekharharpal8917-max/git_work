import torch
import time

def naive_matmul(A, B):
    n = len(A)
    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def measure_time(func, *args, repetitions=5):
    # (b) Discard an initial warm-up run
    _ = func(*args)
    
    times = []
    # (a) Run several repetitions
    for _ in range(repetitions):
        start = time.perf_counter()
        _ = func(*args)
        end = time.perf_counter()
        times.append(end - start)
        
    # (c) & (d) Calculate average and minimum execution time
    avg_time = sum(times) / len(times)
    min_time = min(times)
    return avg_time, min_time

matrix_sizes = [50, 100, 200, 400, 800, 1200]
naive_sizes = [50, 100, 200] # Kept small because naive Python is very slow

# Open files to store results: matrix_size time
with open("pytorch_times.dat", "w") as f_pt, open("naive_times.dat", "w") as f_nv:
    f_pt.write("# Matrix_Size Avg_Time Min_Time\n")
    f_nv.write("# Matrix_Size Avg_Time Min_Time\n")
    
    for n in matrix_sizes:
        # Part A: Generate random matrices
        A = torch.randn(n, n)
        B = torch.randn(n, n)
        
        # PyTorch Timing
        pt_avg, pt_min = measure_time(lambda: A @ B)
        f_pt.write(f"{n} {pt_avg:.6f} {pt_min:.6f}\n")
        
        # Part B: Naive Python Timing (only for smaller n)
        if n in naive_sizes:
            A_list = A.tolist()
            B_list = B.tolist()
            nv_avg, nv_min = measure_time(naive_matmul, A_list, B_list, repetitions=3)
            f_nv.write(f"{n} {nv_avg:.6f} {nv_min:.6f}\n")
            print(f"Size {n}: PyTorch Avg = {pt_avg:.5f}s | Naive Avg = {nv_avg:.5f}s")