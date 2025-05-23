# SQLite database header constants
HEADER_FORMAT = ">16sH6B14I"  # Corrected format string
HEADER_SIZE = 100  # bytes

# Header field positions (remain the same)
MAGIC_STRING = 0
PAGE_SIZE = 1
WRITE_VERSION = 2
READ_VERSION = 3
RESERVED_SPACE = 4
MAX_PAYLOAD_FRACTION = 5
MIN_PAYLOAD_FRACTION = 6
LEAF_PAYLOAD_FRACTION = 7
FILE_CHANGE_COUNTER = 8
DATABASE_SIZE = 9
FIRST_FREELIST_PAGE = 10
FREELIST_PAGE_COUNT = 11
SCHEMA_COOKIE = 12
SCHEMA_FORMAT = 13
PAGE_CACHE_SIZE = 14
LARGEST_ROOT_PAGE = 15
TEXT_ENCODING = 16
USER_VERSION = 17
INCREMENTAL_VACUUM = 18
APPLICATION_ID = 19
VERSION_VALID_FOR = 20
SQLITE_VERSION = 21

# Magic string for valid SQLite databases
SQLITE_MAGIC_STRING = b"SQLite format 3\x00"