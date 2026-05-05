from rest_framework.pagination import PageNumberPagination

class My_Pagination(PageNumberPagination):
    page_size = 30 # bir sahifada nechta ma'lumot kelishi
    page_size_query_param = 'page_size'
    max_page_size = 10_000 # sahifalar soni
