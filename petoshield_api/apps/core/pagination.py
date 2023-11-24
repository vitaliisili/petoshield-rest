from rest_framework import pagination


class ResultSetPagination(pagination.PageNumberPagination):
    """A custom pagination class for result sets.
    Attributes:
        page_size (int): The number of results to be displayed per page. Default is 20.
        page_size_query_param (str): The query parameter name for specifying the page size. Default is 'page_size'.
        max_page_size (int): The maximum allowed page size. Default is 100.
    """

    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        """Paginates the given queryset based on the request parameters.
        Args:
            queryset (QuerySet): The original queryset to be paginated.
            request (HttpRequest): The request object containing the query parameters.
            view (APIView, optional): The view object associated with the queryset.
            Default is None.
        Returns:
            PaginatedQuerySet: The paginated queryset.
        Raises:
            None
        Note:
            This method overrides the base class method to add custom pagination behavior.
        """
        if request.query_params.get(self.page_query_param) is None:
            return None
        return super().paginate_queryset(queryset, request, view)
