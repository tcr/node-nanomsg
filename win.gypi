{
    # compiler settings to build the nanomsg library
    'defines': [
    ],
    'direct_dependent_settings': {
        # build nanomsg hub with same compiler flags as the library
        'defines': [
        ],
        'include_dirs': [
          'deps/nanomsg/src',
        ],
    },
    'target_defaults': {
        'default_configuration': 'Debug',
        'configurations': {
          'Debug': {
            'defines': [ 'DEBUG', '_DEBUG' ],
            'msvs_settings': {
              'VCCLCompilerTool': {
                'RuntimeLibrary': 0, # shared debug
              },
            },
          },
          'Release': {
            'defines': [ 'NDEBUG' ],
            'msvs_settings': {
              'VCCLCompilerTool': {
                'RuntimeLibrary': 1, # shared release
              },
            },
          }
        },
        'msvs_settings': {
          'VCLinkerTool': {
            'GenerateDebugInformation': 'true',
          },
        },
        'include_dirs': [
          '.'
        ],
        'defines': [
        ],
        'conditions': [
          ['OS=="win"', {
            'defines': [
              '_WIN32'
            ]
          }]
        ],
      },
}
