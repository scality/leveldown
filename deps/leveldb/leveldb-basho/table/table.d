table/table.d table/table.o: table/table.cc include/leveldb/table.h \
 include/leveldb/iterator.h include/leveldb/slice.h \
 include/leveldb/status.h include/leveldb/perf_count.h \
 include/leveldb/cache.h include/leveldb/comparator.h \
 include/leveldb/env.h include/leveldb/filter_policy.h \
 include/leveldb/options.h table/block.h table/filter_block.h util/hash.h \
 table/format.h include/leveldb/table_builder.h \
 table/two_level_iterator.h util/coding.h port/port.h \
 include/leveldb/ldb_config.h port/port_posix.h port/atomic_pointer.h
table/table.o: table/table.d
