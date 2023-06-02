import torch
import threading
import time

from seq2seq.models.gnmt import GNMT

def gnmt_loop(batchsize, train, local_rank, barriers, tid):

    barriers[0].wait()

    model_config = {

        "hidden_size": 1024,
        "vocab_size": 32320,
        "num_layers": 4,
        "dropout": 0.2,
        "batch_first": False,
        "share_embedding": True
    }

    print("-------------- thread id:  ", threading.get_native_id())

    input0 = torch.ones([50, batchsize]).to(torch.int64).to(0)
    input1 = torch.ones([batchsize]).to(torch.int64).to(0)
    input2 = torch.ones([50, batchsize]).to(torch.int64).to(0)

    model = GNMT(**model_config).to(local_rank)

    if train:
        model.train()
    else:
        model.eval()

    for i in range(1):
        print("Start epoch: ", i)

        start = time.time()
        start_iter = time.time()
        batch_idx = 0
        torch.cuda.synchronize()

        while batch_idx < 1:
            print(f"submit!, batch_idx is {batch_idx}")
            torch.cuda.profiler.cudart().cudaProfilerStart()

            if train:
                output = model(input0, input1, input2)
            else:
                with torch.no_grad():
                    output = model(input0, input1, input2)

            torch.cuda.profiler.cudart().cudaProfilerStop()

            #print(output.shape)
            batch_idx += 1

            if batch_idx < 1:
                    barriers[0].wait()

    print("Epoch took: ", time.time()-start)