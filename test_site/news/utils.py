class DataMixin:
    title = None
    cat_selected = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cat_selected'] = self.cat_selected

        return context
