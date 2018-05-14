#ifndef __STATUS_H
#define __STATUS_H
//来自server.h
struct rdbStatus {

    long long stat_expiredkeys;     /* Number of expired keys */
    long long stat_keyspace_hits;   /* Number of successful lookups of keys */
    long long stat_keyspace_misses; /* Number of failed lookups of keys */
};

extern struct rdbStatus status;
#endif
