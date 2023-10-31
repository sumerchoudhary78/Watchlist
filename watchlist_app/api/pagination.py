from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 1 # set no. of items on each page
    # page_query_param = 'p' # rename "page" attribute in url
    page_size_query_param = 'size' #taking page size from user
    max_page_size = 2 # max limit on no. of items on each page
    # last_page_strings = 'end' # to access the last page
    
class WatchListLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 2
    limit_query_param = 'limit'
    offset_query_param = 'start'
    
class WatchListCursorPagination(CursorPagination):
    page_size = 1
    ordering = 'created'
    cursor_query_param = 'record'