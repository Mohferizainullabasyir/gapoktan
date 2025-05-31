from django.contrib import admin
from .models import ProfilGapoktan, Kegiatan, Grup, KetuaKelompok, KetuaGapoktan, Petani, Alsintan, Lahan, DataERDKK, KesehatanTanaman,  ForumDiskusi, KomentarDiskusi
from django.utils.html import format_html


@admin.register(ProfilGapoktan)
class ProfilGapoktanAdmin(admin.ModelAdmin):
    list_display=('id', 'gambar_kantor', 'deskripsi_kantor', 'gambar_ketua', 'deskripsi_ketua', 'updated_at',)

@admin.register(Kegiatan)
class KegiatanAdmin(admin.ModelAdmin):
    list_display = ('id','judul', 'tanggal', 'preview_gambar','slug',)
    search_fields = ('judul', 'deskripsi')
    list_filter = ('tanggal',)
    ordering = ('-tanggal',)

    def preview_gambar(self, obj):
        if obj.gambar:
            return format_html('<img src="{}" width="80" style="border-radius: 6px;" />', obj.gambar.url)
        return "-"
    preview_gambar.short_description = "Dokumentasi"
    
@admin.register(Grup)
class GrupAdmin(admin.ModelAdmin):
    list_display=('id', 'nama', 'aktif','slug',)
    prepopulated_fields = {"slug": ("nama",)} 

@admin.register(KetuaKelompok)
class KetuaKelompokAdmin(admin.ModelAdmin):
    list_display = ('id', 'daftar_grup', 'nama', 'nik', 'no_hp', 'alamat','slug')
    filter_horizontal = ('grup',)

    def daftar_grup(self, obj):
        return ", ".join([g.nama for g in obj.grup.all()])

    daftar_grup.short_description = 'Grup'
    
@admin.register(KetuaGapoktan)
class KetuaGapoktanAdmin(admin.ModelAdmin):
    list_display = ('id', 'grup', 'nama', 'nik_tersembunyi', 'no_hp', 'alamat','slug')

    
@admin.register(Petani)
class PetaniAdmin(admin.ModelAdmin):
    list_display=('id', 'grup', 'nama', 'nik', 'no_hp', 'alamat','slug')

@admin.register(Alsintan)
class AlsintanAdmin(admin.ModelAdmin):
    list_display = ('id','nama_alat','jenis_alat','jumlah','kondisi','tanggal_pengadaan','sumber_dana','slug')
    search_fields = ('nama_alat', 'jenis_alat')
    list_filter = ('kondisi', 'tanggal_pengadaan')

    
@admin.register(Lahan)
class LahanAdmin(admin.ModelAdmin):
    list_display=('id', 'pemilik', 'gambar_lahan', 'luas', 'jenis_tanaman', 'lokasi','latitude','longitude', 'tanggal_tanam', 'tanggal_panen', 'progress_tanam','slug')
    prepopulated_fields = {"slug": ("pemilik",)} 
    
@admin.register(DataERDKK)
class DataERDKKAdmin(admin.ModelAdmin):
    list_display = ('petani', 'komoditas', 'luas_lahan', 'jenis_pupuk', 'jumlah_kebutuhan', 'tahun_rencana','slug')
    search_fields = ('petani__nama_petani', 'komoditas', 'jenis_pupuk')
    list_filter = ('tahun_rencana', 'jenis_pupuk', 'komoditas')
    prepopulated_fields = {"slug": ("petani",)}
    
@admin.register(KesehatanTanaman)
class KesehatanTanamanAdmin(admin.ModelAdmin):
    list_display=('id', 'lahan', 'kondisi', 'gambar_tanaman', 'isi_penyakit_dan_tindakan')
    
class KomentarDiskusiInline(admin.TabularInline):
    model = KomentarDiskusi
    extra = 1
    verbose_name_plural = "Komentar"

@admin.register(ForumDiskusi)
class ForumDiskusiAdmin(admin.ModelAdmin):
    list_display = ("judul", "user", "tanggal")
    search_fields = ("judul", "isi", "user__username")
    ordering = ("-tanggal",)
    inlines = [KomentarDiskusiInline]


@admin.register(KomentarDiskusi)
class KomentarDiskusiAdmin(admin.ModelAdmin):
    list_display = ("forum", "user", "tanggal")
    search_fields = ("forum__judul", "isi", "user__username")
    ordering = ("-tanggal",)