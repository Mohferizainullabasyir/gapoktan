from django.shortcuts import render

def dashboard(request):
    context = {
        "judul": "Halaman Ketua",
        "isi": "Info Terkini Terkait Lahan Pertanian ",
        }
    return render(request, 'dashboard.html', context)
