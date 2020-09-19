#!/usr/bin/env python3

import subprocess
from multiprocessing import Pool
import os

src = "../data/prod/"
dest = "../data/prod_backup/"
tasks = []

# Synchronizing the directory structure only from src to dest
subprocess.call(["rsync", "-av", '-f+ */', '-f- *', src, dest])


def run(task):
  # Do something with task here
  task_s = task
  task_d = task.replace(src,dest)
  # Synchronizing files
  subprocess.call(["rsync", "-zvh", task_s, task_d])


if __name__ == "__main__":
  # Generates the file names in the src directory
  for root, dirs, files in os.walk(src):
    for name in files:
      tasks.append(os.path.join(root, name))

  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))

  # Start each task within the pool
  p.map(run, tasks)


