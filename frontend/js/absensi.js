// File: frontend/js/absensi.js
document.getElementById('tanggal').valueAsDate = new Date(); // Hari ini default

async function loadAbsensi() {
    const data = await api.get('/absensi/');
    const siswaData = await api.get('/siswa/');
    const tbody = document.querySelector('#table-absensi tbody');

    tbody.innerHTML = '';
    data.forEach(absen => {
        const siswa = siswaData.find(s => s.id === absen.siswa_id) || { nama: "(Terhapus)" };
        tbody.innerHTML += `
            <tr>
                <td>${absen.tanggal}</td>
                <td>${siswa.nama}</td>
                <td><span class="badge b-${absen.status}">${absen.status}</span></td>
                <td>${absen.keterangan || '-'}</td>
            </tr>`;
    });
}

document.getElementById('form-absensi').addEventListener('submit', async (e) => {
    e.preventDefault();
    const siswa_id = document.getElementById('siswa_id').value;
    if (!siswa_id) return alert("Pilih siswa dulu!");

    await api.post('/absensi/', {
        siswa_id: parseInt(siswa_id),
        tanggal: document.getElementById('tanggal').value,
        status: document.getElementById('status').value,
        keterangan: document.getElementById('keterangan').value
    });
    document.getElementById('keterangan').value = '';
    loadAbsensi();
});
