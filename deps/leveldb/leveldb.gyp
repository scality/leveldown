{'targets': [{
    'target_name': 'leveldb'
  , 'variables': {
        'ldbversion': 'rocksdb'
    }
  , 'type': 'static_library'
		# Overcomes an issue with the linker and thin .a files on SmartOS
  , 'standalone_static_library': 1
  , 'dependencies': [
        '../snappy/snappy.gyp:snappy'
    ]
  , 'direct_dependent_settings': {
        'include_dirs': [
            'leveldb-<(ldbversion)/include/'
          , 'leveldb-<(ldbversion)/port/'
          , 'leveldb-<(ldbversion)/util'
          , 'leveldb-<(ldbversion)/'
        ]
    }
  , 'defines': [
        'SNAPPY=1'
    ]
  , 'include_dirs': [
        'leveldb-<(ldbversion)/'
      , 'leveldb-<(ldbversion)/include/'
    ]
  , 'conditions': [
        ['OS == "win"', {
            'conditions': [
                ['MSVS_VERSION != "2015" and MSVS_VERSION != "2013"', {
                     'include_dirs': [ 'leveldb-<(ldbversion)/port/win' ]
                }]
            ],
            'include_dirs': [
                'port-libuv/'
            ]
          , 'defines': [
                'LEVELDB_PLATFORM_UV=1'
              , 'NOMINMAX=1'
              , '_HAS_EXCEPTIONS=0'
            ]
          , 'sources': [
                'port-libuv/port_uv.cc'
              , 'port-libuv/env_win.cc'
              , 'port-libuv/win_logger.cc'
            ]
          , 'msvs_settings': {
                'VCCLCompilerTool': {
                    'RuntimeTypeInfo': 'false'
                  , 'EnableFunctionLevelLinking': 'true'
                  , 'ExceptionHandling': '2'
                  , 'DisableSpecificWarnings': [ '4355', '4530' ,'4267', '4244' ]
                }
            }
        }, { # OS != "win"
            'sources': [
                'leveldb-<(ldbversion)/port/port_posix.cc'
              , 'leveldb-<(ldbversion)/port/port_posix.h'
              , 'leveldb-<(ldbversion)/util/env_posix.cc'
            ]
          , 'defines': [
                'LEVELDB_PLATFORM_POSIX=1'
            ]
          , 'ccflags': [
                '-fno-builtin-memcmp'
              , '-fPIC'
            ]
          , 'cflags': [ '-std=c++0x' ]
          , 'cflags!': [ '-fno-tree-vrp' ]
        }]
      , ['OS != "win"' and 'OS != "freebsd"', {
            'cflags': [
                '-Wno-sign-compare'
              , '-Wno-unused-but-set-variable'
            ]
        }]
      , ['OS == "linux"', {
            'defines': [
                'OS_LINUX=1'
            ]
          , 'libraries': [
                '-lpthread'
            ]
          , 'ccflags': [
                '-pthread'
            ]
        }]
      , ['OS == "freebsd"', {
            'defines': [
                'OS_FREEBSD=1'
              , '_REENTRANT=1'
            ]
          , 'libraries': [
                '-lpthread'
            ]
          , 'ccflags': [
                '-pthread'
            ]
          , 'cflags': [
                '-Wno-sign-compare'
            ]
        }]
      , ['OS == "solaris"', {
            'defines': [
                'OS_SOLARIS=1'
              , '_REENTRANT=1'
            ]
          , 'libraries': [
                '-lrt'
              , '-lpthread'
            ]
          , 'ccflags': [
                '-pthread'
            ]
        }]
      , ['OS == "mac"', {
            'defines': [
                'OS_MACOSX=1'
            ]
          , 'libraries': []
          , 'ccflags': []
          , 'xcode_settings': {
                'WARNING_CFLAGS': [
                    '-Wno-sign-compare'
                  , '-Wno-unused-variable'
                  , '-Wno-unused-function'
                ]
            }
        }]
    ]
  , 'sources': [
        'leveldb-<(ldbversion)/db/builder.cc'
      , 'leveldb-<(ldbversion)/db/c.cc'
      , 'leveldb-<(ldbversion)/db/c_test.c'
      , 'leveldb-<(ldbversion)/db/db_bench.cc'
      , 'leveldb-<(ldbversion)/db/dbformat.cc'
      , 'leveldb-<(ldbversion)/db/db_impl.cc'
      , 'leveldb-<(ldbversion)/db/db_iter.cc'
      , 'leveldb-<(ldbversion)/db/filename.cc'
      , 'leveldb-<(ldbversion)/db/log_reader.cc'
      , 'leveldb-<(ldbversion)/db/log_writer.cc'
      , 'leveldb-<(ldbversion)/db/memtable.cc'
      , 'leveldb-<(ldbversion)/db/repair.cc'
      , 'leveldb-<(ldbversion)/db/table_cache.cc'
      , 'leveldb-<(ldbversion)/db/version_edit.cc'
      , 'leveldb-<(ldbversion)/db/version_set.cc'
      , 'leveldb-<(ldbversion)/db/write_batch.cc'
      , 'leveldb-<(ldbversion)/helpers/memenv/memenv.cc'
      , 'leveldb-<(ldbversion)/port/port_posix.cc'
      , 'leveldb-<(ldbversion)/table/block.cc'
      , 'leveldb-<(ldbversion)/table/block_builder.cc'
      , 'leveldb-<(ldbversion)/table/filter_block.cc'
      , 'leveldb-<(ldbversion)/table/format.cc'
      , 'leveldb-<(ldbversion)/table/iterator.cc'
      , 'leveldb-<(ldbversion)/table/merger.cc'
      , 'leveldb-<(ldbversion)/table/table.cc'
      , 'leveldb-<(ldbversion)/table/table_builder.cc'
      , 'leveldb-<(ldbversion)/table/two_level_iterator.cc'
      , 'leveldb-<(ldbversion)/util/arena.cc'
      , 'leveldb-<(ldbversion)/util/bloom2.cc'
      , 'leveldb-<(ldbversion)/util/bloom.cc'
      , 'leveldb-<(ldbversion)/util/cache.cc'
      , 'leveldb-<(ldbversion)/util/cache2.cc'
      , 'leveldb-<(ldbversion)/util/coding.cc'
      , 'leveldb-<(ldbversion)/util/comparator.cc'
      , 'leveldb-<(ldbversion)/util/crc32c.cc'
      , 'leveldb-<(ldbversion)/util/db_list.cc'
      , 'leveldb-<(ldbversion)/util/env.cc'
      , 'leveldb-<(ldbversion)/util/env_posix.cc'
      , 'leveldb-<(ldbversion)/util/filter_policy.cc'
      , 'leveldb-<(ldbversion)/util/flexcache.cc'
      , 'leveldb-<(ldbversion)/util/hash.cc'
      , 'leveldb-<(ldbversion)/util/histogram.cc'
      , 'leveldb-<(ldbversion)/util/hot_threads.cc'
      , 'leveldb-<(ldbversion)/util/logging.cc'
      , 'leveldb-<(ldbversion)/util/lz4.c'
      , 'leveldb-<(ldbversion)/util/murmurhash.cc'
      , 'leveldb-<(ldbversion)/util/options.cc'
      , 'leveldb-<(ldbversion)/util/perf_count.cc'
      , 'leveldb-<(ldbversion)/util/random.h'
      , 'leveldb-<(ldbversion)/util/status.cc'
      , 'leveldb-<(ldbversion)/util/thread_tasks.cc'
      , 'leveldb-<(ldbversion)/util/throttle.cc'
      , 'leveldb-<(ldbversion)/tools/leveldb_main.cc'
      , 'leveldb-<(ldbversion)/tools/leveldb_repair.cc'
      , 'leveldb-<(ldbversion)/tools/perf_dump.cc'
      , 'leveldb-<(ldbversion)/tools/sst_rewrite.cc'
      , 'leveldb-<(ldbversion)/tools/sst_scan.cc'
      , 'leveldb-<(ldbversion)/stubs/warming_stub.cc'
    ]
}]}
