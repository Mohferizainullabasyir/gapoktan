from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.db.models.functions import ExtractMonth
from django.db.models import Count, Sum, Q
from administrator.models import (ProfilGapoktan, Kegiatan, Alsintan, Lahan, Grup, KetuaKelompok, KetuaGapoktan, Petani, DataERDKK, KesehatanTanaman, ForumDiskusi, KomentarDiskusi)
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
import json
from django.urls import reverse
from django.utils import timezone
from django import forms

def beranda(request):
    # Data petani per bulan
    petani_per_bulan = [Petani.objects.filter(created_at__month=bulan).count() for bulan in range(1, 13)]

    # Data lahan per bulan
    lahan_per_bulan = [Lahan.objects.filter(created_at__month=bulan).count() for bulan in range(1, 13)]

    # Hitung kebutuhan pupuk per jenis
    total_urea = DataERDKK.objects.filter(jenis_pupuk='UREA').aggregate(total=Sum('jumlah_kebutuhan'))['total'] or 0
    total_npk = DataERDKK.objects.filter(jenis_pupuk='NPK').aggregate(total=Sum('jumlah_kebutuhan'))['total'] or 0
    total_organik = DataERDKK.objects.filter(jenis_pupuk='ORGANIK').aggregate(total=Sum('jumlah_kebutuhan'))['total'] or 0

    context = {
        "judul": "Halaman Petani",
        "menu": "beranda", 
        'petani_per_bulan': petani_per_bulan,
        'lahan_per_bulan': lahan_per_bulan,
        'urea': total_urea,
        'npk': total_npk,
        'organik': total_organik,
    }
    return render(request, 'beranda.html', context)


def profil(request):
    profil = ProfilGapoktan.objects.last()
    latest_kegiatan = Kegiatan.objects.order_by('-tanggal').first()  # Ambil 1 kegiatan terbaru
    context = {
        "judul": "Profil Gapoktan",
        "profil": profil,
        "menu":"profil",
        'latest_kegiatan': latest_kegiatan,
    }
    return render(request, 'profil.html', context)


def kegiatan_list(request):
    kegiatan_list = Kegiatan.objects.all().order_by('-tanggal')  # urutkan dari yang terbaru
    context = {
        'kegiatan_list': kegiatan_list,
    }
    return render(request, 'kegiatan_list.html', context)


def profil_kantor(request):
    profil = ProfilGapoktan.objects.last()
    return render(request, 'profil_kantor.html', {'profil': profil})


def profil_ketua(request):
    profil = ProfilGapoktan.objects.last()
    return render(request, 'profil_ketua.html', {'profil': profil})


def grup(request):
    query = request.GET.get('q')
    if query:
        query_grup = Grup.objects.filter(Q(nama__icontains=query)).order_by('-id')
    else:
        query_grup = Grup.objects.order_by('-id')

    context = {
        "judul": "Halaman grup",
        "menu":"grup",
        'grup': query_grup,
    }
    return render(request, 'grup.html', context)


def ketua(request):
    query = request.GET.get('q')
    if query:
        poktan = KetuaKelompok.objects.filter(
            Q(nama__icontains=query) | Q(grup__nama__icontains=query)
        ).order_by('-id').distinct()
        gapoktan = KetuaGapoktan.objects.filter(
            Q(nama__icontains=query) | Q(grup__nama__icontains=query)
        ).order_by('-id').distinct()
    else:
        poktan = KetuaKelompok.objects.order_by('-id')
        gapoktan = KetuaGapoktan.objects.order_by('-id')

    context = {
        'judul': 'Halaman Ketua',
        'menu': 'ketua',
        'poktan': poktan,
        'gapoktan': gapoktan,
    }
    return render(request, 'ketua.html', context)



def anggota(request):
    query = request.GET.get('q')
    if query:
        query_petani = Petani.objects.filter(
            Q(nama__icontains=query) | Q(grup__nama__icontains=query)
        ).order_by('-id')
    else:
        query_petani = Petani.objects.order_by('-id')

    context = {
        "judul": "Halaman anggota",
        "menu": "anggota",
        'petani': query_petani,
    }
    return render(request, 'anggota.html', context)


