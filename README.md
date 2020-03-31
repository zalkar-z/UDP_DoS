# UDP DoS
Denial of Service implementation using UDP

## Trial #1: 6 client machines vs a single server

- Server listens on port:9000 from all IPs, receives a message and returns it by adding an exclamation point to it.

- Clients send packages endlessly using `while True` statement and print both sent and received packages.

- Package was a simple `hello` message, nothing fancy or big to process.

- Using all bots in my possession, I was able to get Victim's CPU read 25% load from 1% before the flood.

**Next steps:**

- Bots: send BIG packages, don't print
- Tracker client: implement a timer to measure the UDP connection latency.


