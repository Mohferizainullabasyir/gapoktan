from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.functions import ExtractMonth
from django.db.models import Count, Sum
from .models import ProfilGapoktan, Kegiatan, Grup, KetuaKelompok, Petani, Lahan, DataERDKK
from .forms import ProfilGapoktanForm, KegiatanForm, GrupForm, KetuaKelompokForm 
from datetime import datetime

def dashboard(request):
   # Data petani per bulan
    petani_per_bulan = [Petani.objects.filter(created_at__month=bulan).count() for bulan in range(1, 13)]

    # Data lahan per bulan
    lahan_per_bulan = [Lahan.objects.filter(created_at__month=bulan).count() for bulan in range(1, 13)]

    # Hitung kebutuhan pupuk per jenis
    total_urea = DataERDKK.objects.filter(jenis_pupuk='UREA').aggregate(total=Sum('jumlah_kebutuhan'))['total'] or 0
    total_npk = DataERDKK.objects.filter(jenis_pupuk='NPK').aggregate(total=Sum('jumlah_kebutuhan'))['total'] or 0
    total_organik = DataERDKK.objects.filter(jenis_pupuk='ORGANIK').aggregate(total=Sum('jumlah_kebutuhan'))['total'] or 0

    context = {
    "judul": "Halaman Admin",
    'petani_per_bulan': petani_per_bulan,
    'lahan_per_bulan': lahan_per_bulan,
    'urea': total_urea,
    'npk': total_npk,
    'organik': total_organik,
    }
    return render(request, 'dashboardadmin.html', context)

def profiladmin(request):
    profil =  ProfilGapoktan.objects.all() 
    kegiatan_list = Kegiatan.objects.all() 
    context = {
            "judul": "Data Profil",
            "menu":"profil",
            "profil_list":profil,
            "kegiatan_list": kegiatan_list,
        }
    return render(request, 'profiladmin.html', context)

def formprofiladmin(request):
    if request.method == "POST":
        form = ProfilGapoktanForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            form.save()  # Simpan data ke database
            return redirect('profiladmin')  # Redirect ke halaman profil setelah menyimpan
    else:
        form = ProfilGapoktanForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form ProfilGapoktan",
        "menu": "profil",
        "form": form
    }
    return render(request, 'formprofiladmin.html', context)


def editprofiladmin(request, pk):
    profil = get_object_or_404(ProfilGapoktan, id=pk)
    if request.method == "POST":
        form = ProfilGapoktanForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            return redirect('profiladmin')  # Redirect ke halaman daftar profil
    else:
        form = ProfilGapoktanForm(instance=profil)
    context = {
         "judul": "Form Edit ProfilGapoktan",
        "menu": "profil",
        "form": form
    }
    return render(request, 'formprofiladmin.html', context)


def deleteprofiladmin(request, pk):
    profil = get_object_or_404(ProfilGapoktan, pk=pk)
    if request.method == 'POST':
        profil.delete()
        return redirect('profiladmin')  
    return redirect('profiladmin')

#form kegiatan

def formkegiatanadmin(request):
    if request.method == "POST":
        form = KegiatanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profiladmin')
    else:
        form = KegiatanForm()
    return render(request, 'formkegiatanadmin.html', {
        "judul": "Form Kegiatan",
        "menu": "profil",
        "form": form
    })

def editkegiatanadmin(request, pk):
    kegiatan = get_object_or_404(Kegiatan, id=pk)
    if request.method == "POST":
        form = KegiatanForm(request.POST, request.FILES, instance=kegiatan)
        if form.is_valid():
            form.save()
            return redirect('profiladmin')
    else:
        form = KegiatanForm(instance=kegiatan)
    return render(request, 'formkegiatanadmin.html', {
        "judul": "Edit Kegiatan",
        "menu": "profil",
        "form": form
    })

def deletekegiatanadmin(request, pk):
    kegiatan = get_object_or_404(Kegiatan, pk=pk)
    if request.method == 'POST':
        kegiatan.delete()
        return redirect('profiladmin')
    return redirect('profiladmin')

#grup

def grupadmin(request):
    grup =  Grup.objects.all() 
    kegiatan_list = Kegiatan.objects.all() 
    context = {
            "judul": "Data Grup",
            "menu":"grup",
            "grup_list":grup,
            "kegiatan_list": kegiatan_list,
        }
    return render(request, 'grupadmin.html', context)

def formgrupadmin(request):
    if request.method == "POST":
        form = GrupForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            form.save()  # Simpan data ke database
            return redirect('grupadmin')  # Redirect ke halaman grup setelah menyimpan
    else:
        form = GrupForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Grup",
        "menu": "grup",
        "form": form
    }
    return render(request, 'formgrupadmin.html', context)


def editgrupadmin(request, pk):
    grup = get_object_or_404(Grup, id=pk)
    if request.method == "POST":
        form = GrupForm(request.POST, request.FILES, instance=grup)
        if form.is_valid():
            form.save()
            return redirect('grupadmin')  # Redirect ke halaman daftar grup
    else:
        form = GrupForm(instance=grup)
    context = {
         "judul": "Form Edit Grup",
        "menu": "grup",
        "form": form
    }
    return render(request, 'formgrupadmin.html', context)


def deletegrupadmin(request, pk):
    grup = get_object_or_404(Grup, pk=pk)
    if request.method == 'POST':
        grup.delete()
        return redirect('grupadmin')  
    return redirect('grupadmin')

#ketua poktan 

def ketuaadmin(request):
    ketua =  KetuaKelompok.objects.all() 
    kegiatan_list = Kegiatan.objects.all() 
    context = {
            "judul": "Data KetuaKelompok",
            "menu":"ketua",
            "ketua_list":ketua,
            "kegiatan_list": kegiatan_list,
        }
    return render(request, 'ketuaadmin.html', context)

def formketuaadmin(request):
    if request.method == "POST":
        form = KetuaKelompokForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ketuaadmin')
    else:
        form = KetuaKelompokForm()
    return render(request, 'formketuaadmin.html', {
        "judul": "Form KetuaKelompok",
        "menu": "ketua",
        "form": form
    })

def editketuaadmin(request, pk):
    ketua = get_object_or_404(KetuaKelompok, id=pk)
    if request.method == "POST":
        form = KetuaKelompokForm(request.POST, request.FILES, instance=ketua)
        if form.is_valid():
            form.save()
            return redirect('ketuaadmin')
        else:
            print(form.errors)  # Ini akan tampil di terminal
    else:
        form = KetuaKelompokForm(instance=ketua)
    return render(request, 'formketuaadmin.html', {
        "judul": "Edit KetuaKelompok",
        "menu": "ketua",
        "form": form
    })

def deleteketuaadmin(request, pk):
    ketua = get_object_or_404(KetuaKelompok, pk=pk)
    if request.method == 'POST':
        ketua.delete()
        return redirect('ketuaadmin')
    return redirect('ketuaadmin')