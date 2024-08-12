# psn-aiauto-test-anwers

To calculate the total device downtime from the given CSV data, the following are the steps:

Filling Null and Empty Values: Replace Null or empty values with the last non-null value before the value.

Calculating Downtime Interval: For each period where the device value is 1 (off), calculate the time difference between consecutive timestamps.

Sum the Downtime Interval: Convert these intervals from milliseconds to seconds and sum them up to get the total downtime.

The following is a detailed step-by-step guide.

In the given example:
data_test_1 = [
    (1704042000000, 0),
    (1704042026000, 1),
    (1704042035000, 1),
    (1704042037000, 0),
    (1704042059000, 1),
    (1704042060000, 1)
]

Inactive Period Identification

From the data, the inactive period starts when the value 1 appears and ends when the value 0 appears.

Period 1: Starts from timestamp 1704042026000 to timestamp 1704042037000.
Period 2: Starts from timestamp 1704042059000 to timestamp 1704042060000.
Calculating the Duration of Each Period of Inactivity

Period 1:

Start: 1704042026000
End: 1704042037000
Duration 1704042037000 - 1704042026000 = 11000 ms

Period 2:
Start 1704042059000
End: 1704042060000
Duration 1704042060000 - 1704042059000 = 1000 ms

Sum the Duration

Convert from milliseconds to seconds (by dividing by 1000) and sum:

Period 1: 11000 ms / 1000 = 11 seconds
Period 2: 1000 ms / 1000 = 1 second
Total downtime in seconds: 11 seconds + 1 second = 12 seconds

# I used python programming language to calculate how long the device was off referenced by the csv data (in seconds). And I got the total downtime for 58310.00 seconds
