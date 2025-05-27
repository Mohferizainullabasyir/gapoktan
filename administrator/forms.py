from django import forms
from .models import ProfilGapoktan, Kegiatan, Grup, KetuaKelompok, KetuaGapoktan 
from django.utils.text import slugify

class ProfilGapoktanForm(forms.ModelForm):
    class Meta:
        model = ProfilGapoktan
        fields = ['gambar_kantor', 'deskripsi_kantor', 'gambar_ketua', 'deskripsi_ketua']
        
        widgets = {
            'gambar_kantor': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
            }),
            'deskripsi_kantor': forms.Textarea(attrs={
                'class': 'textarea mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',
                'placeholder': 'Masukkan deskripsi kantor...',
                'rows': 4,
            }),
            'gambar_ketua': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
            }),
            'deskripsi_ketua': forms.Textarea(attrs={
                'class': 'textarea mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',
                'placeholder': 'Masukkan deskripsi ketua...',
                'rows': 4,
            }),
        }

        labels = {
            'gambar_kantor': 'Gambar Kantor',
            'deskripsi_kantor': 'Deskripsi Kantor',
            'gambar_ketua': 'Gambar Ketua',
            'deskripsi_ketua': 'Deskripsi Ketua',
        }


class KegiatanForm(forms.ModelForm):
    class Meta:
        model = Kegiatan
        fields = ['judul', 'tanggal', 'deskripsi', 'gambar']
        
        widgets = {
            'judul': forms.TextInput(attrs={
                'class': 'input mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
                'placeholder': 'Judul kegiatan',
            }),
            'tanggal': forms.DateInput(attrs={
                'type': 'date',
                'class': 'input mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
            }),
            'deskripsi': forms.Textarea(attrs={
                'class': 'textarea mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
                'rows': 4,
                'placeholder': 'Deskripsi kegiatan',
            }),
            'gambar': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
            }),
        }

        labels = {
            'judul': 'Judul Kegiatan',
            'tanggal': 'Tanggal',
            'deskripsi': 'Deskripsi',
            'gambar': 'Dokumentasi / Gambar',
        }
        
class GrupForm(forms.ModelForm):
    class Meta:
        model = Grup
        fields = ['nama', 'aktif']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-input border rounded w-full',
                'placeholder': 'Masukkan nama grup'
            }),
            'aktif': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Auto generate slug from nama
        instance.slug = slugify(self.cleaned_data['nama'])
        if commit:
            instance.save()
        return instance
    
class KetuaKelompokForm(forms.ModelForm):
    class Meta:
        model = KetuaKelompok
        fields = ['grup', 'nama', 'nik', 'no_hp', 'alamat']

        widgets = {
            'grup': forms.SelectMultiple(attrs={
                'class': 'select mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
            }),

            'nama': forms.TextInput(attrs={
                'class': 'input mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
                'placeholder': 'Nama Ketua Kelompok',
            }),
            'nik': forms.TextInput(attrs={
                'class': 'input mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
                'placeholder': 'NIK',
            }),
            'no_hp': forms.TextInput(attrs={
                'class': 'input mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
                'placeholder': 'No HP',
            }),
            'alamat': forms.Textarea(attrs={
                'class': 'textarea mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
                'rows': 3,
                'placeholder': 'Alamat Ketua Kelompok',
            }),
        }

        labels = {
            'grup': 'Grup Tani',
            'nama': 'Nama Ketua',
            'nik': 'NIK',
            'no_hp': 'Nomor HP',
            'alamat': 'Alamat',
        }
        


class KetuaGapoktanForm(forms.ModelForm):
    class Meta:
        model = KetuaGapoktan
        fields = ['grup', 'nama', 'nik', 'no_hp', 'alamat']

        widgets = {
            'grup': forms.Select(attrs={
                'class': 'select mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
            }),
            'nama': forms.TextInput(attrs={
                'class': 'input mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
                'placeholder': 'Nama Ketua Gapoktan',
            }),
            'nik': forms.TextInput(attrs={
                'class': 'input mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
                'placeholder': 'NIK',
            }),
            'no_hp': forms.TextInput(attrs={
                'class': 'input mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
                'placeholder': 'Nomor HP',
            }),
            'alamat': forms.Textarea(attrs={
                'class': 'textarea mt-1 block w-full border border-gray-300 rounded-md py-2 px-3 focus:ring focus:ring-blue-200',
                'rows': 3,
                'placeholder': 'Alamat Ketua Gapoktan',
            }),
        }

        labels = {
            'grup': 'Grup Gapoktan',
            'nama': 'Nama Ketua',
            'nik': 'NIK',
            'no_hp': 'Nomor HP',
            'alamat': 'Alamat',
        }
