# -*- mode: python -*-

def common(ctx):
    ctx.default_sdk = "10.6"
    ctx.default_compiler = "clang"
    ctx.load("compiler_c")
    ctx.load("core", "ext/waf-sfiera")

def options(opt):
    common(opt)

def configure(cnf):
    common(cnf)
    cnf.check(lib="z", uselib_store="libpng/system/libz")
    cnf.check(lib="m", uselib_store="libpng/system/libm")

def build(bld):
    common(bld)

    bld.stlib(
        target="libpng/libpng",
        features="universal",
        source=[
            "libpng-1.6.0/png.c",
            "libpng-1.6.0/pngset.c",
            "libpng-1.6.0/pngget.c",
            "libpng-1.6.0/pngrutil.c",
            "libpng-1.6.0/pngtrans.c",
            "libpng-1.6.0/pngwutil.c",
            "libpng-1.6.0/pngread.c",
            "libpng-1.6.0/pngrio.c",
            "libpng-1.6.0/pngwio.c",
            "libpng-1.6.0/pngwrite.c",
            "libpng-1.6.0/pngrtran.c",
            "libpng-1.6.0/pngwtran.c",
            "libpng-1.6.0/pngmem.c",
            "libpng-1.6.0/pngerror.c",
            "libpng-1.6.0/pngpread.c",
        ],
        cflags="-Wall -Werror",
        includes="libpng-1.6.0",
        export_includes="include/all",
        use=[
            "libpng/system/libm",
            "libpng/system/libz",
        ],
    )
    
    bld.platform(
        target="libpng/libpng",
        includes="include/darwin src/darwin",
        export_includes="include/darwin",
        platform="darwin",
    )

    bld.program(
        target="libpng/pngtest",
        features="universal",
        source="libpng-1.6.0/pngtest.c",
        cflags="-Wall -Werror",
        use="libpng/libpng",
    )
