#ifndef __STATUS_H
#define __STATUS_H
struct rdbStatus {
    long long stat_keyspace_hits;   /* Number of successful lookups of keys */
};

extern struct rdbStatus status;
#endif
