import random
import time

def stop_and_wait_arq(total_frames=5, loss_prob=0.3):
    for frame in range(total_frames):
        print(f"Sending Frame {frame}")
        # Simulate random frame loss
        if random.random() < loss_prob:
            print(f"Frame {frame} lost, retransmitting ...")
            time.sleep(1)
            print(f"Resending Frame {frame}")
        print(f"ACK {frame} received\n")
        time.sleep(0.5)

stop_and_wait_arq()
