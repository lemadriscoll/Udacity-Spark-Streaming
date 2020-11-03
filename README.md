# Udacity-Spark-Streaming

Screenshots are above in file form and below shown, along with the required questions. Other logs/screenshots are above.

## Screenshot of sample kafka console output:

![](https://github.com/lemadriscoll/Udacity-Spark-Streaming/blob/main/consoleoutput.png)


## Screenshot after executing Spark job:

![](https://github.com/lemadriscoll/Udacity-Spark-Streaming/blob/main/agg_counter.png)

## Screenshot of Spark Streaming UI:
![](https://github.com/lemadriscoll/Udacity-Spark-Streaming/blob/main/sparkjobs.png)

## How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
Checking maxRatePerPartition and maxOffsetPerTrigger at 200 and 100 did not appear to make a significant difference in speed/throughput/latency, likely because of the dataset size. However, there are clear benefits to not making the max too large. When I increased these into the 1000s, there was a clear slowdown. It is best to keep the batches reasonable.

## What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

parallelism at 100, maxRatePerPartition at 200, and maxOffsetPerTrigger worked well. There are tipping points on each of these where performance dipped, which tells me that it is important to carefully choose and set these parameters rather than allowing them to default.