def alsintan(request):
    daftar_alsintan = Alsintan.objects.all().order_by('-id')
    context = {
        "judul": "Halaman Alsintan",
        "menu": "alsintan",
        "daftar_alsintan": daftar_alsintan,
    }
    return render(request, 'alsintan.html', context)

def lahan(request):
    query = request.GET.get('q')
    if query:
        query_lahan = Lahan.objects.filter(
            Q(pemilik__nama__icontains=query) |
            Q(jenis_tanaman__icontains=query) |
            Q(lokasi__icontains=query)
        ).order_by('-id')
    else:
        query_lahan = Lahan.objects.order_by('-id')

    # Data untuk Google Maps
    lahan_data = [
        {
            'pemilik': l.pemilik.nama,
            'luas': l.luas,
            'jenis_tanaman': l.jenis_tanaman,
            'latitude': l.latitude,
            'longitude': l.longitude
        } for l in query_lahan if l.latitude and l.longitude
    ]

    context = {
        'judul': 'Halaman Lahan',
        "menu": "lahan",
        'lahan': query_lahan,
        'daftar_petani': Petani.objects.all(),
        'lahan_json': json.dumps(lahan_data, cls=DjangoJSONEncoder),
    }
    return render(request, 'lahan.html', context)


def tambah_lahan(request):
    if request.method == 'POST':
        gambar = request.FILES.get('gambar')
        pemilik_id = request.POST.get('pemilik')
        luas = request.POST.get('luas')
        jenis_tanaman = request.POST.get('jenis_tanaman')
        lokasi = request.POST.get('lokasi')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        try:
            pemilik_obj = Petani.objects.get(id=pemilik_id)
        except Petani.DoesNotExist:
            return HttpResponse("Pemilik tidak ditemukan", status=400)

        Lahan.objects.create(
            gambar_lahan=gambar,
            pemilik=pemilik_obj,
            luas=luas,
            jenis_tanaman=jenis_tanaman,
            lokasi=lokasi,
            latitude=latitude,
            longitude=longitude,
        )
        return redirect('lahan')

    return redirect('lahan')


def erdkk(request):
    daftar_erdkk = DataERDKK.objects.all().order_by('-tahun_rencana')
    context = {
        'judul': 'Data ERDKK',
        "menu": "erdkk",
        'daftar_erdkk': daftar_erdkk
    }
    return render(request, 'erdkk.html', context)


def tanaman(request):
    query_tanaman = KesehatanTanaman.objects.order_by('-id')
    context = {
        "judul": "Halaman Tanaman",
        "menu": "tanaman",
        'tanaman': query_tanaman,
    }
    return render(request, 'tanaman.html', context)

# Form untuk ForumDiskusi dan KomentarDiskusi
class ForumDiskusiForm(forms.ModelForm):
    class Meta:
        model = ForumDiskusi
        fields = ['judul', 'isi']

class KomentarDiskusiForm(forms.ModelForm):
    class Meta:
        model = KomentarDiskusi
        fields = ['isi']

# Views

def daftar_forum(request):
    forum_list = ForumDiskusi.objects.all().order_by('-tanggal')
    context = {
        'forum_list': forum_list,
        "menu": "forum",
    }
    return render(request, 'daftar_forum.html', context)


def detail_forum(request, forum_id):
    forum = get_object_or_404(ForumDiskusi, id=forum_id)
    komentar_list = forum.komentar.all().order_by('tanggal')

    if request.method == 'POST':
        form_komentar = KomentarDiskusiForm(request.POST)
        if form_komentar.is_valid():
            komentar = form_komentar.save(commit=False)
            komentar.user = request.user
            komentar.forum = forum
            komentar.tanggal = timezone.now()
            komentar.save()
            return redirect('detail_forum', forum_id=forum.id)
    else:
        form_komentar = KomentarDiskusiForm()

    context = {
        'forum': forum,
        'komentar_list': komentar_list,
        'form_komentar': form_komentar,
    }
    return render(request, 'detail_forum.html', context)


def buat_forum(request):
    if request.method == 'POST':
        form = ForumDiskusiForm(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.user = request.user
            forum.tanggal = timezone.now()
            forum.save()
            return redirect('daftar_forum')
    else:
        form = ForumDiskusiForm()

    return render(request, 'buat_forum.html', {'form': form})