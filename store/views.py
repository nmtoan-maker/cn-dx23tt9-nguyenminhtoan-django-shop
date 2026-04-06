from django.http import HttpResponse

def home(request):
    return HttpResponse("Chào mừng đến với website bán linh kiện máy tính 🚀")