# multiprocessing
This is a little script practicing basic multiprocessing in Python.

## scenario
We used to back up our data from `/data/prod` to `/data/prod_backup` daily by using `rsync -zrvh [Source-Files-Dir] [Destination]` to recursively copy files and directories. However, as the amount of data grows sharply in recent days, the former method becomes a bit inefficient since it only use one core of CPU. Thus, to improve the efficiency of our code, we decide to use multiprocessing to take advantage of the idle CPU cores and back up data parallelly.
