ifeq ($(TARGET_OS),linux)

LIBPNG_CPPFLAGS := $(shell pkg-config --cflags libpng)
LIBPNG_LDFLAGS := $(shell pkg-config --libs libpng)

else

LIBPNG_CPPFLAGS := \
	$(ZLIB_CPPFLAGS) \
	-I $(LIBPNG_ROOT)/include
LIBPNG_LDFLAGS := $(ZLIB_LDFLAGS)

LIBPNG_A := $(OUT)/libpng.a
LIBPNG_SRCS := \
	$(LIBPNG_ROOT)/libpng-1.6.28/png.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngerror.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngget.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngmem.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngpread.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngread.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngrio.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngrtran.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngrutil.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngset.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngtrans.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngwio.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngwrite.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngwtran.c \
	$(LIBPNG_ROOT)/libpng-1.6.28/pngwutil.c

LIBPNG_OBJS := $(LIBPNG_SRCS:%=$(OUT)/%.o)

$(LIBPNG_A): $(LIBPNG_OBJS)
	$(AR) rcs $@ $+

LIBPNG_PRIVATE_CPPFLAGS := \
	$(LIBPNG_CPPFLAGS) \
	-I $(LIBPNG_ROOT)/libpng-1.6.28 \
	-I $(LIBPNG_ROOT)/src

$(LIBPNG_OBJS): $(OUT)/%.c.o: %.c
	@$(MKDIR_P) $(dir $@)
	$(CC) $(CPPFLAGS) $(CFLAGS) $(LIBPNG_PRIVATE_CPPFLAGS) -c $< -o $@

-include $(LIBPNG_OBJS:.o=.d)

endif
