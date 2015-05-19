{ "targets":
  [ { "target_name": "libpng"
    , "product_prefix": ""
    , "type": "static_library"
    , "sources":
      [ "libpng-1.6.17/png.c"
      , "libpng-1.6.17/pngset.c"
      , "libpng-1.6.17/pngget.c"
      , "libpng-1.6.17/pngrutil.c"
      , "libpng-1.6.17/pngtrans.c"
      , "libpng-1.6.17/pngwutil.c"
      , "libpng-1.6.17/pngread.c"
      , "libpng-1.6.17/pngrio.c"
      , "libpng-1.6.17/pngwio.c"
      , "libpng-1.6.17/pngwrite.c"
      , "libpng-1.6.17/pngrtran.c"
      , "libpng-1.6.17/pngwtran.c"
      , "libpng-1.6.17/pngmem.c"
      , "libpng-1.6.17/pngerror.c"
      , "libpng-1.6.17/pngpread.c"
      ]
    , "include_dirs":
      [ "include/darwin"
      , "include/linux"
      , "libpng-1.6.17"
      , "src/darwin"
      , "src/linux"
      ]
    , "direct_dependent_settings":
      { "include_dirs":
        [ "include/all"
        , "include/darwin"
        , "include/linux"
        ]
      }
    , "link_settings":
      { "libraries":
        [ "-lz"
        , "-lm"
        ]
      }
    , "conditions":
      [ [ "OS != 'mac'"
        , { "include_dirs!":
            [ "include/darwin"
            , "src/darwin"
            ]
          , "direct_dependent_settings":
            { "include_dirs!": ["include/darwin"]
            }
          }
        ]
      , [ "OS != 'linux'"
        , { "include_dirs!":
            [ "include/linux"
            , "src/linux"
            ]
          , "direct_dependent_settings":
            { "include_dirs!": ["include/linux"]
            }
          }
        ]
      ]
    }

  , { "target_name": "pngtest"
    , "type": "executable"
    , "sources": ["libpng-1.6.17/pngtest.c"]
    , "dependencies": ["libpng"]
    }
  ]
}
# -*- mode: python; tab-width: 2 -*-
