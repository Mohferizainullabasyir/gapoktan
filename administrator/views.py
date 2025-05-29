from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.functions import ExtractMonth
from django.db.models import Count, Sum
from .models import ProfilGapoktan, Kegiatan, Grup, KetuaKelompok, KetuaGapoktan, Petani, Alsintan, Lahan, DataERDKK
from .forms import ProfilGapoktanForm, KegiatanForm, GrupForm, KetuaKelompokForm, KetuaGapoktanForm, PetaniForm, AlsintanForm, LahanForm 
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
    "menu": "beranda",
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
    ketua_gapoktan_list = KetuaGapoktan.objects.all()
    context = {
            "judul": "Data KetuaKelompok",
            "menu":"ketua",
            "ketua_list":ketua,
            "ketua_gapoktan_list": ketua_gapoktan_list,
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

# ketua gapoktan

def formketuagapoktanadmin(request):
    if request.method == "POST":
        form = KetuaGapoktanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ketuaadmin')
    else:
        form = KetuaGapoktanForm()
    return render(request, 'formketuagapoktanadmin.html', {
        "judul": "Form KetuaGapoktan",
        "menu": "ketua",
        "form": form
    })

def editketuagapoktanadmin(request, pk):
    ketuagapoktan = get_object_or_404(KetuaGapoktan, id=pk)
    if request.method == "POST":
        form = KetuaGapoktanForm(request.POST, request.FILES, instance=ketuagapoktan)
        if form.is_valid():
            form.save()
            return redirect('ketuaadmin')
        else:
            print(form.errors)  # Ini akan tampil di terminal
    else:
        form = KetuaGapoktanForm(instance=ketuagapoktan)
    return render(request, 'formketuagapoktanadmin.html', {
        "judul": "Edit KetuaGapoktan",
        "menu": "ketua",
        "form": form
    })

def deleteketuagapoktanadmin(request, pk):
    ketuagapoktan = get_object_or_404(KetuaGapoktan, pk=pk)
    if request.method == 'POST':
        ketuagapoktan.delete()
        return redirect('ketuaadmin')
    return redirect('ketuaadmin')

# anggota

def anggotaadmin(request):
    anggota =  Petani.objects.all() 
    anggota_gapoktan_list = KetuaGapoktan.objects.all()
    context = {
            "judul": "Data Petani",
            "menu":"anggota",
            "anggota_list":anggota,
            "anggota_gapoktan_list": anggota_gapoktan_list,
        }
    return render(request, 'anggotaadmin.html', context)

def formanggotaadmin(request):
    if request.method == "POST":
        form = PetaniForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('anggotaadmin')
    else:
        form = PetaniForm()
    return render(request, 'formanggotaadmin.html', {
        "judul": "Form Petani",
        "menu": "anggota",
        "form": form
    })

def editanggotaadmin(request, pk):
    anggota = get_object_or_404(Petani, id=pk)
    if request.method == "POST":
        form = PetaniForm(request.POST, request.FILES, instance=anggota)
        if form.is_valid():
            form.save()
            return redirect('anggotaadmin')
        else:
            print(form.errors)  # Ini akan tampil di terminal
    else:
        form = PetaniForm(instance=anggota)
    return render(request, 'formanggotaadmin.html', {
        "judul": "Edit Petani",
        "menu": "anggota",
        "form": form
    })

def deleteanggotaadmin(request, pk):
    anggota = get_object_or_404(Petani, pk=pk)
    if request.method == 'POST':
        anggota.delete()
        return redirect('anggotaadmin')
    return redirect('anggotaadmin')

#alsintan

def alsintanadmin(request):
    alsintan =  Alsintan.objects.all() 
    context = {
            "judul": "Data Alsintan",
            "menu":"alsintan",
            "alsintan_list":alsintan,
        }
    return render(request, 'alsintanadmin.html', context)

def formalsintanadmin(request):
    if request.method == "POST":
        form = AlsintanForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            form.save()  # Simpan data ke database
            return redirect('alsintanadmin')  # Redirect ke halaman alsintan setelah menyimpan
    else:
        form = AlsintanForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Alsintan",
        "menu": "alsintan",
        "form": form
    }
    return render(request, 'formalsintanadmin.html', context)


def editalsintanadmin(request, pk):
    alsintan = get_object_or_404(Alsintan, id=pk)
    if request.method == "POST":
        form = AlsintanForm(request.POST, request.FILES, instance=alsintan)
        if form.is_valid():
            form.save()
            return redirect('alsintanadmin')  # Redirect ke halaman daftar alsintan
    else:
        form = AlsintanForm(instance=alsintan)
    context = {
         "judul": "Form Edit Alsintan",
        "menu": "alsintan",
        "form": form
    }
    return render(request, 'formalsintanadmin.html', context)


def deletealsintanadmin(request, pk):
    alsintan = get_object_or_404(Alsintan, pk=pk)
    if request.method == 'POST':
        alsintan.delete()
        return redirect('alsintanadmin')  
    return redirect('alsintanadmin')


#Lahan

def lahanadmin(request):
    lahan =  Lahan.objects.all() 
    context = {
            "judul": "Data Lahan",
            "menu":"lahan",
            "lahan_list":lahan,
        }
    return render(request, 'lahanadmin.html', context)

def formlahanadmin(request):
    if request.method == "POST":
        form = LahanForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            form.save()  # Simpan data ke database
            return redirect('lahanadmin')  # Redirect ke halaman lahan setelah menyimpan
    else:
        form = LahanForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Lahan",
        "menu": "lahan",
        "form": form
    }
    return render(request, 'formlahanadmin.html', context)


def editlahanadmin(request, pk):
    lahan = get_object_or_404(Lahan, id=pk)
    if request.method == "POST":
        form = LahanForm(request.POST, request.FILES, instance=lahan)
        if form.is_valid():
            form.save()
            return redirect('lahanadmin')  # Redirect ke halaman daftar lahan
    else:
        form = LahanForm(instance=lahan)
    context = {
         "judul": "Form Edit Lahan",
        "menu": "lahan",
        "form": form
    }
    return render(request, 'formlahanadmin.html', context)


def deletelahanadmin(request, pk):
    lahan = get_object_or_404(Lahan, pk=pk)
    if request.method == 'POST':
        lahan.delete()
        return redirect('lahanadmin')  
    return redirect('lahanadmin')