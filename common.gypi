{
    'defines': [
        'NN_HAVE_GCC',
        'NN_HAVE_PIPE',
        'NN_HAVE_POLL',
        'NN_USE_IFADDRS',
        'NN_HAVE_SOCKETPAIR',
        'NN_HAVE_SEMAPHORE',
        'NN_USE_PIPE',
    ],
    'direct_dependent_settings': {
        'defines': [
            'NN_HAVE_GCC',
            'NN_HAVE_PIPE',
            'NN_HAVE_POLL',
            'NN_USE_IFADDRS',
            'NN_HAVE_SOCKETPAIR',
            'NN_HAVE_SEMAPHORE',
            'NN_USE_PIPE',
        ],
        'include_dirs': [
          'deps/nanomsg/src',
        ],
    }
}
