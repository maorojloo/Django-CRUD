from django.shortcuts import redirect


class CheckUser(object):

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        if not request.user.is_authenticated() and \
                        request.path.startswith('/dadmin/'):
            return redirect("/login/")

        response = self.get_response(request)


        return response