def search(request, queryKey, sortKey, searchMethod, modelClass):
    groupSearchQuery = request.GET.get(queryKey, '')
    sortBy = request.GET.get(sortKey, '')
    if(groupSearchQuery):
        if(sortBy):
            return searchMethod(groupSearchQuery, sortBy)
        return searchMethod(groupSearchQuery)
    else:
       if(sortBy):
            return modelClass.objects.all().order_by(sortBy)
       return modelClass.objects.all()

