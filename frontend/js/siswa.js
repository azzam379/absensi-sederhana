// File: frontend/js/siswa.js
async function loadSiswa() {
    const data = await api.get('/siswa/');
    const tbody = document.querySelector('#table-siswa tbody');
    const select = document.querySelector('#siswa_id');

    tbody.innerHTML = '';
    select.innerHTML = '<option value="">-- Pilih Siswa --</option>';

    data.forEach((s, idx) => {
        tbody.innerHTML += `
            <tr>
                <td>${idx + 1}</td>
                <td>${s.nama}</td>
                <td>${s.kelas}</td>
                <td><button class="btn-delete" onclick="hapusSiswa(${s.id})">Hapus</button></td>
            </tr>`;
        select.innerHTML += `<option value="${s.id}">${s.nama} (${s.kelas})</option>`;
    });
}

document.getElementById('form-siswa').addEventListener('submit', async (e) => {
    e.preventDefault();
    await api.post('/siswa/', {
        nama: document.getElementById('nama').value,
        kelas: document.getElementById('kelas').value
    });
    document.getElementById('form-siswa').reset();
    loadSiswa();
});

async function hapusSiswa(id) {
    if (confirm('Hapus data siswa ini?')) {
        await api.delete(`/siswa/${id}`);
        loadSiswa();
        loadAbsensi();
    }
}
