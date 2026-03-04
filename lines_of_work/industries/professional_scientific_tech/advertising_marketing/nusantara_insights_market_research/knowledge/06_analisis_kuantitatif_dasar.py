title = "Analisis Data Kuantitatif Dasar"

content = """
Analisis data kuantitatif transformasikan respons survey menjadi temuan yang dapat ditindaklanjuti.
Langkah standar meliputi data cleaning, statistik deskriptif, dan inferensial.

**Data Cleaning:** Hapus respons tidak lengkap, straight-liners (jawaban sama untuk semua),
atau speeders (waktu respons terlalu singkat). Tentukan aturan exclusion sebelum analisis dan
dokumentasikan. Periksa outliers dan putuskan apakah winsorize atau exclude.

**Statistik Deskriptif:** Frekuensi, mean, median, standar deviasi. Cross-tabulation untuk
hubungan antar variabel kategorikal. Visualisasi (bar chart, pie, crosstab heatmap) untuk
komunikasi ke klien. Pastikan pembobotan diterapkan bila sampel tidak proporsional.

**Inferensial:** Uji signifikansi (chi-square, t-test, ANOVA) untuk memastikan perbedaan
antar kelompok bukan sekadar noise. Laporkan p-value dan effect size. Hindari p-hacking:
tentukan hipotesis dan rencana analisis sebelum melihat data.
"""  # noqa: E501

version = "0.0.1"
