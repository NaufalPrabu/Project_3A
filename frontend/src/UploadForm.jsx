import React, { useState } from 'react';
import axios from 'axios';

function UploadForm() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState('');
  const [error, setError] = useState(''); // ✅ Tambahan: State untuk error

  const handleFileChange = (e) => {
    const selected = e.target.files[0];
    if (selected) {
      const ext = selected.name.split('.').pop().toLowerCase();
      if (ext !== 'jpg' && ext !== 'jpeg' && ext !== 'png') {
        setError('Format file tidak didukung. Gunakan gambar .jpg atau .png.');
        setFile(null);
        setPreview(null);
        setResult('');
      } else {
        setError(''); // Hapus error kalau valid
        setFile(selected);
        setPreview(URL.createObjectURL(selected));
        setResult('');
      }
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError('Silakan pilih file gambar yang valid.');
      return;
    }

    const formData = new FormData();
    formData.append('image', file);

    try {
      const res = await axios.post('http://localhost:5000/predict', formData);
      setResult(res.data.result || res.data.error);
    } catch (error) {
      console.error('Gagal memprediksi:', error);
      setResult('Terjadi kesalahan saat memproses gambar.');
    }
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        {preview && <img src={preview} alt="Preview" className="image-preview" />}
        {error && <p style={{ color: 'red', textAlign: 'center' }}>{error}</p>}
        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '10px' }}>
          <button type="submit">Deteksi Sekarang</button>
        </div>
      </form>
      {result && <div className="result">{result}</div>}
    </div>
  );
}

export default UploadForm;
