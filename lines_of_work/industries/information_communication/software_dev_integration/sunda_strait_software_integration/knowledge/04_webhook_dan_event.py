title = "Webhook dan Event Push untuk Integrasi"

content = """
Webhook memungkinkan sistem mendorong notifikasi ke endpoint lain ketika peristiwa terjadi,
bukan polling berulang. Penting untuk integrasi real-time dan efisiensi.

**Mekanisme:** Sistem sumber mendaftarkan URL callback. Ketika event terjadi (pesanan baru,
pembayaran dikonfirmasi, stok berubah), sistem mengirim HTTP POST ke URL dengan payload.
Penerima harus merespons cepat (misalnya 200 dalam beberapa detik) untuk mencegah retry.

**Keamanan:** Validasi tanda tangan (HMAC) menggunakan secret bersama. Periksa header
X-Webhook-Signature atau sejenisnya. Jangan percaya payload tanpa verifikasi. Gunakan
HTTPS wajib.

**Handling:** Idempotensi penting — event yang sama bisa dikirim ulang karena retry.
Gunakan event ID untuk deduplikasi. Implementasi queue di sisi penerima untuk memproses
asinkron dan menghindari timeout. Simpan audit log untuk debugging.
"""  # noqa: E501

version = "0.0.1"
