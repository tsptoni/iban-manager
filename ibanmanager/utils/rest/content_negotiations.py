from rest_framework.negotiation import DefaultContentNegotiation

class MediaTypeContentNegotiation(DefaultContentNegotiation):


    def select_renderer(self, request, renderers, format_suffix=None):

        http_accept = request.META.get('HTTP_ACCEPT', '*/*')

        path = request.query_params.get('path', '').lower()

        if path.endswith('.jpg') or path.endswith('.jpeg'):
            http_accept = 'image/jpeg,' + http_accept
        elif path.endswith('.png'):
            http_accept = 'image/png,' + http_accept
        elif path.endswith('.mp3') or path.endswith('.m4a'):
            http_accept = 'audio/mpeg,' + http_accept

        request.META['HTTP_ACCEPT'] = http_accept

        return super(MediaTypeContentNegotiation,self).select_renderer(request, renderers, format_suffix)
