{ "targets":
  [ { "target_name": "libpng"
    , "product_prefix": ""
    , "type": "static_library"
    , "sources":
      [ "libpng-1.6.0/png.c"
      , "libpng-1.6.0/pngset.c"
      , "libpng-1.6.0/pngget.c"
      , "libpng-1.6.0/pngrutil.c"
      , "libpng-1.6.0/pngtrans.c"
      , "libpng-1.6.0/pngwutil.c"
      , "libpng-1.6.0/pngread.c"
      , "libpng-1.6.0/pngrio.c"
      , "libpng-1.6.0/pngwio.c"
      , "libpng-1.6.0/pngwrite.c"
      , "libpng-1.6.0/pngrtran.c"
      , "libpng-1.6.0/pngwtran.c"
      , "libpng-1.6.0/pngmem.c"
      , "libpng-1.6.0/pngerror.c"
      , "libpng-1.6.0/pngpread.c"
      ]
    , "include_dirs":
      [ "include/darwin"
      , "libpng-1.6.0"
      , "src/darwin"
      ]
    , "direct_dependent_settings":
      { "include_dirs":
        [ "include/all"
        , "include/darwin"
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
      ]
    }

  , { "target_name": "pngtest"
    , "type": "executable"
    , "sources": ["libpng-1.6.0/pngtest.c"]
    , "dependencies": ["libpng"]
    }
  ]
}
# -*- mode: python; tab-width: 2 -*-
