db/write_batch.d db/write_batch.o: db/write_batch.cc \
 include/leveldb/write_batch.h include/leveldb/status.h \
 include/leveldb/slice.h include/leveldb/env.h \
 include/leveldb/perf_count.h include/leveldb/db.h \
 include/leveldb/iterator.h include/leveldb/options.h db/dbformat.h \
 include/leveldb/comparator.h include/leveldb/filter_policy.h \
 include/leveldb/table_builder.h util/coding.h port/port.h \
 include/leveldb/ldb_config.h port/port_posix.h port/atomic_pointer.h \
 util/logging.h db/memtable.h db/skiplist.h util/arena.h util/random.h \
 db/write_batch_internal.h
db/write_batch.o: db/write_batch.d
