# Redis

![redis logo](https://upload.wikimedia.org/wikipedia/fr/6/6b/Redis_Logo.svg)

Redis (Remote Dictionary Server) is an open-source, in-memory data structure store used as a database, cache, and message broker. It is known for its high performance, flexibility, and support for various data structures.

## Features
- **In-Memory Storage**: Provides ultra-fast data access by storing data in memory.
- **Data Structures**: Supports strings, hashes, lists, sets, sorted sets, bitmaps, hyperloglogs, and streams.
- **Persistence**: Offers snapshotting (RDB) and append-only file (AOF) mechanisms.
- **Replication**: Master-slave replication for high availability.
- **Clustering**: Supports distributed clustering for scalability.
- **Pub/Sub Messaging**: Enables real-time messaging between clients.

## Installation on Ubuntu 20.04
```
sudo apt-get -y install redis-server
pip3 install redis
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Running Redis
Start the Redis server:
```
redis-server
```

Check if Redis is running:
```
redis-cli ping
```

Expected output:
```
PONG
```

## Basic Commands
```
SET key value   # Store a value
GET key         # Retrieve a value
DEL key         # Delete a key
EXISTS key      # Check if a key exists
INCR key        # Increment a value
```

## Use Cases
- Caching frequently accessed data.
- Session storage for web applications.
- Real-time analytics and leaderboard tracking.
- Message queues and pub/sub systems.

## Resources
- [Official Documentation](https://redis.io/docs)
- [GitHub Repository](https://github.com/redis/redis)

## License
Redis is released under the [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

