import random
import time
from argparse import ArgumentParser

import requests

inputs = [
    "Hello, how are you?",
    "What up dig dog?",
    "You are a killer!",
    "Live a good life",
    "Life is great",
    "Chilling on a roof",
    "Love you",
    "Mox is cute",
    "You are my enemy",
    "Change is required",
    "Love the life",
]

# Uncomment to use for Locust

# from locust import HttpUser, task

# class QuickstartUser(HttpUser):
#     @task
#     def predict(self):
#         with self.client.get(f"/predict/{random.choice(inputs)}") as response:
#             if response.status_code != 200:
#                 response.failure("Could not return response")


def benchmark(*urls):
    for isvc in urls:
        times = []
        count_s = count_f = 0
        for _ in range(1000):
            start = time.time()
            res = requests.get(f"{isvc}/predict/{random.choice(inputs)}")
            if res.status_code == 200:
                times.append(time.time() - start)
                count_s += 1
            else:
                print(f"Bad status code from {isvc}: {res.status_code}")
                count_f += 1

        print(f"Average Latency for {isvc}: {sum(times)/len(times)}")
        print(f"Successes for {isvc}: {count_s}")
        print(f"Failures for {isvc}: {count_f}")


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--url", help="InferenceService URL", required=True)

    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    benchmark(args.url)


if __name__ == "__main__":
    main()
